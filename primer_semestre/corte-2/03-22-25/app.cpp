#include <iostream>

using namespace std;

int main()
{

  float n1, n2, n3;
  cout << "nota 1 : ";
  cin >> n1;
  cout << "nota 2 : ";
  cin >> n2;
  cout << "nota 3 : ";
  cin >> n3;
  float media = (n1 + n2 + n3) / 3;
  cout << "Media das notas: " << media << endl;
  if (media >= 3.5)
  {
    cout << "Aprovado" << endl;
  }
  else
  {
    cout << "Reprovado" << endl;
  }

  return 0;
}