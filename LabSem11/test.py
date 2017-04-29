from nodo import Nodo
from arbolbinario import ArbolBinario
import sys

def menu():

    print("1. Agregar un elemento al arbol")
    print("2. Buscar un elemento en el arbol")
    print("3. Hallar el minimo del arbol")
    print("4. Hallar el maximo del arbol")
    print("5. Eliminar elemento")
    print("6. Mostrar los elementos del arbol")
    print("7. Mostrar opciones")
    print("8. Salir")

arbol = ArbolBinario()
arbol.crearArbol()

menu()


while True:

    respuesta = input("Escoja una opcion: ")
    if respuesta == "1" :
        string = input("Introduzca el string que desea añadir al arbol: ")
        arbol.agregar_elem(string)

    elif respuesta == "2":
        string = input("Introduzca el string que desea buscar en el arbol: ")
        print(arbol.buscar(string))


    elif respuesta == "3":
        print("El elemento minimo en el arbol es: ")
        print(arbol.minimo())         

    elif respuesta =="4":
        print("El elemento maximo en el arbol es: ")
        print(arbol.maximo())         

    elif respuesta == "5":
        string = input("Introduzca el string que desea eliminar: ")
        arbol.eliminar_elem(string)
        
    elif respuesta == "6":
        arbol.pre_orden(arbol.raiz)
    elif respuesta == "7":
        menu()
    elif respuesta == "8":
        print("Adios")
        sys.exit()
    else:
        pass


