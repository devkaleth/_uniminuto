x = 0
while x <= 10 :
  edad = int(input('ingrese su edad : '))
  if edad < 18:
    print('eres mayor de edad')
  else :
    print('eres menor de edad')

  x += 1
  print('fin del ciclo')