class Program
{
  public static void Main(string[] args)
  {
    float a, b, h;
    Console.Write("Valor de A : ");
    a = Single.Parse(Console.ReadLine());
    Console.Write("Valor de B : ");
    b = Single.Parse(Console.ReadLine());
    Console.Write("Valor de H : ");
    h = Single.Parse(Console.ReadLine());
    float x = (((a * a) * b) / 2) * h;
    Console.WriteLine("El valor de x es : " + x);
    Console.WriteLine("================================================");
    float? pedroNota1, pedroNota2;
    float? paubloNota1, paubloNota2;
    float? betiNota1, betiNota2;
    float? banbanNota1, banbanNota2;
    Console.Write("Pedro Nota 1 : ");
    pedroNota1 = Single.Parse(Console.ReadLine());
    Console.Write("Pedro Nota 2 : ");
    pedroNota2 = Single.Parse(Console.ReadLine());
    Console.Write("paublo Nota 1 : ");
    paubloNota1 = Single.Parse(Console.ReadLine());
    Console.Write("paublo Nota 2 : ");
    paubloNota2 = Single.Parse(Console.ReadLine());
    Console.Write("beti Nota 1 : ");
    betiNota1 = Single.Parse(Console.ReadLine());
    Console.Write("beti Nota 2 :");
    betiNota2 = Single.Parse(Console.ReadLine());
    Console.Write("banban Nota 1 : ");
    banbanNota1 = Single.Parse(Console.ReadLine());
    Console.Write("banban Nota 2 : ");
    banbanNota2 = Single.Parse(Console.ReadLine());

    float promedioPedro = 0;
    float promedioPablo = 0;
    float promedioBeti = 0;
    float promedioBanban = 0;

    if (pedroNota1.HasValue && pedroNota2.HasValue)
    {
      promedioPedro = (pedroNota1.Value * 0.30f) + (pedroNota2.Value * 0.70f);
    }
    if (paubloNota1.HasValue && paubloNota2.HasValue)
    {
      promedioPablo = (paubloNota1.Value * 0.30f) + (paubloNota2.Value * 0.70f);
    }
    if (betiNota1.HasValue && betiNota2.HasValue)
    {
      promedioBeti = (betiNota1.Value * 0.30f) + (betiNota2.Value * 0.70f);
    }
    if (banbanNota1.HasValue && banbanNota2.HasValue)
    {
      promedioBanban = (banbanNota1.Value * 0.30f) + (banbanNota2.Value * 0.70f);
    }

    Console.WriteLine("Promedio de Pedro : " + promedioPedro);
    Console.WriteLine("Promedio de Pablo : " + promedioPablo);
    Console.WriteLine("Promedio de Beti : " + promedioBeti);
    Console.WriteLine("Promedio de Banban : " + promedioBanban);

    return 0;
  }
}