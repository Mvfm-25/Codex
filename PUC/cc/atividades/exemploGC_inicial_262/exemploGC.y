// exemploGC.y — CÓDIGO INICIAL do gerador de código x86 (32 bits) para a
//               linguagem C--, em UMA passagem, usando a pilha do processador
//               como máquina de pilha.   Construção de Compiladores — PUCRS
//
// O que este código inicial JÁ FAZ:
//   - variáveis globais int e bool;
//   - expressões aritméticas, relacionais, lógicas, '!' , menos unário e  ?: ;
//   - comandos: atribuição (é um COMANDO, como em Pascal), if/else, while,
//     read, write e blocos { };
//   - análise semântica de funções: tabela de símbolos com parâmetros e
//     variáveis locais (deslocamentos já calculados), número de argumentos,
//     return com/sem valor.
//
// Organização:
//   gramática + ações curtas que chamam métodos      (este arquivo)
//   tabela de símbolos                               TS_entry, TabSimb, ClasseID
//   biblioteca de E/S em assembly                    BibliotecaIO
//
// Registro de ativação sugerido (cresce para endereços menores):
//      8+4*(n-1-i)(%EBP)  parâmetro i (0..n-1), empilhados da esquerda p/ direita
//      4(%EBP)            endereço de retorno (CALL)
//      0(%EBP)            %EBP do chamador
//     -4*k(%EBP)          variável local k (1..m)
// Valor de retorno em %EAX; o chamador remove os argumentos (ADDL $4n, %ESP).
// Os deslocamentos já são calculados na TS (TS_entry.getOperando()).

%{
  import java.io.*;
  import java.util.ArrayList;
  import java.util.HashSet;
  import java.util.Stack;
%}

%token ID, INT, FLOAT, BOOL, NUM, LIT, VOID, MAIN, READ, WRITE, RETURN
%token IF, ELSE, WHILE, TRUE, FALSE
%token EQ, LEQ, GEQ, NEQ, AND, OR

%nonassoc IFX
%nonassoc ELSE

%right '?' ':'
%left OR
%left AND
%left '>' '<' EQ LEQ GEQ NEQ
%left '+' '-'
%left '*' '/' '%'
%right '!' UMINUS

%type <sval> ID LIT NUM
%type <ival> type

%%

/* =========================== programa ============================ */

prog    : { geraInicio(); }  lDecl  mainF  { geraFimPrograma(); }
        ;

lDecl   : lDecl decl
        |
        ;

decl    : type ID ';'                      { declaraVar($2, $1); }
        | cabecalho lParamOpc ')'          { fixaDeslocParams(); }
          corpo                            { fechaFuncao(); }
        ;

type    : INT    { $$ = INT; }
        | BOOL   { $$ = BOOL; }
        | FLOAT  { yyerror("(sem) tipo float nao suportado pelo gerador"); $$ = INT; }
        ;

/* ============================ funções ============================ */

cabecalho : type ID '('                    { abreFuncao($2, $1); }
          | VOID ID '('                    { abreFuncao($2, VOID); }
          ;

lParamOpc : lParam
          |
          ;

lParam  : lParam ',' param
        | param
        ;

param   : type ID                          { declaraParam($2, $1); }
        ;

mainF   : VOID MAIN '(' ')'                { abreFuncao("main", VOID); }
          corpo                            { fechaFuncao(); }
        ;

        // variáveis locais só no início do corpo (não há variáveis de bloco)
corpo   : '{' lDeclLocal                   { geraPrologo(); }
          lcmd '}'                         { geraEpilogo(); }
        ;

lDeclLocal : lDeclLocal type ID ';'        { declaraVar($3, $2); }
           |
           ;

/* =========================== comandos ============================ */

lcmd    : lcmd cmd
        |
        ;

