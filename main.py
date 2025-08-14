import matplotlib.pylab as plt
import pandas as pd 
from collections import defaultdict
from colorama import init, Fore, Back
init(autoreset=True) 
init()

def momento():
    import time
    print("")
    print("espere un momento...")
    print("")
    time.sleep (6)
    



def limpiar (): #funciòn llamad para limpiar pantallas
    from os import system
    system ("cls")

#impresòn de menù
opcion = 0
while opcion >= 0 or opcion < 8:
    limpiar ()
    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print (Fore.BLUE + " MENÚ PRINCIPAL".center(100))
    print (Fore.BLUE + " -(Elija una opción)- ".center(100))
    print (Fore.LIGHTRED_EX + "(RECUERDE AVANZAR EN ORDEN CRONOLÓGICO SEGÚN EL MENÚ)".center(100))
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print ("")
    print (Fore.BLUE + "1-▶️  Extracción e Información de la estructura de los datos")
    print (Fore.BLUE + "2-▶️  Normalizaciòn")
    print (Fore.BLUE + "3-▶️  Migración a DB SQL")
    print (Fore.BLUE + "4-▶️  Reset (volver a cero, eliminar base de datos, para nueva carga")
    print (Fore.BLUE + "5-▶️  carga y análisis")
    print (Fore.BLUE + "6-▶️  Informe final")
    print (Fore.BLUE + "7-▶️  Salir")
    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")

#validaciòn para que el menù solo se ingrese los numeros requeridos
    try:
        #input de elecciòn opciòn de demenù
        opcion = int(input("Seleccione una opción por su número: "))
        # captura de errores
    except ValueError:
        print (Fore.RED + "La opción que ingreso no es válida, vuelva a intentarlo")
        # tiempo para que se lea el enunciado del informe
        momento()
    # llamado a limpiar la patalla para que se efectìe arrastre de menùes y se preste a confusióm
    limpiar()
    match opcion:
        case 1:
            import opcion01
            opcion01.extraccion ()
        case 2:
            print ("")
            print (Fore.LIGHTBLUE_EX + 100*"*")
            print (Fore.LIGHTBLUE_EX+ "EXTRUCTURA DE DATOS (NORMALIZACIÒN)".center(100))
            print (Fore.LIGHTBLUE_EX + 100*"*")
            print (Fore.LIGHTBLUE_EX + " COLUMNAS QUE DEBERIAN SER NORMALIZADAS SEGÚN SUS TIPOS DE DATOS".center(100))
            print (Fore.LIGHTBLUE_EX + 100*"*")
            print ("")
            import opcion02
            opcion02.normalizacion ()
            #momento()
            print ("")
            print (Fore.LIGHTBLUE_EX + 100*"*")
            print (Fore.LIGHTBLUE_EX+ "SE CREARA UNA BASE DATOS EN SQLITE3 NORMALIZADA CON LA SIGUENTE ESTRUCTURA".center(100))
            print (Fore.LIGHTBLUE_EX + 100*"*")
            print ("")
            import db_migrar
            db_migrar.createdb
            db_migrar.create_tabla
            print ("")
            print (Fore.LIGHTBLUE_EX + 100*"*")
            print (Fore.LIGHTGREEN_EX+ "LA BASE DE DATOS TELECOMX (NORMALIZADA) SE CREÓ EXITOSAMENTE".center(100))
            print (Fore.LIGHTBLUE_EX + 100*"*")
            print ("")
        case 3:
            import opcion03
            opcion03.migracion ()
        case 4:
            import opcion04
            opcion04.eliminacion()
        case 5:
            #DISTRIBUCIÒN DE CHURN POR TIPO DE CONTRATO
            import opcion05
            opcion05.migracion()
            
            #agrupamiento por rangos de tenure
            import opcion05b
            opcion05b.promedio()

            #Tasa de churn por método de pago
            import opcion05c
            opcion05c.promedio()

            #Churn por combinación de servicios
            import opcion05d 
            opcion05d.conbinacion()
        case 6:
            import opcion06
            opcion06.informe()
        case 7:
            import opcion07
            opcion07.salir ()            
    input()
