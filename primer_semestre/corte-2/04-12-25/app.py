import os 
n = 8
i = 5
print('tines 5 intentos')
while (True) :
  x = int(input('ingrese un numero del uno al 10 : '))
  if (x != n ) :
    print('el numero no es correcto :(')
    i = i - 1
    if(n > x) :
      print('el numero es mayor')
    else :
      print('el numero es menor')
    print('te quedan', i, 'intentos')
  elif (x == n) :
    print('el numero es correcto :)')
    break
  if (i == 0) :
    print('perdistes ')
    print('el numero era :', n)
    break


for i in range(3, 100 , 3):
    print(i)