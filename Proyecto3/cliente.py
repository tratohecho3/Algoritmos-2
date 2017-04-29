from usuario import *
from registro_usuario import *
from chat import *
from conversaciones import *

def cargarCaritas(archivo):
    f = open(archivo,"r+")
    caritas1 = f.readlines()
    aux = caritas1[0]
    caritas2 = aux.split("\t")
    return caritas2

def mostrarCaritas(caritas4):
    mostrar = ""
    mostrar = mostrar + caritas4[0][0:2]
    for i in range(1,len(caritas4)):
        mostrar = mostrar + "," + caritas4[i][0:2]
    print(mostrar)

def menu1():
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Cargar usuarios")
    print("4. Eliminar usuario")
    print("5. Cargar caritas")

def menu2():
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Mostrar contactos")
    print("4. Ver conversacion")
    print("5. Enviar mensaje")
    print("6. Mostrar caritas")
    print("7. Mostrar usuarios registrados")
    print("8. Cerrar Sesion")
tabla = tablaRU()
tabla.crear_tabla(20)
caritas3 = None
conversacion = conversaciones()
conversacion.crearTabla(20)
menu1()
while True:
    respuesta = input("Por favor introduce una opcion: ")

    if respuesta == "1":
        nombre = input("Introduce el nombre del usuario: ")
        password = input("Introduce la password del usuario: ")
        telefono = input("Introduce el telefono del usuario: ")
        lista = Lista()
        usuario = Usuario()
        usuario.crearUsuario(nombre,password,telefono,lista)
        nodo = Nodo(usuario)
        if tabla.agregarUsuario(nodo):
            print("Usuario creado exitosamente")
            menu1()
        else:
            print("El usuario ya existe")
            menu1()

    elif respuesta == "2":
        nombre_usuario = input("Por favor introduce el nombre de usuario: ")
        password_usuario = input("Por favor introduce la password del usuario: ")
        if tabla.login(nombre_usuario,password_usuario)[0]:
            print("Bienvenido " + nombre_usuario)
            usuario_logueado = tabla.login(nombre_usuario,password_usuario)[1]
            menu2()
            while True:
                respuesta_interna = input("Por favor introduce una opcion: ")

                if respuesta_interna == "1":
                    nombre_agregar = input("Por favor introduce el nombre del contacto a agregar: ")

                    if tabla.buscar_nombre(nombre_agregar)[0]:
                        usuario_logueado.dato.agregarContacto(tabla.buscar_nombre(nombre_agregar)[1].dato)
                        print("Usuario agregado exitosamente")
                        menu2()
                    else:
                        print("Ese usuario no esta registrado")
                        menu2()

                elif respuesta_interna == "2":
                    nombre_eliminar = input("Por favor introduce el nombre del contacto a eliminar: ")
                    usuario_logueado.dato.eliminarContacto(nombre_eliminar)
                    menu2()

                elif respuesta_interna == "3":
                    print("Tus contactos registrados son: ")
                    usuario_logueado.dato.mostrarContactos()
                    menu2()
                elif respuesta_interna == "4":
                    registrado = False
                    contacto1 = input("¿Con que usuario desea ver la conversacion?: ")
#                    print(usuario_logueado.dato.contactos.buscar_nombre(contacto1)[0])
#                    print(usuario_logueado.dato.contactos.buscar_nombre(contacto1)[1].dato.nombre)
                    if usuario_logueado.dato.contactos.buscar_nombre(contacto1)[0]:
                        registrado = True
                    if registrado == False:
                        print("El usuario ingresado no está en su lista de amigos o no existe")
                        menu2()
                    hay = True
                    if contacto1 < nombre_usuario:
                        if conversacion.buscarConversacion(contacto1 + "-" + nombre_usuario) == None:
                            hay = False
                    else:
                        if conversacion.buscarConversacion(nombre_usuario + "-" +contacto1) == None:
                            hay = False
                    if hay == True:
                        if contacto1 < nombre_usuario:
                            c = conversacion.buscarConversacion(contacto1 + "-" + nombre_usuario)
                        elif nombre_usuario < contacto1:
                            c = conversacion.buscarConversacion(nombre_usuario + "-" + contacto1)
                        c.mensaje.mostrar()
                    elif hay == False:
                        print("No se tiene una conversacion registrada con dicho usuario")
                    menu2()

                elif respuesta_interna == "5":
                    contacto1 = input("Ingrese el nombre del usuario al que le desea escribir: ")
                    nodo = Nodo(contacto1)
                    if usuario_logueado.dato.contactos.buscar_nombre(contacto1)[0]:
                        mensaje = input("Ingrese el mensaje que se desea enviar: ")
                        mensaje = nombre_usuario + ": " + mensaje
                        if contacto1 < nombre_usuario:
                            conver = conversacion.buscarConversacion(contacto1 + "-" +nombre_usuario)
                        else:
                            conver = conversacion.buscarConversacion(nombre_usuario + "-" + contacto1)
                        nodo2 = Nodo(mensaje)
                        if conver == None:
                            chat1 = chat()
                            chat1.crearChat(contacto1,nombre_usuario)
                            chat1.agregarMensaje(nodo2)
                            conversacion.agregarConversacion(chat1)
                        else:
                            chat1.agregarMensaje(nodo2)
                    else:
                        print("El usuario no se encuentra en su lista de contactos")
                    menu2()


                elif respuesta_interna == "6":
                    if caritas3 == None:
                        print("No se ha cargado ningun paquete de caritas")
                    else:
                        mostrarCaritas(caritas3)
                elif respuesta_interna == "7":
                    print("Los usuarios registrados son: ")
                    tabla.mostrarRegistro()
                    menu2()
                elif respuesta_interna == "8":
                    print("Deslogueado satisfactoriamente")
                    menu1()
                    break


        else:
            print("Error, Usuario o password incorrecta")
            menu1()


    elif respuesta == "3":
        archivo = input("Por favor introduce el nombre del archivo para el registro de usuarios: ")
        tabla.cargarUsuarios(archivo)
        menu1()
    elif respuesta == "4":
        nombre = input("Introduce el nombre del usuario a eliminar: ")
        if tabla.eliminarUsuario(nombre):
            print("Usuario eliminado")
            menu1()
        else:
            print("El usuario no existe")
            menu1()
    elif respuesta == "5":
        carita = input("Introduce el nombre del archivo donde se encuentran las caritas: ")
        caritas3 = cargarCaritas(carita)



