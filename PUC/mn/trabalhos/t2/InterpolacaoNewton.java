public class InterpolacaoNewton {

    static final double[] T = {0.0, 3.0, 7.0, 10.0, 14.0, 29.0, 31.0};
    static final double[] H = {1.5, 1007.0, 2075.0, 2670.0, 3190.0, 2339.0, 1892.0};

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

        System.out.println("\nVerificacao (o polinomio passa pelos pontos dados):");
        for (int i = 0; i < n; i++) {
            System.out.printf("  P(%.0f) = %.4f  (dado: %.1f)%n", T[i], avaliar(T[i]), H[i]);
        }

        double a = T[0];
        double b = T[n - 1];

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

        double lo = Math.max(a, tPico - passo);
        double hi = Math.min(b, tPico + passo);
        double[] otimo = secaoAurea(lo, hi, 1e-12);
        double tMax = otimo[0];
        double hMax = otimo[1];

        System.out.println("\n=== Resultado ===");
        System.out.printf("Altura maxima estimada : %.4f m%n", hMax);
        System.out.printf("Instante do maximo     : %.4f s%n", tMax);
    }

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

    static double avaliar(double x) {
        int n = coef.length;
        double resultado = coef[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            resultado = resultado * (x - T[i]) + coef[i];
        }
        return resultado;
    }

    static double[] secaoAurea(double a, double b, double tol) {
        final double gr = (Math.sqrt(5.0) - 1.0) / 2.0;
        double c = b - gr * (b - a);
        double d = a + gr * (b - a);
        double fc = avaliar(c);
        double fd = avaliar(d);
        while ((b - a) > tol) {
            if (fc > fd) {
                b = d;
                d = c;
                fd = fc;
                c = b - gr * (b - a);
                fc = avaliar(c);
            } else {
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
