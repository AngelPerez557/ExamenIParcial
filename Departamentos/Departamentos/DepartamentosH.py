import os
os.system('cls' if os.name == 'nt' else 'clear')
import  TotalDepartamentos 

usuario = "admin"
contrasenia = "admin123"
contraseniaInversa = contrasenia[::-1]
acceso = False

usu = input("Ingrese el usuario: ")

if usu == usuario:
    intento = input("Ingresa tu contraseña: ")
    intentoInverso = intento[::-1]

    if intento == contrasenia and intentoInverso == contraseniaInversa and contraseniaInversa[2::2] == intentoInverso[2::2]:
        acceso = True

        opcion = "S"
        while opcion.upper() == "S":
            print("Ingrese lo que desea hacer \n 1. Ver su departamento y municipio junto con su edad \n 2. Ver solo su municipio\n 3.Examen_07\n 4.Examen_17")
            deseo = int(input())
            if deseo == 1:
                print("Ingrese su numero de cedula")
                cedula = input()
                if len(cedula) >= 8 :  
                    try:
                        ano = int(cedula[4:8])
                        departamento = str(cedula[0:4])
                        edad = 2024 - ano

                        if departamento in TotalDepartamentos.Departamentos and ano <= 2024:  
                            print("Su departamento es:", TotalDepartamentos.Departamentos[departamento], "\nSu edad es:", edad)
                        else:
                            print("Algo salio mal, vuelve a intentarlo")

                    except ValueError:
                        print("La cedula debe contener numeros validos para el año y el departamento")

                    print("Desea Hacer otra cosa? S/N")
                    opcion = input()
                    import os
                    os.system('cls'if os.name == 'nt' else 'clear')
                    





            elif deseo == 2:
                print("Ingrese su numero de cedula")
                cedula = input()
                municipio = str(cedula[0:2])
                print("Los municipios de su departamento son:")
                if municipio == "01":
                    for clave, valor in TotalDepartamentos.Atlantida.items():
                        print(clave, valor)
                elif municipio == "02":
                        for clave, valor in TotalDepartamentos.Colon.items():
                            print(clave, valor)
                elif municipio == "03":
                        for clave, valor in TotalDepartamentos.Comayagua.items():
                            print(clave, valor)        
                elif municipio == "04":
                        for clave, valor in TotalDepartamentos.Copan.items():
                            print(clave, valor)
                elif municipio == "05":
                        for clave, valor in TotalDepartamentos.Cortes.items():
                            print(clave, valor)
                elif municipio == "06":
                        for clave, valor in TotalDepartamentos.Choluteca.items():
                            print(clave, valor)
                elif municipio == "07":
                        for clave, valor in TotalDepartamentos.Paraiso.items():
                            print(clave, valor)
                elif municipio == "08":
                        for clave, valor in TotalDepartamentos.Morazan.items():
                            print(clave, valor)
                elif municipio == "09":
                        for clave, valor in TotalDepartamentos.Gracias.items():
                            print(clave, valor)
                elif municipio == "10":
                        for clave, valor in TotalDepartamentos.Intibuca.items():
                            print(clave, valor)
                elif municipio == "11":
                        for clave, valor in TotalDepartamentos.Isla.items():
                            print(clave, valor)
                elif municipio == "12":
                        for clave, valor in TotalDepartamentos.Paz.items():
                            print(clave, valor)
                elif municipio == "13":
                        for clave, valor in TotalDepartamentos.Lempira.items():
                            print(clave, valor)
                elif municipio == "14":
                        for clave, valor in TotalDepartamentos.Ocotepeque.items():
                            print(clave, valor)
                elif municipio == "15":
                        for clave, valor in TotalDepartamentos.Olancho.items():
                            print(clave, valor)
                elif municipio == "16":
                        for clave, valor in TotalDepartamentos.Santa.items():
                            print(clave, valor)
                elif municipio == "17":
                        for clave, valor in TotalDepartamentos.Valle.items():
                            print(clave, valor)
                elif municipio == "18":
                        for clave, valor in TotalDepartamentos.Yoro.items():
                            print(clave, valor)  
            
                print("Desea Hacer otra cosa? S/N")
                opcion = input() 
                import os
                os.system('cls'if os.name == 'nt' else 'clear')


            
            elif deseo == 3:
                print("Ingrese la cantidad que paga de renta anual")
                renta=int(input())
                total=0

                if renta < 60000:
                    total = 60000*0.10
                    print("Su total a pagar es: ",renta-total,"E")
                elif renta >=60000:
                    total = 60000*0.45
                    print("Su total a pagar es: ",renta-total,"E")
            
            elif deseo == 4:
                print("Ingrese su edad")
                edad=int(input())

                for i in range(edad+1):
                    print(i)

                 
    else:
        print("Credenciales incorrectas")
else:
    print("Credenciales incorrectas")