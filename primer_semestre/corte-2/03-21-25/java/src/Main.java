import java.util.Scanner;

public class Main {

    public static void main (String[] args){

        Scanner sr = new Scanner(System.in);
        System.out.print("El valor de la longitud : ");
        double longitud = sr.nextDouble();

        double area = 2 *Math.pow(3 , 0.5) * longitud * longitud;
        double volumen = (2.0 / 3) * Math.pow(longitud , 3);

        System.out.println("El area del hexagono es : " + area);
        System.out.println("El volumen del hexagono es : " + volumen);

        sr.close();

    }

}