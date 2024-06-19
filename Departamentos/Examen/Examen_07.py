#Angel Antonio Perez Rodriguez
print("Ingrese la cantidad que paga de renta anual")
renta=int(input())
total=0

if renta < 60000:
    total = 60000*0.10
    print("Su total a pagar es: ",renta-total,"E")
elif renta >=60000:
    total = 60000*0.45
    print("Su total a pagar es: ",renta-total,"E")
    

    
    

