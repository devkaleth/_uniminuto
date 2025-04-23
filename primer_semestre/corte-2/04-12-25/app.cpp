#include <iostream>

using namespace std;

int main()
{
  int n = 2;
  int i = 5;
  while (true)
  {
    int InputUser;
    cout << "Ingrese un numero: ";
    cin >> InputUser;
    if (InputUser == n)
    {
      cout << "ganastes :)" << endl;
    }
    else
    {
      cout << "perdiste :(" << endl;
      i--;
      cout << "Te quedan " << i << " intentos" << endl;
    }
  }

  return 0;
}