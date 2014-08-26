def base10(numero,base):
    cifras=cifrasnumero(numero)
    exponente=cifras-1
    num=numero/(10**exponente)
    nuevonumero=numero%(10**exponente)
    if nuevonumero>0:
        nnu=base10(nuevonumero,base)
        return (num*base**exponente) + nnu
    else:
        return numero
    
def cifrasnumero(a):
    if a/10==0:
        return 1
    else:
        return 1 + cifrasnumero(a/10)

def otraBase(numero,base):
    cifras=cifrasNumeros(numero)
    exponente=cifras-1
    nuevoNumero=numero/(base**exponente)
    num=numero%(base**exponente)
    if nuevoNumero > 0
        nnu=otraBase(nuevoNumero,base)
        return (num*10**exponente)
    
    
