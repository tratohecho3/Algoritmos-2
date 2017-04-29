from cuco_entry import *
from cuco_table import *
import sys
def menu():

    print("1. Agregar un Cuco")
    print("2. Eliminar un Cuco")
    print("3. Buscar un Cuco por Clave")
    print("4. Mostrar los Cucos")
    print("5. Mostrar opciones")
    print("6. Salir")


lista = CucoTable()
n = input("Introduce el numero de elementos de la Tabla: ")
lista.crearCucoTabla(int(n))
menu()


while True:

    respuesta = input("Escoja una opcion: ")
    if respuesta == "1" :
        clave = input("Introduzca la clave del Cuco a agregar: ")
        valor = input("Introduzca el valor del Cuco a agregar: ")
        lista.agregar(clave,valor)



    elif respuesta == "2":
        clave = input("Introduzca la clave del Cuco a eliminar: ")
        lista.eliminar(clave)


    elif respuesta == "3":
        clave = input("Introduzca la clave del Cuco a buscar: ")
        lista.buscar(clave)         

    elif respuesta =="4":
        lista.mostrar()
    elif respuesta == "5":
        menu()
    elif respuesta == "6":
        print("Adios")
        sys.exit()
    else:
        pass





