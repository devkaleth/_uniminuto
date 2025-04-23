

a = int(input('dia : '))
 if a == 1:
   print('Lunes')
  if a == 2:
    print('Martes')
  if a == 3:
   print('Miercoles')
 if a == 4:
   print('Jueves')
  if a == 5:
    print('viernes')
  if a == 6:
   print('Sabado')
 if a == 7:
   print('Domingo')

 match a : 
   case 1:
     print('Lunes')
   case 2:
     print('Martes')
   case 3 : 
     print('Miercoles')
   case 4 : 
     print('Jueves')
   case 5 :
     print('Viernes')
   case 6 :
     print('Sabado')
   case 7 :
     print('Domingo')
  
 a = int(input('numero 1 : '))
 b = int(input('numero 2 : '))
 c = input('Operacion : ')

 if(c == '+') :
   print(a + b)
 elif(c == '-'):
   print(a - b)

 elif(c == '*' or c == 'x') :
   print(a * b)
 elif(c == '/') :
   print(a / b)
 else:
   print('Operador no valido')
 figura = int(input('figura : '))
 if (fingura == 1) : 
   base = int(input('base : '))
   altura = int(input('altura : '))
   area = (base * altura) / 2
   print('area : ', area)

elif (figura == 2) :
  base = int(input('base : '))
  altura = int(input('altura : '))
  area = base * altura
  print('area : ', area)
elif (figura == 3) :
  b = int(input('ingrese b : '))
  d = int(input('ingrese d : ')) 
  result = (b * dia) / 2
  print('area : ' , result)


