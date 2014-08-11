#Al ejecutar el programa interactivo se pedira entregar las medidas
#del triangulo deseado. El programa detectara si las medidas propor
#cionadas son capaces de formar un triangulo, de modo contrario el
#programa avisara del error. Si las medidas entregadas son capaces
#de formar un triangulo, se imprimira en pantalla el tipo de trian-
#gulo, si es rectangulo, el area y el perimetro de este.
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
