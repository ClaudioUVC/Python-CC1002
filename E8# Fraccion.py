# -*- coding: utf-8 -*-
import estructura
estructura.crear("fraccion","numerador denominador")

#sumaF: fraccion fraccion -> fraccion
#suma fracciones
#ej: sumF(fraccion(3,4),fraccion(4,5)) = fraccion(numerador=31, denominador=20)
def sumaF(a,b):
    num = b.denominador*a.numerador + a.denominador*b.numerador
    den = b.denominador*a.denominador
    return fraccion(num,den)

#restaF: fraccion fraccion -> fraccion
#resta fracciones
#ej: restaF(fraccion(3,4),fraccion(4,5)) = fraccion(numerador=-1, denominador=20)
def restaF(a,b):
    num = b.denominador*a.numerador - a.denominador*b.numerador
    den = b.denominador*a.denominador
    return fraccion(num,den)

#mulF: fraccion fraccion -> fraccion
#multiplica fracciones
#ej: mulF(fraccion(3,4),fraccion(4,5)) = fraccion(numerador=12, denominador=20)
def mulF(a,b):
    num=a.numerador*b.numerador
    den=a.denominador*b.denominador
    return fraccion(num,den)

#divF: fraccion fraccion -> fraccion
#divide fracciones
#ej: divF(fraccion(3,4),fraccion(4,5)) = fraccion(numerador=15, denominador=16)
def divF(a,b):
    num=a.numerador*b.denominador
    den=a.denominador*b.numerador
    return fraccion(num,den)

#MCD: int int -> int
#Calcula el maximo comun divisor
#ej: MCD(10,4) es 2
def MCD(x,y):
    x=abs(x)
    y=abs(y)
    mayor=max(x,y)
    menor=min(x,y)
    resto=(mayor%menor)
    if resto == 0:
        return menor
    else:
        return MCD(menor,resto)

#-
def aString(x):
  return str(x.numerador)+"/"+str(x.denominador)

#simplificar: fraccion -> fraccion
#simplifica  una fracción
#ej: simplificar(fraccion(2,4))->fraccion(1,2)
def simplificar(x):
  m=MCD(x.numerador,x.denominador)
  return fraccion(x.numerador/m, x.denominador/m)

#prueba: fraccion fraccion -> fraccion
#suma, resta, multiplica y divide fracciones
def prueba(a,b):
    suma=aString(simplificar(sumaF(a,b)))
    resta=aString(simplificar(restaF(a,b)))
    mul=aString(simplificar(mulF(a,b)))
    div=aString(simplificar(divF(a,b)))
    return "La suma es: "+suma+\
           " ~ La resta es: "+resta+\
           " ~ La multiplicacion es: "+mul+\
           " ~ La division es: "+div
