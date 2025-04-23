a = float(input("Entrada A : "))
b = float(input("Entrada B : "))
h = float(input("Entrada H : "))
x = (((a*a)*b)/2)*h
print("El resultado es : " , x)

# pedro , paublo beti y banban , decean conocer la nota definitiva 
# de su materia favorida programacion basica teniendo en cuenta
# que en el periodo se sacarondos dos notas una con el 30% y la otra con el 70%
# calcular la nota definitiva aplicar todo lo relacionado a la clase


pedroNota1 = float(input("pedro nota 1 : "))
pedroNota2 = float(input("pedro nota 2 : "))

paubloNota1 = float(input("paublo nota 1 : "))
paubloNota2 = float(input("paublo nota 2 : "))

betiNota1 = float(input("beti nota 1 : "))
betiNota2 = float(input("beti nota 2 : "))

banbanNota1 = float(input("banban nota 1 : "))
banbanNota2 = float(input("banban nota 2 : "))


resultadoNotaPedro = (pedroNota1 * 0.30) + (pedroNota2 * 0.70)
resultadoNotapaublo = (paubloNota1 * 0.30) + (paubloNota2 * 0.70)
resultadoNotaBeti = (betiNota1 * 0.30) + (betiNota2 * 0.70)
resultadoNotaBanban = (banbanNota1 * 0.30) + (banbanNota2 * 0.70)

print("nota de pedro es : " , resultadoNotaPedro)
print("nota de paublo es : " , resultadoNotapaublo)
print("nota de beti es : " , resultadoNotaBeti)
print("nota de banban es : " , resultadoNotaBanban)
