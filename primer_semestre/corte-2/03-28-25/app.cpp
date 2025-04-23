#include <iostream>
#include <cmath>

using namespace std;

int main()
{

  int a;

  int n1, n2;
  char op;

  cout << "dia : ";

  cin >> a;

  if (a == 1)
  {
    cout << "dia lunes";
  }
  else if (a == 2)
  {
    cout << "dia martes";
  }
  else if (a == 3)
  {
    cout << "dia miercoles";
  }
  else if (a == 4)
  {
    cout << "dia jueves";
  }
  else if (a == 5)
  {
    cout << "dia viernes";
  }
  else if (a == 6)
  {
    cout << "dia sabado";
  }
  else if (a == 7)
  {
    cout << "dia domingo";
  }
  else
  {
    cout << "numero no valido";
  }

  cout << "\nIngrese el primer numero: ";
  cin >> n1;
  cout << "\nIngrese el segundo numero: ";
  cin >> n2;
  cout << "\nIngrese el operador: ";
  cin >> op;

  if (op == '+')
  {
    cout << "\nResultado: " << n1 + n2;
  }
  else if (op == '-')
  {
    cout << "\nResultado: " << n1 - n2;
  }
  else if (op == '/')
  {
    cout << "\nResultado: " << n1 / n2;
  }
  else if (op == '*')
  {
    cout << "\nResultado: " << n1 * n2;
  }
  else if (op == '%')
  {
    cout << "\nResultado: " << n1 % n2;
  }
  else if (op == '^')
  {
    cout << "\nResultado: " << pow(n1, n2);
  }
  else if (op == 'x' | op == '*')
  {
    cout << "\nResultado: " << n1 * n2;
  }

  return 0;
}