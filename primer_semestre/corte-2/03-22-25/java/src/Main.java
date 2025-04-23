import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("nota 1 : ");
        double nota = sc.nextDouble();
        System.out.print("nota 2 : ");
        double nota2 = sc.nextDouble();
        System.out.print("nota 3 : ");
        double nota3 = sc.nextDouble();
        double media = (nota + nota2 + nota3) / 3;
        System.out.println("La media aritmética es: " + media);
        if (media >= 3.5) {
            System.out.println("Aprobado");
        } else {
            System.out.println("Reprobado");
        }

        System.out.print("ingrese el valor de b");
        
        System.out.println("ingrese el valor de h");
    }
}