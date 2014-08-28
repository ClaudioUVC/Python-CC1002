import estructura
estructura.crear("fraccion","numerador denominador")

#sumaF: fraccion fraccion -> fraccion
def sumaF(a,b):
    num = b.denominador*a.numerador + a.denominador*b.numerador
    den = b.denominador*a.denominador
    return fraccion(num,den)

    
    
