#perimetro
def perimetrotriangulo(a,b,c):
    return a+b+c

#area
#num->num
def areatriangulo(a,b,c):
    import math
    s = ((a+b+c)/2.0)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

#valido
def triangulovalido(a,b,c):
    if a>0 and b>0 and c>0:
        if ((a+b)>c) and ((b+c)>a) and ((c+a)>b):
            return True
        else:
            return False
    else:
        return False

#tipo
def tipotriangulo (a,b,c):
    if a==b and b==c:
        print "Equilatero."
    else:
        if a==b or b==c or c==a:
            print "Isosceles."
        else:
            print "Escaleno."

#rectangulo
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
