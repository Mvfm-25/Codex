<#
.SYNOPSIS
  Baixa o texto do cronograma de uma cadeira pelo browser do WMux (aba própria, fechada no fim).

.PARAMETER CursoUrl
  Página do curso no Moodle (course/view.php?id=...). Usada para achar o link do cronograma.
.PARAMETER CronogramaUrl
  Link direto do cronograma (ex.: sarc.pucrs.br/Default/Export.aspx?...). Se dado, pula a busca.
.PARAMETER Saida
  Arquivo onde gravar o texto (UTF-8 sem BOM).

Imprime JSON: {ok, url_final, caminho:[urls visitadas], saida, erro}
#>
param(
  [string]$CursoUrl,
  [string]$CronogramaUrl,
  [Parameter(Mandatory = $true)][string]$Saida
)

function Out-Result($obj) { $obj | ConvertTo-Json -Compress -Depth 5; exit 0 }

if (-not (Test-Path '\\.\pipe\wmux')) { Out-Result @{ ok = $false; erro = 'wmux_indisponivel' } }
if (-not $CursoUrl -and -not $CronogramaUrl) { Out-Result @{ ok = $false; erro = 'informe CursoUrl ou CronogramaUrl' } }

$pipeToken = (Get-Content "$env:APPDATA\wmux\pipe-token" -Raw).Trim()
$client = New-Object System.IO.Pipes.NamedPipeClientStream('.', 'wmux', [System.IO.Pipes.PipeDirection]::InOut)
$client.Connect(3000)
$writer = New-Object System.IO.StreamWriter($client); $writer.AutoFlush = $true
$reader = New-Object System.IO.StreamReader($client)
function Invoke-WMux($method, $params = @{}) {
  $writer.Write((ConvertTo-Json @{ method = $method; params = $params; token = $pipeToken } -Compress -Depth 10) + "`n")
  return ($reader.ReadLine() | ConvertFrom-Json)
}

$me = "puc-cronograma-$(Get-Random)"
$caminho = New-Object System.Collections.ArrayList
$t = (Invoke-WMux 'browser.target' @{ caller = $me; fresh = $true }).result

function Go($url) {
  [void]$caminho.Add($url)
  Invoke-WMux 'browser.navigate' @{ caller = $me; url = $url } | Out-Null
  Invoke-WMux 'browser.waitfor' @{ caller = $me; loadState = 'complete'; timeout = 20000 } | Out-Null
  Start-Sleep -Milliseconds 1500
  return (Invoke-WMux 'browser.eval' @{ caller = $me; js = 'location.href' }).result.result
}
function FindLink($regex, [switch]$External) {
  $filtro = if ($External) { "&& !/moodle\.pucrs\.br/.test(a.href)" } else { "" }
  # textContent do Moodle traz quebras de linha/nbsp entre as palavras: normalizar antes de testar
  $js = "(Array.from(document.querySelectorAll('#region-main a, a')).filter(a => /$regex/i.test(a.textContent.replace(/\s+/g,' ').trim()) && /^https?:/.test(a.href) $filtro).map(a => a.href)[0]) || ''"
  return (Invoke-WMux 'browser.eval' @{ caller = $me; js = $js }).result.result
}

try {
  $alvo = $CronogramaUrl
  if (-not $alvo) {
    $atual = Go $CursoUrl
    if ($atual -match 'login') { throw 'moodle_exige_login' }
    $alvo = FindLink 'cronograma'
    if (-not $alvo) {
      $plano = FindLink 'plano de ensino'
      if ($plano) { Go $plano | Out-Null; $alvo = FindLink 'cronograma' }
    }
    if (-not $alvo) { throw 'link_do_cronograma_nao_encontrado' }
    if ($alvo -match 'moodle\.pucrs\.br/mod/url/') {
      $atual = Go $alvo
      if ($atual -match 'moodle\.pucrs\.br') {
        # a página mod/url mostra o link de destino no conteúdo principal; o cabeçalho tem outros links externos
        $jsExt = "(() => { const ls = Array.from(document.querySelectorAll('#region-main a')).map(a => a.href).filter(h => /^https?:/.test(h) && !/moodle\.pucrs\.br/.test(h)); return ls.find(h => /sarc|export\.aspx|cronograma/i.test(h)) || ls[0] || ''; })()"
        $ext = (Invoke-WMux 'browser.eval' @{ caller = $me; js = $jsExt }).result.result
        if ($ext) { $alvo = $ext } else { $alvo = $atual }
      } else { $alvo = $atual }
    }
  }
  $final = Go $alvo
  $texto = (Invoke-WMux 'browser.get_text' @{ caller = $me }).result.text
  if (-not $texto) { throw 'texto_vazio' }
  $dir = Split-Path -Parent $Saida
  if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force $dir | Out-Null }
  [IO.File]::WriteAllText($Saida, $texto, (New-Object System.Text.UTF8Encoding $false))
  $res = @{ ok = $true; url_final = $final; caminho = $caminho; saida = $Saida }
} catch {
  $res = @{ ok = $false; erro = "$($_.Exception.Message)"; caminho = $caminho }
} finally {
  if ($t.created) { Invoke-WMux 'surface.close' @{ id = $t.surfaceId } | Out-Null }
  $client.Close()
}
Out-Result $res
