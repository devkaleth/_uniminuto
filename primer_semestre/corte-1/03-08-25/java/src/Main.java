import java.util.Scanner; // Importar la clase Scanner

public class Main {
    public static void main(String[] args) {
        System.out.print("El valor de A :");
        Scanner sc = new Scanner(System.in);
        double a  =  sc.nextDouble();
        System.out.print("El valor de B :");
        double b = sc.nextDouble();
        double x = (a * b ) + 2;
        double z = b + 2;

        System.out.println(String.format("El resultado de x es : %s" , x));
        System.out.println(String.format("El resultado de z es : %s" , z));
    }
}