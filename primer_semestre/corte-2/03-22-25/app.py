n1 = float(input("digital 1 : "))
n2 = float(input("digital 2 : "))
n3 = float(input("digital 3 : "))
nota = (n1 + n2 + n3) / 3

if  nota >= 3.5 :
  print("aprobado")
else:
  print("reprobado")

b = float(input("valor de b : "))
h = float(input("valor h : "))

if b > 0 and h > 0:
  at = (b * h) / 2
  print("el area del triangulo es : ", at)

else :
  print("ingre un nuevo valor")


x = float(input("ingrese el valor de x :"))
a = float(input("ingrese del valor a :"))

m = a + x


if m > 0 and x > 0 :
  s = (a * 2)
  print(f"el valor de s es : {s}")
else :
  print(f"el valor de m es : {m}") 
print("fin del programming")