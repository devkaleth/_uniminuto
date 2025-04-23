# calcular la edad de tres estudiantes y imprimirla


c = 1

while (c <= 3):
  nacimiento = input("año de nacimiento : ")
  actual = input("actual : ")

  edad = int(actual) - int(nacimiento)

  print("estudiante ", c, " : ", edad)
  c += 1

# calcular la nota definitiva de 4 estudiantes teniendo en cuenta que durante el semestre sacaron tres nota
# si la nota octenidad es mayor o igual a 3 que salga un mensaje que diga aprobo si no que salga un mensaje que diga aprobo

x = 0

while x <= 2:
  n1 = float(input('n1 : '))
  n2 = float(input('n2 : '))
  n3 = float(input('n3 : '))
  res = (n1 + n2 + n3) / 3
  if res >= 3.0 :
    print('aprobado')
  else : 
    print('reprobado')
  x = x + 1



