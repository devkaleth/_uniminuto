class Program
{
  static void Main(string[] args)
  {
    int x = 1;
    while (x <= 10)
    {
      int edad;
      Console.Write("Cual es tu edad : ");
      string input = Console.ReadLine();
      bool StringIsNumber = int.TryParse(input, out edad);
      if (StringIsNumber)
      {
        Console.WriteLine("Tu edad es : " + edad);
        if (edad >= 18)
        {
          Console.WriteLine("Eres mayor de edad");
        }
        else
        {
          Console.WriteLine("Eres menor de edad");
        }
      }
      else
      {
        Console.WriteLine("No es un numero");
        break;
      }
      x++;
    }
  }
}
