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
