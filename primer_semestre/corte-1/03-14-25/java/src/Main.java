import java.util.Scanner;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Entrada A : ");
        double a = sc.nextDouble();
        System.out.print("Entrada B : ");
        double b = sc.nextDouble();
        System.out.print("Entrada H : ");
        double h = sc.nextDouble();
        double x = (((a*a)*b)/2)*h;
        System.out.println("Salida : " + x);
        System.out.println("================================================================");
        System.out.print("pedro nota 1 : ");
        float pedroNota1 =  sc.nextFloat();
        System.out.print("pedro nota 2 : ");
        float pedroNota2 =  sc.nextFloat();
        System.out.print("paublo nota 1 : ");
        float paubloNota1 =  sc.nextFloat();
        System.out.print("paublo nota 2 : ");
        float paubloNota2 = sc.nextFloat();
        System.out.print("beti nota 1 : ");
        float betiNota1 = sc.nextFloat();
        System.out.print("beti nota 2 : ");
        float betiNota2 = sc.nextFloat();
        System.out.print("banban nota 1 : ");
        float banbanNota1 = sc.nextFloat();
        System.out.print("banban nota 2 : ");
        float banbanNota2 = sc.nextFloat();
        double notaPedro = (pedroNota1 * 0.30) + (pedroNota2 * 0.70);
        double notaPaublo = (paubloNota1 * 0.30) + (paubloNota2 * 0.70);
        double notaBeti = (betiNota1 * 0.30) + (betiNota2 * 0.70);
        double notaBanban = (banbanNota1 * 0.30) + (banbanNota2 * 0.70);
        System.out.println(String.format("Nota definitiva de pedro : %f", notaPedro));
        System.out.println(String.format("Nota definitiva de paublo : %f", notaPaublo));
        System.out.println(String.format("Nota definitiva de beti : %f", notaBeti));
        System.out.println(String.format("Nota definitiva de banban : %f", notaBanban));


    }
}