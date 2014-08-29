#base10: int int -> int
#Convierte a un numero decimal, desde cualquier otra base entre 2 y 9.
#ejemplo.
def base10(numero,base):
    cifras=cifrasNumero(numero)
    exponente=cifras-1
    num=numero/(10**exponente)
    nuevonumero=numero%(10**exponente)
    if nuevonumero>0:
        nnu=base10(nuevonumero,base)
        return (num*base**exponente) + nnu
    else:
        return numero

#cifrasNumero: int -> int
#Indica las cifras de un numero entregado.
#ejemplo.
def cifrasNumero(a):
    if a/10==0:
        return 1
    else:
        return 1 + cifrasNumero(a/10)

#otraBase: int int -> int
#Cambia un numero a una base cualquiera (entre 2 y 9),desde una decimal.
#ejemplo.
def otraBase(numero,base):
    nuevonumero=numero/base
    resto=numero%base
    if nuevonumero>0 and resto >=0:
        resto2=resto/10.0
        return int(str(otraBase(nuevonumero,base))+str(resto))
    elif nuevonumero==0 and resto>=0:
        return resto
    
#correcto: int int -> boolean
#Indica si un numero esta escrito correctamente en una base.
#ejemplo.
def correcto(numero,base):
    nuevonumero=numero/10
    resto=numero%10
    if nuevonumero > 0:
        if resto < base:
            Respuesta= True*correcto(nuevonumero,base)
            if Respuesta==1:
                return True
            else:
                return False
        else:
            return False
    else:
        return True

#convertir:
#Un programa interactivo que convierte cualquier numero en base entre 2 y 10, al resto de las bases.
#ejemplo.
def convertir():
    num=input ("Ingrese el numero: ")
    bas=input ("Ingrese la base: ")
    if bas==1 or bas>10:
        print "La base solo puede ser entre 2 y 10."
        return convertir()
    elif bas==0:
        print "El programa ha finalizado."
    elif correcto(num,bas)==True:
        ab10=base10(num,bas)
        print "En base 2: ",otraBase(ab10,2)
        print "En base 3: ",otraBase(ab10,3)
        print "En base 4: ",otraBase(ab10,4)
        print "En base 5: ",otraBase(ab10,5)
        print "En base 6: ",otraBase(ab10,6)
        print "En base 7: ",otraBase(ab10,7)
        print "En base 8: ",otraBase(ab10,8)
        print "En base 9: ",otraBase(ab10,9)
        print "En base 10: ",otraBase(ab10,10)
        return convertir()
