class Program
{
  static void Main(String[] args)
  {
    Console.Write("El valor de la longitud : ");
    double l = double.Parse(Console.ReadLine() ?? "0");
    double area = (2 * Math.Sqrt(3)) * Math.Pow(l, 2);
    double volumen = (2.0 / 3) * Math.Pow(l, 3);
    Console.WriteLine("El area de la esfera es : " + area);
    Console.WriteLine("El volumen de la esfera es : " + volumen);
  }
}