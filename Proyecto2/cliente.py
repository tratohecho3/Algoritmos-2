from pathlib import Path
from cancion import Cancion
from lista import *
from reproductor import Reproductor

from PyQt5.QtWidgets import *

import sys
import subprocess as sp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rep = Reproductor()
    rep.show()
    sp.call('clear',shell=True)

    #############
    # Menu loop #
    #############

    # Su código iría aquí

def menu():

    print("1. Listar Canciones")
    print("2. Agregar para sonar justo despues de la cancion actual")
    print("3. Agregar para sonar justo antes de la cancion actual")
    print("4. Ordenar lista de reproduccion por artista")
    print("5. Ordenar lista de reproduccion por titulo")
    print("6. Eliminar cancion por titulo")
    print("7. Mostrar opciones")
    print("8. Salir")
menu()
while True:

    respuesta = input("Escoja una opcion: ")
    if respuesta == "1" :
            rep.mostrar() 

    elif respuesta == "2":
        titulo = input("Ingrese el titulo de la cancion: ")
        artista = input("Ingrese el autor de la cancion: ")
        path = input("Ingrese la direccion del archivo: ")
        path2 = path.split(".")
        if len(path2) == 2:
            if path2[1] == "wav":      
                cancion = Cancion(titulo,artista,path)
                nodo = NodoLista(cancion, None, None)
                rep.sonarDespues(nodo)
            else:
                print("===========================================")
                print("La direccion del archivo es invalida.")
                print("===========================================")
        else:
            print("===========================================")
            print("La direccion del archivo es invalida.")
            print("===========================================")            
    elif respuesta == "3":
        titulo = input("Ingrese el titulo de la cancion:")
        artista = input("Ingrese el autor de la cancion: ")
        path = input("Ingrese la direccion del archivo: ")
        path2 = path.split(".")
        if len(path2) == 2:
            if path2[1] == "wav":     
                cancion = Cancion(titulo,artista,path)
                nodo = NodoLista(cancion, None, None)
                rep.sonarAntes(nodo)
            else:
                print("===========================================")
                print("La direccion del archivo es invalida.")
                print("===========================================")
        else:
            print("===========================================")
            print("La direccion del archivo es invalida.")
            print("===========================================")

    elif respuesta =="4":
        rep.ordenar_artista()
    elif respuesta == "5":
        rep.ordenar_titulo()
    elif respuesta == "6":
        titulo = input("Ingrese el titulo de la cancion a eliminar: ")
        rep.eliminar(titulo)

    elif respuesta == "7":
        menu()
    elif respuesta == "8":  
        respuesta = input("¿Esta seguro de que desea salir? (Si/No) ")
        if respuesta.lower() == "si":
            print(" ")
            print("Esperamos que vuelva pronto")
            sys.exit()
        elif respuesta.lower() == "no": 
            print(" ")
            print(" ")
            menu()
        else: 
            print("===============================================================================")
            print("La opcion escogida no es valida. Volvera al menu principal.")
            print("===============================================================================")
            respuesta = "no"
            print(" ")
            print(" ")
            menu()

    else:
        print("====================================")
        print("Escoja una opción válida")
        print("====================================")
        print(" ")
        print(" ")
        menu()







    # Para eliminar una canción debe solicitar el título y pasarlo al método
    # eleminar de la instancia de Reproductor 'rep'.
    # 
    # rep.eliminar(titulo_solicitado)

    ############
    # Fin menu #
    ############

    sys.exit(app.exec_())