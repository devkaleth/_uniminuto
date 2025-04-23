

x = 1
for i in range(10) : 
  E=int(input("ingrese un numero: "))
  if E >= 18:
    print("es mayor de edad")
  else:
    print("es menor de edad")
  x += 1

while x <= 10 : 
  print("ya no se puede ingresar mas numeros")
  break