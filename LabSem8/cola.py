from nodo import Nodo

class Cola(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False
    def enqueue(self,x):
        nodo = Nodo(x,None)
        if self.head == None and self.last == None:
            self.count += 1
        else:
            self.last = nodo
            self.last.next = nodo
            self.count += 1
        return None
    def dequeue(self):
        if self.count == 0:
            self.head = None
            return None
        else:
            aux = self.head.element
            self.head = self.head.next
            self.count = self.count - 1
            return aux
    def size(self):
        return self.count
    def first(self):
        return self.head.element