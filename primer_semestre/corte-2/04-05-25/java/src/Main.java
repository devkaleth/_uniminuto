import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
    int x = 0;
    while(x <= 10){

        System.out.print("Ingrese su edad : ");

        int edad  = sc.nextInt();

        if(edad >= 18){
             System.out.println("eres mayor de edad");
        }
        else{
            System.out.println("eres menor de edad");
        }

        x ++ ;
    }
    sc.close();
	}
}