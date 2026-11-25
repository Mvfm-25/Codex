<#
.SYNOPSIS
  Compara os recursos de um curso do Moodle com os arquivos da cadeira e baixa o que falta,
  usando a sessão já logada do browser do WMux (aba própria, fechada no fim).

.PARAMETER CursoUrl     course/view.php?id=N
.PARAMETER PastaCadeira pasta da cadeira no vault (ex.: C:\...\PUC\ss)
.PARAMETER Baixar       sem esta opção, só lista (nada é gravado no vault)
.PARAMETER MaxMB        não baixa arquivos maiores que isso (padrão 15)

Destino dos novos arquivos: provas/<p1|p2|p3|ps|g2>/ quando o nome indica prova
("P2 - Exemplo", "SS___PS___..."), senão atividades/. Arquivos com o mesmo conteúdo (SHA-1) de
um arquivo local são reconhecidos mesmo com outro nome. Imprime JSON (ASCII) com, por recurso:
secao, nome, id, status (local|novo|baixado|grande|erro|nao_arquivo), arquivo.
#>
param(
  [Parameter(Mandatory = $true)][string]$CursoUrl,
  [Parameter(Mandatory = $true)][string]$PastaCadeira,
  [switch]$Baixar,
  [int]$MaxMB = 15,
  # regex sobre o nome do recurso/arquivo: o que não baixar mesmo sendo novo (executáveis sempre ficam de fora)
  [string]$Ignorar = '^$'
)

if (-not (Test-Path '\\.\pipe\wmux')) { '{"ok":false,"erro":"wmux_indisponivel"}'; exit 0 }
$pipeToken = (Get-Content "$env:APPDATA\wmux\pipe-token" -Raw).Trim()
$client = New-Object System.IO.Pipes.NamedPipeClientStream('.', 'wmux', [System.IO.Pipes.PipeDirection]::InOut); $client.Connect(3000)
$writer = New-Object System.IO.StreamWriter($client); $writer.AutoFlush = $true; $reader = New-Object System.IO.StreamReader($client)
function Invoke-WMux($method, $params = @{}) {
  $writer.Write((ConvertTo-Json @{ method = $method; params = $params; token = $pipeToken } -Compress -Depth 10) + "`n")
  return ($reader.ReadLine() | ConvertFrom-Json)
}
$me = "moodle-sync-$(Get-Random)"
$t = (Invoke-WMux 'browser.target' @{ caller = $me; fresh = $true }).result
function Go($url) {
  Invoke-WMux 'browser.navigate' @{ caller = $me; url = $url } | Out-Null
  Invoke-WMux 'browser.waitfor' @{ caller = $me; loadState = 'complete'; timeout = 20000 } | Out-Null
  Start-Sleep -Milliseconds 1200
}
function Eval($js) { return (Invoke-WMux 'browser.eval' @{ caller = $me; js = $js }).result.result }

# hashes dos arquivos locais
$sha = [System.Security.Cryptography.SHA1]::Create()
$locais = @{}
Get-ChildItem -Recurse -File $PastaCadeira | Where-Object { $_.FullName -notmatch '\\materiais\\\.cache\\|\\\.git\\' } | ForEach-Object {
  try { $h = [BitConverter]::ToString($sha.ComputeHash([IO.File]::ReadAllBytes($_.FullName))).Replace('-', ''); $locais[$h] = $_.FullName.Substring($PastaCadeira.Length + 1) } catch {}
}

