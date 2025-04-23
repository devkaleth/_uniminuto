class Program {
  public static void Main (String[] args) {
    int? A;
    int? B;
    Console.Write("El valor de A : ");
    A = int.Parse(Console.ReadLine());
    Console.Write("El valor de B : ");
    B = int.Parse(Console.ReadLine());
    int x = (int)((A * B ) + 2);
    int z = B + 2 ;
    Console.WriteLine("Result x : " , x);
    Console.WriteLine("Result z : " , z);
  }
}