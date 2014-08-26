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
        
def otrabase(numero,base):
    nuevonumero=numero/base
    resto=numero%base
    if nuevonumero>0 and resto >=0:
        resto2=resto/10.0
        return (otrabase(nuevonumero,base)+resto2)*10
    elif nuevonumero==0 and resto>=0:
        return resto
