# Gerador de código x86 (32 bits) — BYACC/J + JFlex  (código inicial 2026/2)
# only works with the Java extension of yacc: byacc/j

JFLEX  = java -jar JFlex.jar
#BYACCJ = ./yacc.linux -tv -J
BYACCJ = byaccj -tv -J
JAVAC  = javac

SRCJ = ClasseID.java TS_entry.java TabSimb.java BibliotecaIO.java

all: Parser.class

build: clean Parser.class

clean:
	rm -f *~ *.class *.o *.s *.exe Yylex.java Parser.java ParserVal.java y.output
	rm -f exemplos/*/*.s exemplos/*/*.o exemplos/*/*.exe exemplos/*/*.saida

Parser.class: $(SRCJ) Yylex.java Parser.java
	$(JAVAC) Parser.java $(SRCJ)

Yylex.java: exemploGC.flex
	$(JFLEX) exemploGC.flex

Parser.java: exemploGC.y
	$(BYACCJ) exemploGC.y

# ---------------------------------------------------------------------------
# Testes (montar e executar exige Linux x86 ou x86-64: as --32, ld -m elf_i386)
#   make teste          exemplos/ok      : compila, executa e compara com .esperado
#   make teste-erros    exemplos/erros   : mensagens de erro iguais ao .esperado
#   make teste-funcoes  exemplos/funcoes : OBJETIVO dos alunos (hoje: "nao implementada")
#   make testes         os três
# Se existir prog.entrada, ela é usada como entrada padrão do programa.
# ---------------------------------------------------------------------------
testes: teste teste-erros teste-funcoes

teste: Parser.class
	@./testa.sh exec exemplos/ok/*.cmm

teste-erros: Parser.class
	@./testa.sh erro exemplos/erros/*.cmm

teste-funcoes: Parser.class
	@./testa.sh exec exemplos/funcoes/*.cmm
