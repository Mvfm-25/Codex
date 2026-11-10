#!/bin/bash
# uso: ./run.x programa.cmm    (gera programa.s, monta, liga e executa)
set -e
ARQ="${1%.cmm}"

java Parser "$ARQ.cmm" > "$ARQ.s"

# montador e ligador em 32 bits (também em máquinas de 64 bits)
as --32 -o "$ARQ.o" "$ARQ.s"
ld -m elf_i386 -s -o "$ARQ.exe" "$ARQ.o"

"./$ARQ.exe"
