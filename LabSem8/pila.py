from nodo import Nodo

class Pila(object):
    def __init__(self):
        self.head = None
        self.count = 0


    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def push(self,x):   
        aux = Nodo(x,None)
        aux.next = self.head
        self.head = Nodo(x , self.head)
        self.count += 1
        self.aux2 = x

    def pop(self):
        if self.count == 0:
            self.head = None
            return None
        else: 
            aux3 = self.head
            self.head = self.head.next
            self.count = self.count - 1
            return aux3.element

    def top(self):
        return self.aux2

    def size(self):
        return self.count


