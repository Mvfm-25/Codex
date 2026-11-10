/**
 * Mini biblioteca de E/S em assembly x86 de 32 bits (Linux, int $0x80),
 * anexada ao final de todo programa gerado. Não usa nenhuma biblioteca externa.
 *
 * Convenção de uso pelo código gerado:
 *   __write     escreve o inteiro em %EAX
 *   __writeLit  escreve %EDX bytes a partir do endereço %ECX
 *   __writeln   escreve '\n'
 *   __read      lê uma linha da entrada padrão e devolve o inteiro em %EAX
 *
 * As rotinas alteram %EAX, %EBX, %ECX e %EDX, mas preservam %EBP e %ESP —
 * o código gerado mantém os valores intermediários na pilha, não em registradores.
 * Todos os rótulos internos começam com "__" para não colidir com os nomes
 * do programa-fonte (variáveis e funções recebem o prefixo "_").
 */
public final class BibliotecaIO {
    private BibliotecaIO() {}

    public static final String FIM_PROGRAMA = """
            #
            # devolve o controle para o SO
            #
            \tMOVL $0, %EBX
            \tMOVL $1, %EAX
            \tint $0x80
            """;

    public static final String ROTINAS = """
            #
            # Funcoes da biblioteca (IO)
            #
            __writeln:
            \tMOVL $__fim_msg, %ECX
            \tDECL %ECX
            \tMOVB $10, (%ECX)
            \tMOVL $1, %EDX
            \tJMP __writeLit
            __write:
            \tMOVL $__fim_msg, %ECX
            \tMOVL $0, %EBX
            \tCMPL $0, %EAX
            \tJGE __write3
            \tNEGL %EAX
            \tMOVL $1, %EBX
            __write3:
            \tPUSHL %EBX
            \tMOVL $10, %EBX
            __divide:
            \tMOVL $0, %EDX
            \tIDIVL %EBX
            \tDECL %ECX
            \tADD $48, %DL
            \tMOVB %DL, (%ECX)
            \tCMPL $0, %EAX
            \tJNE __divide
            \tPOPL %EBX
            \tCMPL $0, %EBX
            \tJE __print
            \tDECL %ECX
            \tMOVB $'-', (%ECX)
            __print:
            \tMOVL $__fim_msg, %EDX
            \tSUBL %ECX, %EDX
            __writeLit:
            \tMOVL $1, %EBX
            \tMOVL $4, %EAX
            \tint $0x80
            \tRET
            #
            # __read: le um byte por vez ate '\\n' ou fim de arquivo
            # (funciona tambem com a entrada redirecionada de um arquivo)
            #
            __read:
            \tMOVL $__msg, %ECX
            __read_byte:
            \tMOVL $1, %EDX
            \tMOVL $0, %EBX
            \tMOVL $3, %EAX
            \tint $0x80
            \tCMPL $0, %EAX
            \tJLE __read_fim
            \tCMPB $10, (%ECX)
            \tJE __read_fim
            \tINCL %ECX
            \tCMPL $__fim_msg - 1, %ECX
            \tJB __read_byte
            __read_fim:
            \tMOVB $10, (%ECX)
            \tMOVL $0, %EAX
            \tMOVL $0, %EBX
            \tMOVL $0, %EDX
            \tMOVL $__msg, %ECX
            \tCMPB $'-', (%ECX)
            \tJNE __reading
            \tINCL %ECX
            \tINC %BL
            __reading:
            \tMOVB (%ECX), %DL
            \tCMP $10, %DL
            \tJE __fimread
            \tSUB $48, %DL
            \tIMULL $10, %EAX
            \tADDL %EDX, %EAX
            \tINCL %ECX
            \tJMP __reading
            __fimread:
            \tCMPB $1, %BL
            \tJNE __fimread2
            \tNEGL %EAX
            __fimread2:
            \tRET
            """;

    public static final String BUFFERS = """
            #
            # buffers da biblioteca
            #
            __msg:
            \t.zero 30
            __fim_msg:
            \t.byte 0
            """;
}
