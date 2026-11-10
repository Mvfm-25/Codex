import java.util.ArrayList;

/**
 * Tabela de símbolos com dois níveis: global e o da função em análise.
 * (Sem variáveis de bloco: os locais são declarados no início do corpo da função.)
 */
public class TabSimb {
    private final ArrayList<TS_entry> globais = new ArrayList<>();
    private ArrayList<TS_entry> locais = null;      // != null dentro de uma função

    public boolean dentroDeFuncao() { return locais != null; }

    public void abreEscopo()  { locais = new ArrayList<>(); }
    public void fechaEscopo() { locais = null; }

    /** Insere no escopo corrente (local, se dentro de função). */
    public void insert(TS_entry nodo) {
        (dentroDeFuncao() ? locais : globais).add(nodo);
    }

    public void insertGlobal(TS_entry nodo) { globais.add(nodo); }

    /** Procura só no escopo corrente — usado para detectar redeclaração. */
    public TS_entry pesquisaEscopoAtual(String id) {
        return busca(dentroDeFuncao() ? locais : globais, id);
    }

    /** Procura primeiro nos locais e depois nos globais (escopo estático). */
    public TS_entry pesquisa(String id) {
        TS_entry n = dentroDeFuncao() ? busca(locais, id) : null;
        return n != null ? n : busca(globais, id);
    }

    private static TS_entry busca(ArrayList<TS_entry> lista, String id) {
        for (TS_entry nodo : lista)
            if (nodo.getId().equals(id)) return nodo;
        return null;
    }

    /** Uma palavra (4 bytes) por variável global — int e bool. */
    public void geraGlobais(StringBuilder out) {
        for (TS_entry nodo : globais)
            if (nodo.getClasse() == ClasseID.VarGlobal)
                out.append("_").append(nodo.getId()).append(":\t.zero 4\n");
    }

    public void listar(String titulo, boolean locaisTambem) {
        System.err.println("# TS " + titulo + ":");
        if (locaisTambem && locais != null)
            for (TS_entry nodo : locais) System.err.println("#   " + nodo);
        else
            for (TS_entry nodo : globais) System.err.println("#   " + nodo);
    }
}
