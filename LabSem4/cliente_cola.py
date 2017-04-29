from arrayT import ArrayT
from heap_functions import build_max_heap, dequeue, heapify

'''
Sección de codigo que no será modificada por ningún estudiante en el
laboratorio. La idea es que se usen estos arreglos como prueba de su
implementación de la cola de prioridades.
'''

class Task(object):
    def __init__(self, *args, **kwargs):
        assert len(args) == 0, "Deben especificarse todos nombres de los parametro"
        assert len(kwargs) > 0, "Actividad vacía"
        assert len(kwargs) < 3, "Parametro excesivos"
        assert kwargs.get("prioridad"), "Falta especificar la prioridad de la actividad"
        assert kwargs.get("actividad"), "Falta especificar el nombre de la actividad"
        assert type(kwargs.get("prioridad")) == int, "La prioridad debe ser un entero"
        assert type(kwargs.get("actividad")) == str, "El nombre de la actividad debe ser un string"
        self.__prioridad = kwargs.get("prioridad")
        self.__actividad = kwargs.get("actividad")

    def __compare__(self, other):
        assert type(other) == Task or other == None, "No se puede comparar una actividad con un objeto de tipo {0}".format(type(other))
        if other == None:
            return(2)
        if self.__prioridad < other.__prioridad:
            return(1)
        elif self.__prioridad > other.__prioridad:
            return(-1)
        else:
            if self.__actividad < other.__actividad:
                return(1)
            elif self.__actividad > other.__actividad:
                return(-1)
            else:
                return(0)

    def __lt__(self,other):
        return(self.__compare__(other) == -1)

    def __le__(self,other):
        return(self.__compare__(other) == -1 or self.__compare__(other) == 0)

    def __eq__(self,other):
        return(self.__compare__(other) == 0)

    def __gt__(self,other):
        return(self.__compare__(other) == 1)

    def __ge__(self,other):
        return(self.__compare__(other) == 1 or self.__compare__(other) == 0)

    def __ne__(self,other):
        return(self.__compare__(other) != 0)

    def __repr__(self):
        return(self.__str__())

    def __str__(self):
        return(self.__actividad)

y = ArrayT(5)

y[0] = Task(prioridad=4,actividad="Hacer currículum")
y[1] = Task(prioridad=10,actividad="Comprar comida")
y[2] = Task(prioridad=2,actividad="Recargar telefono")
y[3] = Task(prioridad=5,actividad="Lavar la ropa")
y[4] = Task(prioridad=8,actividad="Ir al odontólogo")

print("Secuencia de actividades a realizar:\n")
build_max_heap(y)
while len(y) > 1:
    aux = dequeue(y)
    print("Realicé la actividad:", aux[0])
    y = aux[1]
    heapify(y,0,len(y))
    print("Faltan:", len(y))

print("Realicé la actividad:", y[0])
print("Terminé")