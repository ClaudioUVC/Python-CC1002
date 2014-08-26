#para llamarlo basta import progmcd
import mcd
print "Ingrese el numerador, presione ENTER y luego ingrese el denominador"
a=input("Ingrese el numerador: ")
b=input("Ingrese el denominador: ")
divisor=mcd.MCD(a,b)
if a == 0:
    print "Su fraccion es indefinida, por lo cual no puede simplificarse."
else:
    if b==0:
        print "ERROR: Su fraccion esta indeterminada porque posee un 0 en el denominador."
    else: 
        if divisor > 1:
            numerador=(a)/divisor
            denominador=(b)/divisor
            print "Su expresion ha sido simplificada por: ",divisor
            print "Su fraccion ha quedado como: ",numerador,"/",denominador
        else:
            print "Su numero ya esta simplificado"
