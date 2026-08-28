import java.util.*;

public class cotasEmJava{
    public static void main(String[] args){

        int coeficienteMaiorGrau = 6;
        int[] listaCoeficientes = {18, 34, 493, 1431};

        System.out.println("Por Cauchy : " + cauchy(coeficienteMaiorGrau, listaCoeficientes));
        System.out.println("Por Lagrange : " + lagrange(coeficienteMaiorGrau, listaCoeficientes));

    }

    public static int cauchy(int maiorGrau, int[] listaCoeficientes){

        // Fazendo a divisão proposta por Cauchy pelo jeito mais idiota que pude.
        ArrayList<Integer> listaResposta = new ArrayList<Integer>();
        for (int i : listaCoeficientes){
            listaResposta.add(i / maiorGrau);
        }

        return 1 + Collections.max(listaResposta);
    }

    public static int lagrange(int maiorGrau, int[] listaCoeficientes){
        
        int soma = 0;
        for (int i : listaCoeficientes){
            soma += i / maiorGrau;
        }

        return Math.max(1, soma);
    }

}
