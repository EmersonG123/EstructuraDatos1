class Nodo:
    def __init__(self,dato,siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
    def __str__(self):
        return self.dato
nodo4=Nodo(165)
nodo3=Nodo(13,nodo4)
nodo2=Nodo(16,nodo3)
nodo1=Nodo(12,nodo2)
def recorrerNodo(nodo):
    while nodo!=None:
        print(nodo.dato)
        nodo=nodo.siguiente
recorrerNodo(nodo1)