$res = New-Object System.Collections.ArrayList
try {
  Go $CursoUrl
  if ((Eval 'location.href') -match 'login') { throw 'moodle_exige_login' }
  $id = ([regex]'id=(\d+)').Match($CursoUrl).Groups[1].Value
  $nsec = [int](Eval "Math.max(0, ...Array.from(document.querySelectorAll('a[href*=`"section=`"]')).map(a => +((a.href.match(/[?&]section=(\d+)/) || [0, 0])[1])))")
  for ($s = 0; $s -le [Math]::Max($nsec, 20); $s++) {
    Go "https://moodle.pucrs.br/course/view.php?id=$id&section=$s"
    $js = "(() => { const h = ((document.querySelector('#region-main h2, #region-main h3') || {}).textContent || '').trim(); const ls = Array.from(document.querySelectorAll('#region-main a')).filter(a => /mod\/(resource|folder|url)\/view\.php\?id=\d+/.test(a.href)).map(a => ({nome: a.textContent.replace(/\s+/g, ' ').trim().replace(/ (Arquivo|URL|Pasta|File|Folder)$/, ''), href: a.href})); const vistos = new Set(); return JSON.stringify({h, ls: ls.filter(x => !vistos.has(x.href) && vistos.add(x.href))}); })()"
    $sec = (Eval $js) | ConvertFrom-Json
    if (-not $sec.ls -or $sec.ls.Count -eq 0) { if ($s -gt $nsec) { break } else { continue } }
    foreach ($r in $sec.ls) {
      $rid = ([regex]'id=(\d+)').Match($r.href).Groups[1].Value
      $item = [ordered]@{ secao = $sec.h; nome = $r.nome; id = $rid; status = ''; arquivo = '' }
      if ($r.href -notmatch 'mod/resource/') { $item.status = 'nao_arquivo'; [void]$res.Add($item); continue }
      $jsF = @"
(async () => {
  const r = await fetch('https://moodle.pucrs.br/mod/resource/view.php?id=$rid&redirect=1', {credentials: 'include'});
  const tam = +(r.headers.get('content-length') || 0);
  if (tam > $MaxMB * 1048576) return JSON.stringify({grande: tam});
  const cd = r.headers.get('content-disposition') || '';
  let m = cd.match(/filename\*=UTF-8''([^;]+)/i), nome;
  if (m) nome = decodeURIComponent(m[1]);
  else { m = cd.match(/filename="?([^";]+)"?/i);
         nome = m ? m[1] : decodeURIComponent(r.url.split('/').pop().split('?')[0]);
         try { nome = decodeURIComponent(escape(nome)); } catch (e) {} }   // cabeçalho lido como Latin-1
  const b = new Uint8Array(await r.arrayBuffer());
  let s = ''; for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000));
  return JSON.stringify({ok: r.ok, tipo: r.headers.get('content-type'), nome, b64: btoa(s)});
})()
"@
      try {
        $o = (Eval $jsF) | ConvertFrom-Json
        if ($o.grande) { $item.status = 'grande'; $item.arquivo = "$([math]::Round($o.grande/1MB,1)) MB"; [void]$res.Add($item); continue }
        if (-not $o.ok -or $o.tipo -match 'text/html') { $item.status = 'erro'; [void]$res.Add($item); continue }
        $bytes = [Convert]::FromBase64String($o.b64)
        $h = [BitConverter]::ToString($sha.ComputeHash($bytes)).Replace('-', '')
        if ($locais.ContainsKey($h)) { $item.status = 'local'; $item.arquivo = $locais[$h]; [void]$res.Add($item); continue }
        $nome = $o.nome -replace '[\\/:*?"<>|]', '_'
        if ([IO.Path]::GetExtension($nome) -eq '') { $nome = ($r.nome -replace '[\\/:*?"<>|]', '_') + '.txt' }
        $pm = [regex]::Match("$($r.nome) $nome", '(?i)\b(P[1-3]|PS|G2)\b(?=[\s_\-.]|$)')
        $dest = if ($pm.Success -and ("$($r.nome) $nome" -match '(?i)prova|exemplo|_P[1-3]|_PS|^P[1-3]\b|^PS\b')) { "provas\$($pm.Groups[1].Value.ToLower())" } else { 'atividades' }
        $rel = "$dest\$nome"
        $item.arquivo = $rel
        if ($nome -match '(?i)\.(exe|msi|bat|cmd|ps1|dll|scr|jar)$' -or "$($r.nome) $nome" -match $Ignorar) {
          $item.status = 'ignorado'; [void]$res.Add($item); continue
        }
        if ($Baixar) {
          $abs = Join-Path $PastaCadeira $rel
          New-Item -ItemType Directory -Force (Split-Path $abs) | Out-Null
          if (Test-Path $abs) { $abs = Join-Path (Split-Path $abs) ("moodle-$rid-" + $nome); $item.arquivo = $abs.Substring($PastaCadeira.Length + 1) }
          [IO.File]::WriteAllBytes($abs, $bytes); $locais[$h] = $item.arquivo
          $item.status = 'baixado'
        } else { $item.status = 'novo' }
      } catch { $item.status = 'erro' }
      [void]$res.Add($item)
    }
  }
  $saida = @{ ok = $true; recursos = $res }
} catch {
  $saida = @{ ok = $false; erro = "$($_.Exception.Message)"; recursos = $res }
} finally {
  if ($t.created) { Invoke-WMux 'surface.close' @{ id = $t.surfaceId } | Out-Null }
  $client.Close()
}
# ASCII puro: o console do Windows (cp1252) estraga nomes com acento
$json = $saida | ConvertTo-Json -Depth 6 -Compress
[regex]::Replace($json, '[^\x00-\x7F]', { param($m) '\u{0:x4}' -f [int][char]$m.Value })
