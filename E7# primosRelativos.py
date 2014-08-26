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

#MCD: int int -> bool
#Dice si dos numeros son primos relativos o no.
#ej: priRe(10,4) da True
def priRe(a,b):
    if MCD(a,b)==1:
        return True
    else:
        return False
    
#recur: int int -> string
#Analiza los primos relativos desde una base a, hasta b.
#ej: recur(2,20) entrega 2-3,2-5,2-7.....2-19.
def recur(a,b):
	minimo=2
	if priRe(a,b)==True and b>=2:
		print a,"~",b
		return recur(a,b-1)
	elif priRe(a,b)==False and b>=2:
		return recur(a,b-1)
	    
#recur2: int int -> string
#Analiza los primos relativos entre a y b.
#ej: recur(2,20) entrega 2-3,2-5,2-7.....2-19....19-20.
def recur2(a,b):
    if a<=b:
	recur(a,b)
	a=a+1
	recur2(a,b)
