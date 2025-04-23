#include <iostream>
#include <cmath>
using namespace std;

int main()
{
  float L;
  int A = 2;
  double raiz = pow(3, 0.5);
  cout << "El valor de L : ";
  cin >> L;
  float area = A * raiz * pow(L, 2);
  float volumen = 2.0 / 3 * pow(L, 2);
  cout << "El area es: " << area << endl;
  cout << "El volumen es: " << volumen << endl;
  return 0;
}