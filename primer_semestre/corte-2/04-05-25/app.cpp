#include <iostream>

using namespace std;

int main()
{

  for (int i = 0; i <= 10; i++)
  {
    cout << i << endl;
  }

  int x = 0;
  while (x <= 10)
  {
    int edad;
    cout << "Ingrese su edad: ";
    cin >> edad;
    if (edad >= 18)
    {
      cout << "mayor de edad \n";
    }
    else
    {
      cout << "menor de edad \n";
    }
    x++;
  }

  return 0;
}