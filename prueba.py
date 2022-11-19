# PIA: Sistema Criptografico
# Integrantes:
# 1911964
# 1920760
# 1743353
# 1819511
# 1821251

import main # Se importo el codigo main 
import time

while True:
    print("\n")
    print("\n-----------------MENÚ----------------\n")
    #Se le muestra el menu al usuario y debera escoger entre 3 opciones
    print("Bienvenido, ¿desea registrarse (1), iniciar sesion (2) o salir (3)?") 
    op= int(input("Opción: "))

    while op!=1 and op!=2 and op!=3:
        print("Opción no valida, seleccione una que lo sea.\n")
        print("Bienvenido, ¿desea registrarse (1), iniciar sesion (2) o salir (3)?")
        op= int(input("Opción: "))
    
    #Registro del usuario
    if op == 1:
        username= input("\nIngrese un nombre de usuario: ")
        password= input("Ingrese una contraseña: ")
        Age= input ("Cual es tu edad")
        Email= input("Ingresa tu correo")
        Celphone= input("Cual es tu telefono")

        main.register(username, password)
        print("\nEspere un momento...Listo sus datos han sido registrados!" + username + "con el correo" + Email) #Se registra al usuario

        
        #Firma de documentos
        print("Realizando la firma de documentos.....listo..")
        time.sleep(5)                                           #Se importo el modulo time para generar una espera
        with open (username + ".cer", "rb") as f:
            cer= str(f.read())                          #Abre el archivo .cer y lo lee
        seed= bytes(32)
        
        a= main.sign(cer, seed)     #Se genera la firma

        file= open("Firma_" + username + ".txt", "w")      #Se crea un archivo txt, que contiene la firma generada
        file.write(str(a))
        file.close()                                    
        
        print("\nSe realizo la firma de documentos con exito.")
    
    #Inicio de sesión del usuario
    elif op == 2:
        namecer= input("\nIngresa el nombre certificado (.cer): ")          #Ejemplo: santiago.cer
        namekey= input("Ingresa el nombre de la clave privada (.key): ")    #Ejemplo: santiago.key
        password= input("Ingresa la contraseña de la clave privada: ")      #Contraseña registrada con el usuario
        x= main.login(namecer, namekey, password)
        while x == False:
            print("Contraseña incorrecta. Vuelve a intentarlo:\n")
            password= input("Ingresa la contraseña de la clave privada: ")
            x= main.login(namecer, namekey, password)
        print("\nSe ha iniciado sesión con exito!\n")                       #El usuario inicia sesión
        print("\nRealizando la firma de documentos.......\n")
        time.sleep(5)
        with open (namecer + ".cer", "rb") as f: #Abre el archivo .cer y lo lee
            cer= str(f.read())
        seed= bytes(32)
        
        a= main.sign(cer, seed)     #Se genera la firma

        file= open("Firma_" + namecer + ".txt", "w")            #Se crea un archivo txt, que contiene la firma generada
        file.write(str(a))
        file.close()
      
        print("\nSe realizo la firma de documentos con exito.")

    #Salir y cerrar el programa
    elif op == 3:
        print("\nHasta luego! :D")
        break

    #Regresar al menu o salir
    print("\n¿Desea regresar al menu (1) o salir (2)?")
    i= int(input("Opción: "))

    if i != 1:
        print("\nHasta luego :D")
        break

