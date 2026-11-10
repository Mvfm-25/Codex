#!/bin/bash
# testa.sh exec|erro arquivos.cmm...
#   exec: gera o .s, monta, liga, executa (com prog.entrada, se houver) e compara com prog.esperado
#   erro: compara as mensagens de erro do compilador com prog.esperado
modo=$1; shift
ok=0; falhas=0
for f in "$@"; do
    b="${f%.cmm}"
    if [ "$modo" = erro ]; then
        java Parser "$f" > /dev/null 2> "$b.saida"
        sed -i.bak '/^Picked up/d' "$b.saida" && rm -f "$b.saida.bak"
    else
        entrada=/dev/null; [ -f "$b.entrada" ] && entrada="$b.entrada"
        if java Parser "$f" > "$b.s" 2> "$b.saida" \
           && as --32 -o "$b.o" "$b.s" && ld -m elf_i386 -o "$b.exe" "$b.o"; then
            timeout 5 "./$b.exe" < "$entrada" > "$b.saida"
        fi
    fi
    if diff -q "$b.saida" "$b.esperado" > /dev/null 2>&1; then
        echo "  ok     $f"; ok=$((ok + 1))
    else
        echo "  FALHOU $f   (compare $b.saida com $b.esperado)"; falhas=$((falhas + 1))
    fi
done
echo "  -> $ok ok, $falhas falha(s)"
