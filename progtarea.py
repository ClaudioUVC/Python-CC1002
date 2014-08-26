import correcto
numero=input ("Ingrese el numero: ")
base=input ("Ingrese la base inicial: ")
if base>0:
    if correcto.correcto(numero,base) == True:
        if base==10:
        
        a=2
        b=10
        if a<=base:
            print "Base",a,": ",
    else:
        print "El numero que usted ha ingresado no corresponde a la base mencionada, por favor, intentelo denuevo."
else:
    print "Fin del programa."
