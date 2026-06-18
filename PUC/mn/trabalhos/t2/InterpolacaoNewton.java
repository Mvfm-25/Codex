/*
 * Métodos Numéricos - Trabalho III
 * Interpolação de Newton (diferenças divididas)
 *
 * Problema (EsAO / obuseiro L117 a 31 graus, carga média):
 * a partir de dados parciais da altura do projétil ao longo do tempo,
 * estimar:
 *   1) a altura máxima atingida pelo projétil;
 *   2) o instante (tempo após o disparo) em que essa altura ocorre.
 *
 * Estratégia:
 *   - construir o polinômio interpolador de Newton de grau 6 (7 pontos);
 *   - avaliá-lo com o esquema de Horner para a forma de Newton;
 *   - localizar o máximo: varredura fina no intervalo dos dados para
 *     encontrar a região do pico e, em seguida, refinamento por busca
 *     da seção áurea (golden section search) para obter alta precisão.
 */
public class InterpolacaoNewton {

    // Dados fornecidos pelos sensores: tempo (s) x altura (m)
    static final double[] T = {0.0, 3.0, 7.0, 10.0, 14.0, 29.0, 31.0};
    static final double[] H = {1.5, 1007.0, 2075.0, 2670.0, 3190.0, 2339.0, 1892.0};

    // Coeficientes da forma de Newton (diferenças divididas do "topo" da tabela)
    static double[] coef;

    public static void main(String[] args) {
        int n = T.length;
        coef = diferencasDivididas(T, H);

        System.out.println("=== Interpolacao de Newton ===");
        System.out.println("Pontos utilizados (tempo s, altura m):");
        for (int i = 0; i < n; i++) {
            System.out.printf("  h(%.0f) = %.4f%n", T[i], H[i]);
        }

        System.out.println("\nCoeficientes (diferencas divididas) do polinomio de Newton:");
        for (int i = 0; i < coef.length; i++) {
            System.out.printf("  c[%d] = %.10g%n", i, coef[i]);
        }

        // Verificacao: o polinomio deve reproduzir os pontos de entrada
        System.out.println("\nVerificacao (o polinomio passa pelos pontos dados):");
        for (int i = 0; i < n; i++) {
            System.out.printf("  P(%.0f) = %.4f  (dado: %.1f)%n", T[i], avaliar(T[i]), H[i]);
        }

        // Busca do maximo no intervalo coberto pelos dados
        double a = T[0];
        double b = T[n - 1];

        // 1) Varredura fina para localizar a regiao do pico
        double passo = 0.001;
        double tPico = a;
        double hPico = avaliar(a);
        for (double t = a; t <= b; t += passo) {
            double h = avaliar(t);
            if (h > hPico) {
                hPico = h;
                tPico = t;
            }
        }

        // 2) Refinamento por secao aurea em torno do pico encontrado
        double lo = Math.max(a, tPico - passo);
        double hi = Math.min(b, tPico + passo);
        double[] otimo = secaoAurea(lo, hi, 1e-12);
        double tMax = otimo[0];
        double hMax = otimo[1];

        System.out.println("\n=== Resultado ===");
        System.out.printf("Altura maxima estimada : %.4f m%n", hMax);
        System.out.printf("Instante do maximo     : %.4f s%n", tMax);
    }

    /**
     * Calcula os coeficientes da forma de Newton via tabela de diferencas
     * divididas. Retorna o vetor c[0..n-1] tal que:
     *   P(x) = c[0] + c[1](x-x0) + c[2](x-x0)(x-x1) + ...
     */
    static double[] diferencasDivididas(double[] x, double[] y) {
        int n = x.length;
        double[][] dd = new double[n][n];
        for (int i = 0; i < n; i++) {
            dd[i][0] = y[i];
        }
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < n - j; i++) {
                dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x[i + j] - x[i]);
            }
        }
        double[] c = new double[n];
        for (int j = 0; j < n; j++) {
            c[j] = dd[0][j];
        }
        return c;
    }

    /**
     * Avalia o polinomio de Newton em x usando o esquema de Horner aninhado:
     *   P(x) = c0 + (x-x0)(c1 + (x-x1)(c2 + ...))
     */
    static double avaliar(double x) {
        int n = coef.length;
        double resultado = coef[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            resultado = resultado * (x - T[i]) + coef[i];
        }
        return resultado;
    }

    /**
     * Busca da secao aurea para MAXIMIZAR a funcao em [a, b].
     * Retorna {x_otimo, valor_otimo}.
     */
    static double[] secaoAurea(double a, double b, double tol) {
        final double gr = (Math.sqrt(5.0) - 1.0) / 2.0; // ~0.618
        double c = b - gr * (b - a);
        double d = a + gr * (b - a);
        double fc = avaliar(c);
        double fd = avaliar(d);
        while ((b - a) > tol) {
            if (fc > fd) {       // maximo esta em [a, d]
                b = d;
                d = c;
                fd = fc;
                c = b - gr * (b - a);
                fc = avaliar(c);
            } else {             // maximo esta em [c, b]
                a = c;
                c = d;
                fc = fd;
                d = a + gr * (b - a);
                fd = avaliar(d);
            }
        }
        double x = (a + b) / 2.0;
        return new double[]{x, avaliar(x)};
    }
}
