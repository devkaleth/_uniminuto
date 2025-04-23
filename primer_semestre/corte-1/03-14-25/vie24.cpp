#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  float a, b, h;
  float x;
  cout << "Entrada A :";
  cin >> a;
  cout << "Entrada B :";
  cin >> b;
  cout << "Entrada H :";
  cin >> h;
  x = ((pow(a, 2) * b) / 2) * h;
  cout << "resultado : " << x << endl;
  return 0;
}
