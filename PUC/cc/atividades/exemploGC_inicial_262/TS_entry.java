import java.util.ArrayList;
import java.util.List;

/**
 * Entrada da tabela de símbolos.
 *
 *  - variáveis e parâmetros: tipo, classe e deslocamento em relação a %EBP
 *  - funções: tipo de retorno, lista de parâmetros e número de variáveis locais
 */
public class TS_entry {
    private final String id;
    private final int tipo;          // Parser.INT, Parser.BOOL, Parser.VOID (funções)
    private final ClasseID classe;
    private int desloc;              // VarLocal / NomeParam: deslocamento em bytes (EBP)

    // somente para NomeFuncao
    private final List<TS_entry> params = new ArrayList<>();
    private int nLocais = 0;

    public TS_entry(String id, int tipo, ClasseID classe) {
        this.id = id;
        this.tipo = tipo;
        this.classe = classe;
    }

    public String getId()        { return id; }
    public int getTipo()         { return tipo; }
    public ClasseID getClasse()  { return classe; }
    public int getDesloc()       { return desloc; }
    public void setDesloc(int d) { desloc = d; }

    public List<TS_entry> getParams() { return params; }
    public int getNumLocais()         { return nLocais; }
    public int novoLocal()            { return ++nLocais; }

    public boolean isFuncao()   { return classe == ClasseID.NomeFuncao; }
    public boolean isVariavel() { return classe != ClasseID.NomeFuncao; }

    /** Operando de memória (sintaxe AT&T) que contém o valor da variável. */
    public String getOperando() {
        return classe == ClasseID.VarGlobal ? "_" + id : desloc + "(%EBP)";
    }

    /** Rótulo de código de uma função (a main é o ponto de entrada _start). */
    public String getRotulo()    { return id.equals("main") ? "_start" : "_" + id; }
    public String getRotuloFim() { return "_fim_" + id; }

    public String getTipoStr() {
        if (tipo == Parser.INT)  return "int";
        if (tipo == Parser.BOOL) return "bool";
        if (tipo == Parser.VOID) return "void";
        return "?";
    }

    @Override
    public String toString() {
        String s = String.format("%-10s %-5s %-10s", id, getTipoStr(), classe);
        if (isFuncao())
            return s + " params=" + params.size() + " locais=" + nLocais;
        return classe == ClasseID.VarGlobal ? s + " _" + id : s + " " + getOperando();
    }
}
