#EDTEAM
#year = 2023
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# print ("El año ",  year,  "es bisiesto.")
#else: 
#    print("El año " , year , " no es bisiesto.")

# cajero automatico

def ejecutar():
    saldo = 1000
    
    while (True):
        
        opcion = input ("Que deseas hacer?\n1, consignar\n2, retirar\n3, salir")
        if (opcion == "3"):
            print("hasta luego")
            break
        if (opcion == " 1"):
            valor = input(int)("Digite el valor a consignar")
            saldo += valor
            print("Accion realizada correctamente. saldo: " + saldo)
            
        elif ( opcion == "2"):
            valor = input(int)("Digite el valor a retirar")
            
        if (valor > saldo):
            print("no se realizo la accion. Saldo" + saldo)
        else:
            saldo -= valor
            print("Accion realizada correctamente. Saldo" + saldo)
            
    else:
         print("Opcion invalida")
         
        
            

            
            
