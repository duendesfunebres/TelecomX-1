pass
    

def salir():
    def limpiar (): #funciòn llamad para limpiar pantallas
        from os import system
        system ("cls")
    from colorama import init, Fore, Back
    init(autoreset=True) 
    init()
    confirmar = 0
    limpiar()
    print ("")
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print (Fore.BLUE + " POR FAVOR CONFIRMAR".center(100))
    print (Fore.BLUE + " -(Elija una opción)- ".center(100))
    print (Fore.LIGHTBLUE_EX + 100*"*")
    print ("")
    while confirmar>= 0 or confirmar <=3:
        print ("0-  ME EQUIVOQUÉ DESEO VOLVER... ")
        print ("")
        print ("1- TERMINAR EL PROGRAMA Y SALIR DEFINITIVAMENTE")
        print ("")
        print (Fore.LIGHTBLUE_EX + 100*"*")
        print ("")
        try:
            confirmar = int(input("Seleccione una opción por su número: "))
        except ValueError:
            from colorama import init, Fore
            init(autoreset=True) 
            init()
            print (Fore.RED + "La opción que ingreso no es válida, vuelva a intentarlo")
            import time
            time.sleep (3)    
        else:
            if confirmar == 0:
                print ('presione nuevamente "ENTER"')
                break
            elif confirmar == 1:
                limpiar()
                quit()