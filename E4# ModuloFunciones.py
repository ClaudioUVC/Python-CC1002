#perimetrotriangulo: num num num -> num
#Calcula el perimetro de un triangulo
#ej: perimetrotriangulo(3,4,5) es 12
def perimetrotriangulo(a,b,c):
    return a+b+c

#areatriangulo: num num num -> num
#Calcula el area de un triangulo
#ej: areatriangulo(3,4,5) es 6
def areatriangulo(a,b,c):
    import math
    s = ((a+b+c)/2.0)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

#triangulovalido: num num num -> boolean
#Indica si los lados proporcionados son capaces de formar un triangulo
#ej: triangulo(3,4,5) entregara "True"
def triangulovalido(a,b,c):
    if a>0 and b>0 and c>0:
        if ((a+b)>c) and ((b+c)>a) and ((c+a)>b):
            return True
        else:
            return False
    else:
        return False

#tipotriangulo: num num num -> str
#Identifica el tipo de triangulo a partir de los lados entregados.
#ej: tipotriangulo(3,4,5) es Escaleno
def tipotriangulo (a,b,c):
    if a==b and b==c:
        print "Equilatero."
    else:
        if a==b or b==c or c==a:
            print "Isosceles."
        else:
            print "Escaleno."

#triangulorectangulo: num num num -> boolean
#Identifica si el triangulo formado es rectangulo o no.
#ej: triangulorectangulo(3,4,5) entregara "True"
def triangulorectangulo(a,b,c):
    if ((a*a)+(b*b))==(c*c):
        return True
    else:
        if ((b*b)+(c*c))==(a*a):
            return True
        else:
            if ((c*c)+(a*a))==(b*b):
                return True
            else:
                return False