cmd     : '{' lcmd '}'
        | ';'

        | ID '=' exp ';'                   { gcAtribui($1); }       // atribuição: COMANDO

        | ID '('                           { iniciaChamada($1); }   // chamada como comando
          lArgOpc ')' ';'                  { gcChamada(true); }

        | WRITE '(' LIT ')' ';'            { gcWriteLit($3); gcWriteln(); }
        | WRITE '(' exp ')' ';'            { gcWriteExp(); gcWriteln(); }
        | WRITE '(' LIT ','                { gcWriteLit($3); }
                         exp ')' ';'       { gcWriteExp(); gcWriteln(); }
        | READ '(' ID ')' ';'              { gcRead($3); }

        | RETURN exp ';'                   { gcReturn(true); }
        | RETURN ';'                       { gcReturn(false); }

        | IF '(' exp ')'                   { pRot.push(novosRotulos(2));
                                             gcDesviaSeFalso(pRot.peek()); }
          cmd restoIf

        | WHILE                            { pRot.push(novosRotulos(2));
                                             geraRot(pRot.peek()); }       // início
          '(' exp ')'                      { gcDesviaSeFalso(pRot.peek() + 1); }  // saída
          cmd                              { gcJmp(pRot.peek());
                                             geraRot(pRot.pop() + 1); }
        ;

restoIf : ELSE                             { gcJmp(pRot.peek() + 1);
                                             geraRot(pRot.peek()); }
          cmd                              { geraRot(pRot.pop() + 1); }
        | %prec IFX                        { geraRot(pRot.pop()); }
        ;

/* ========================== expressões =========================== */

exp     : NUM                              { gera("PUSHL $%s", $1); }
        | TRUE                             { gera("PUSHL $1"); }
        | FALSE                            { gera("PUSHL $0"); }
        | ID                               { gcCarregaVar($1); }
        | ID '('                           { iniciaChamada($1); }
          lArgOpc ')'                      { gcChamada(false); }
        | '(' exp ')'
        | '!' exp                          { gcExpNot(); }
        | '-' exp  %prec UMINUS            { gcExpNeg(); }

        | exp '+' exp                      { gcExpArit('+'); }
        | exp '-' exp                      { gcExpArit('-'); }
        | exp '*' exp                      { gcExpArit('*'); }
        | exp '/' exp                      { gcExpArit('/'); }
        | exp '%' exp                      { gcExpArit('%'); }

        | exp '>' exp                      { gcExpRel('>'); }
        | exp '<' exp                      { gcExpRel('<'); }
        | exp EQ  exp                      { gcExpRel(EQ); }
        | exp LEQ exp                      { gcExpRel(LEQ); }
        | exp GEQ exp                      { gcExpRel(GEQ); }
        | exp NEQ exp                      { gcExpRel(NEQ); }

        | exp OR  exp                      { gcExpLog(OR); }
        | exp AND exp                      { gcExpLog(AND); }

        | exp '?'                          { pRot.push(novosRotulos(2));
                                             gcDesviaSeFalso(pRot.peek()); }
          exp                              { gcJmp(pRot.peek() + 1);
                                             geraRot(pRot.peek()); }
          ':' exp                          { geraRot(pRot.pop() + 1); }
        ;

lArgOpc : lArg
        |
        ;

lArg    : lArg ',' exp                     { pArgs.push(pArgs.pop() + 1); }
        | exp                              { pArgs.push(pArgs.pop() + 1); }
        ;

