#ingresar lados
import triangulo
import math
a=input ('Ingrese el primer lado: ')
b=input ('Ingrese el segundo lado: ')
c=input ('Ingrese el tercer lado: ')
if triangulo.triangulovalido(a,b,c)==True:
    if triangulo.triangulorectangulo(a,b,c)==True:
        print "El triangulo es: Rectangulo", triangulo.tipotriangulo(a,b,c)
        print "El perimetro del triangulo: ", triangulo.perimetrotriangulo(a,b,c)
        print "El area del triangulo: ", triangulo.areatriangulo(a,b,c)
    else:
        print "El triangulo es: ", triangulo.tipotriangulo(a,b,c)
        print "El perimetro del triangulo: ", triangulo.perimetrotriangulo(a,b,c)
        print "El area del triangulo: ", triangulo.areatriangulo(a,b,c)
else:
    print "Los lados proporcionados para formar el triangulo no son validos."
