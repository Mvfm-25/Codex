// T2 de POA
// [mvfm][06-06-2026]

public class salao {

    static int n, b, c;
    static int[][] tab;   // 0 = vazio, 1 = Bigode (b), 2 = Capeta (c)
    static long total;

    static final int[][] DIRS = {
        {0, 1}, {0, -1}, {1, 0}, {-1, 0},
        {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
    };

    public static void main(String[] args) {
        if (args.length < 3) {
            System.err.println("Uso: java salao n b c");
            return;
        }
        n = Integer.parseInt(args[0]);
        b = Integer.parseInt(args[1]);
        c = Integer.parseInt(args[2]);

        if (b + c > n * n) { System.out.println(0); return; }

        tab = new int[n][n];
        posicionar(0, b, c);

        System.out.println(total);
    }

    static void posicionar(int pos, int restamB, int restamC) {
        if (restamB == 0 && restamC == 0) {
            if (configValida()) total++;
            return;
        }
        if (n * n - pos < restamB + restamC) return;   // nao cabe mais

        int linha = pos / n, coluna = pos % n;

        // casa vazia
        posicionar(pos + 1, restamB, restamC);

        // coloca um Bigode
        if (restamB > 0) {
            tab[linha][coluna] = 1;
            posicionar(pos + 1, restamB - 1, restamC);
            tab[linha][coluna] = 0;
        }

        // coloca um Capeta
        if (restamC > 0) {
            tab[linha][coluna] = 2;
            posicionar(pos + 1, restamB, restamC - 1);
            tab[linha][coluna] = 0;
        }
    }

    static boolean configValida() {
        for (int linha = 0; linha < n; linha++) {
            for (int coluna = 0; coluna < n; coluna++) {
                int quadrilha = tab[linha][coluna];
                if (quadrilha == 0) continue;

                int mesma = 0, outra = 0;
                for (int[] d : DIRS) {
                    int r = linha + d[0], cc = coluna + d[1];
                    while (r >= 0 && r < n && cc >= 0 && cc < n) {
                        int v = tab[r][cc];
                        if (v != 0) {
                            if (v == quadrilha) mesma++; else outra++;
                            break;   // bloqueado pela primeira peca da direcao
                        }
                        r += d[0]; cc += d[1];
                    }
                }
                if (mesma != 0 || outra < 2) return false;
            }
        }
        return true;
    }
}