%%

  /* ================================================================ *
   *  1. Infraestrutura: analisador léxico, erros, saída               *
   * ================================================================ */

  private Yylex lexer;
  private int nErros = 0;
  private final StringBuilder codigo = new StringBuilder();   // .text
  private final ArrayList<String> strTab = new ArrayList<>(); // literais

  private int yylex() {
    int yyl_return = -1;
    try {
      yylval = new ParserVal(0);
      yyl_return = lexer.yylex();
    }
    catch (IOException e) {
      System.err.println("IO error :" + e);
    }
    return yyl_return;
  }

  public void yyerror(String error) {
    if (error.startsWith("stack underflow")) return;   // fim da recuperação do byacc/j
    nErros++;
    if (error.equals("syntax error"))                    // mensagem do analisador sintático
      error = "erro sintatico proximo de '" + lexer.yytext() + "'";
    System.err.println("Erro: " + error + "  linha: " + lexer.getLine());
  }

  public Parser(Reader r) { lexer = new Yylex(r, this); }

  public void setDebug(boolean debug) { yydebug = debug; }

  public void listarTS() { ts.listar("global", false); }

  public static void main(String args[]) throws IOException {
    if (args.length == 0) {
      System.out.println("\n\tFormato: java Parser entrada.cmm > entrada.s\n");
      return;
    }
    Parser yyparser = new Parser(new FileReader(args[0]));
    yyparser.yyparse();
    if (yyparser.nErros > 0) {
      System.err.println(yyparser.nErros + " erro(s) - codigo nao gerado.");
      System.exit(1);
    }
    System.out.print(yyparser.codigo);
  }

  /** Emite uma instrução (formato printf; use %% para o '%' dos registradores). */
  void gera(String fmt, Object... args) {
    codigo.append('\t').append(String.format(fmt, args)).append('\n');
  }
  void geraLinha(String s)  { codigo.append(s).append('\n'); }
  void geraRot(int r)       { geraLinha(rot(r) + ":"); }
  void gcJmp(int r)         { gera("JMP %s", rot(r)); }

  /**
   * Construção que o código inicial reconhece e verifica, mas para a qual
   * a geração de código ainda não foi escrita. Conta como erro (o .s não é
   * gerado) e cada assunto é informado uma única vez.
   */
  private final HashSet<String> jaAvisado = new HashSet<>();
  void naoImplementado(String oque) {
    if (jaAvisado.add(oque)) {
      nErros++;
      System.err.println("Erro: geracao de codigo nao implementada: " + oque
                         + "  linha: " + lexer.getLine());
    }
  }

  /* ================================================================ *
   *  2. Tabela de símbolos e verificações semânticas                  *
   * ================================================================ */

  private final TabSimb ts = new TabSimb();
  private TS_entry funcaoAtual = null;

  /** Variável global (fora de função) ou local (dentro do corpo). */
  void declaraVar(String id, int tipo) {
    if (ts.pesquisaEscopoAtual(id) != null) {
      yyerror("(sem) identificador >" + id + "< jah declarado");
      return;
    }
    if (!ts.dentroDeFuncao()) {
      ts.insert(new TS_entry(id, tipo, ClasseID.VarGlobal));
    } else {
      TS_entry nodo = new TS_entry(id, tipo, ClasseID.VarLocal);
      nodo.setDesloc(-4 * funcaoAtual.novoLocal());
      ts.insert(nodo);
    }
  }

  void abreFuncao(String id, int tipoRet) {
    TS_entry f = ts.pesquisa(id);
    if (f != null) yyerror("(sem) identificador >" + id + "< jah declarado");
    funcaoAtual = new TS_entry(id, tipoRet, ClasseID.NomeFuncao);
    ts.insertGlobal(funcaoAtual);       // visível no próprio corpo: recursão
    ts.abreEscopo();
  }

  void declaraParam(String id, int tipo) {
    if (ts.pesquisaEscopoAtual(id) != null) {
      yyerror("(sem) parametro >" + id + "< repetido");
      return;
    }
    TS_entry p = new TS_entry(id, tipo, ClasseID.NomeParam);
    funcaoAtual.getParams().add(p);
    ts.insert(p);
  }

  /** Só ao ver ')' sabemos n: o último parâmetro fica em 8(%EBP). */
  void fixaDeslocParams() {
    var ps = funcaoAtual.getParams();
    int n = ps.size();
    for (int i = 0; i < n; i++)
      ps.get(i).setDesloc(8 + 4 * (n - 1 - i));
  }

  void fechaFuncao() {
    if (yydebug) ts.listar("local de " + funcaoAtual.getId(), true);
    ts.fechaEscopo();
    funcaoAtual = null;
  }

  /** Busca uma variável e reporta os erros semânticos de uso. */
  TS_entry buscaVar(String id) {
    TS_entry nodo = ts.pesquisa(id);
    if (nodo == null)
      yyerror("(sem) variavel >" + id + "< nao declarada");
    else if (!nodo.isVariavel()) {
      yyerror("(sem) >" + id + "< eh funcao, nao variavel");
      return null;
    }
    return nodo;
  }

  /**
   * Variável com código já implementado? Nesta versão inicial, só globais.
   * TODO: parâmetros e locais — o operando já está pronto em
   * v.getOperando() (ex.: "8(%EBP)", "-4(%EBP)"); basta remover esta restrição
   * depois de implementar o prólogo e o epílogo das funções.
   */
  boolean acessoImplementado(TS_entry v) {
    if (v.getClasse() == ClasseID.VarGlobal) return true;
    naoImplementado("acesso a parametros e variaveis locais");
    return false;
  }

  /* ================================================================ *
   *  3. Geração: expressões                                           *
   * ================================================================ */

  void gcCarregaVar(String id) {
    TS_entry v = buscaVar(id);
    if (v != null && acessoImplementado(v)) gera("PUSHL %s", v.getOperando());
  }

  void gcExpArit(int oparit) {
    gera("POPL %%EBX");
    gera("POPL %%EAX");
    switch (oparit) {
      case '+' -> gera("ADDL %%EBX, %%EAX");
      case '-' -> gera("SUBL %%EBX, %%EAX");
      case '*' -> gera("IMULL %%EBX, %%EAX");
      case '/' -> { gera("CLTD"); gera("IDIVL %%EBX"); }
      case '%' -> { gera("CLTD"); gera("IDIVL %%EBX"); gera("MOVL %%EDX, %%EAX"); }
    }
    gera("PUSHL %%EAX");
  }

  void gcExpRel(int oprel) {
    gera("POPL %%EAX");
    gera("POPL %%EDX");
    gera("CMPL %%EAX, %%EDX");
    gera("MOVL $0, %%EAX");
    switch (oprel) {
      case '<'        -> gera("SETL  %%AL");
      case '>'        -> gera("SETG  %%AL");
      case Parser.EQ  -> gera("SETE  %%AL");
      case Parser.GEQ -> gera("SETGE %%AL");
      case Parser.LEQ -> gera("SETLE %%AL");
      case Parser.NEQ -> gera("SETNE %%AL");
    }
    gera("PUSHL %%EAX");
  }

  void gcExpLog(int oplog) {
    gera("POPL %%EDX");
    gera("POPL %%EAX");
    gera("CMPL $0, %%EAX");
    gera("MOVL $0, %%EAX");
    gera("SETNE %%AL");
    gera("CMPL $0, %%EDX");
    gera("MOVL $0, %%EDX");
    gera("SETNE %%DL");
    gera(oplog == Parser.OR ? "ORL %%EDX, %%EAX" : "ANDL %%EDX, %%EAX");
    gera("PUSHL %%EAX");
  }

  void gcExpNot() {                            // 0 -> 1, qualquer outro -> 0
    gera("POPL %%EAX");
    gera("CMPL $0, %%EAX");
    gera("MOVL $0, %%EAX");
    gera("SETE %%AL");
    gera("PUSHL %%EAX");
  }

  void gcExpNeg() {
    gera("NEGL (%%ESP)");
  }

  /* ================================================================ *
   *  4. Geração: comandos e controle de fluxo                         *
   * ================================================================ */

  private int proxRot = 1;
  private final Stack<Integer> pRot = new Stack<>();   // if, while e ?: (2 rótulos cada)

  String rot(int r) { return String.format("rot_%02d", r); }

  int novosRotulos(int n) { int r = proxRot; proxRot += n; return r; }

  void gcDesviaSeFalso(int r) {
    gera("POPL %%EAX");
    gera("CMPL $0, %%EAX");
    gera("JE %s", rot(r));
  }

  /** id = exp ;  — comando: o valor é desempilhado e armazenado. */
  void gcAtribui(String id) {
    TS_entry v = buscaVar(id);
    if (v == null || !acessoImplementado(v)) return;
    gera("POPL %%EDX");
    gera("MOVL %%EDX, %s", v.getOperando());
  }

  void gcWriteLit(String s) {
    strTab.add(s);
    int n = strTab.size() - 1;
    gera("MOVL $_str_%dLen, %%EDX", n);
    gera("MOVL $_str_%d, %%ECX", n);
    gera("CALL __writeLit");
  }

  void gcWriteExp() {
    gera("POPL %%EAX");
    gera("CALL __write");
  }

  void gcWriteln() { gera("CALL __writeln"); }

  /** read(id): empilha o ENDEREÇO da variável, lê e armazena. */
  void gcRead(String id) {
    TS_entry v = buscaVar(id);
    if (v == null || !acessoImplementado(v)) return;
    // TODO: para locais/parâmetros use  LEAL d(%EBP), %EAX ; PUSHL %EAX
    gera("PUSHL $%s", v.getOperando());
    gera("CALL __read");
    gera("POPL %%EDX");
    gera("MOVL %%EAX, (%%EDX)");
  }

  /* ================================================================ *
   *  5. Funções e chamadas: TODO                                     *
   * ================================================================ */

  private final Stack<TS_entry> pChamadas = new Stack<>();   // chamadas aninhadas
  private final Stack<Integer>  pArgs     = new Stack<>();   // nº de args de cada uma

  /** Entrada da função. Só a main (_start) é gerada nesta versão. */
  void geraPrologo() {
    TS_entry f = funcaoAtual;
    geraLinha("");
    geraLinha("#");
    geraLinha("# " + f.getTipoStr() + " " + f.getId() + "(" + f.getParams().size()
              + " param, " + f.getNumLocais() + " locais)");
    geraLinha("#");
    geraLinha(f.getRotulo() + ":");
    if (!f.getId().equals("main")) {
      // TODO: PUSHL %EBP ; MOVL %ESP, %EBP ; SUBL $4*nLocais, %ESP
      naoImplementado("funcoes (prologo, epilogo, chamada e retorno)");
    }
    if (f.getNumLocais() > 0) {
      // TODO: reservar espaço para as variáveis locais (também na main)
      naoImplementado("acesso a parametros e variaveis locais");
    }
  }

  /** Saída única da função: todo return desvia para _fim_<nome>. */
  void geraEpilogo() {
    TS_entry f = funcaoAtual;
    geraLinha(f.getRotuloFim() + ":");
    if (f.getId().equals("main")) {
      codigo.append(BibliotecaIO.FIM_PROGRAMA);
    }
    // TODO: nas demais funções: MOVL %EBP, %ESP ; POPL %EBP ; RET
  }

  void gcReturn(boolean comValor) {
    if (funcaoAtual == null) return;
    boolean isVoid = funcaoAtual.getTipo() == VOID;
    if (comValor && isVoid)
      yyerror("(sem) funcao void >" + funcaoAtual.getId() + "< nao pode retornar valor");
    if (!comValor && !isVoid)
      yyerror("(sem) funcao >" + funcaoAtual.getId() + "< deve retornar um valor");
    if (funcaoAtual.getId().equals("main")) {        // return; na main encerra o programa
      if (comValor) gera("POPL %%EAX");
      gera("JMP %s", funcaoAtual.getRotuloFim());
      return;
    }
    // TODO: POPL %EAX (se houver valor) ; JMP _fim_<funcao>
    naoImplementado("funcoes (prologo, epilogo, chamada e retorno)");
  }

  void iniciaChamada(String id) {
    TS_entry f = ts.pesquisa(id);
    if (f == null)
      yyerror("(sem) funcao >" + id + "< nao declarada");
    else if (!f.isFuncao()) {
      yyerror("(sem) >" + id + "< nao eh funcao");
      f = null;
    }
    pChamadas.push(f);
    pArgs.push(0);
  }

  /**
   * Fim da chamada: os argumentos já foram empilhados (esq. -> dir.).
   * comoComando = true em "f(x);" (o valor devolvido é descartado).
   */
  void gcChamada(boolean comoComando) {
    TS_entry f = pChamadas.pop();
    int n = pArgs.pop();
    if (f == null) return;
    if (n != f.getParams().size())
      yyerror("(sem) funcao >" + f.getId() + "< espera " + f.getParams().size()
              + " argumento(s), recebeu " + n);
    if (!comoComando && f.getTipo() == VOID)
      yyerror("(sem) funcao void >" + f.getId() + "< usada em expressao");
    // TODO: CALL _f ; ADDL $4n, %ESP ; e, em expressão, PUSHL %EAX
    naoImplementado("funcoes (prologo, epilogo, chamada e retorno)");
  }

  /* ================================================================ *
   *  6. Início e fim do arquivo .s                                    *
   * ================================================================ */

  void geraInicio() {
    geraLinha(".text");
    geraLinha("");
    geraLinha("#\t nome COMPLETO e matricula dos componentes do grupo...");
    geraLinha("#");
    geraLinha("");
    geraLinha(".GLOBL _start");
  }

  void geraFimPrograma() {
    codigo.append("\n").append(BibliotecaIO.ROTINAS);
    geraLinha("");
    geraLinha("#");
    geraLinha("# area de dados");
    geraLinha("#");
    geraLinha(".data");
    geraLinha("#");
    geraLinha("# variaveis globais");
    geraLinha("#");
    ts.geraGlobais(codigo);
    geraLinha("");
    codigo.append(BibliotecaIO.BUFFERS);
    geraLinha("");
    geraLinha("#");
    geraLinha("# area de literais");
    geraLinha("#");
    for (int i = 0; i < strTab.size(); i++) {
      geraLinha("_str_" + i + ":");
      geraLinha("\t.ascii \"" + strTab.get(i) + "\"");
      geraLinha("_str_" + i + "Len = . - _str_" + i);
    }
  }
