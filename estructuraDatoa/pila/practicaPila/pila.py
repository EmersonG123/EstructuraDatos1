class Pila():
    def __init__(self,size):
        self.lista=[]
        self.tope=0
        self.size=size
    def empty(self):
        if self.tope==0:
            return True
        else:
            return False

    def llena(self):
        if self.tope==self.size:
            return  True
        else:
            False

    def push(self,dato):
        if self.tope<self.size:
            self.lista+=[dato]
            self.tope+=1
        else:
            print("pila llena")
    def pop(self):
        if self.empty():
            print("pila vacia")
        else:
            self.tope-=1
            self.lista=[self.lista[x] for x in (self.lista)]
    def recorrerPila(self):
        if self.empty()==False:
            i=self.tope-1
            while i>=0:
                print( f" elemento: {self.lista[i]} posicion {i}")
                i-=1
        else:
            print("[ ]")
    def leerUltimo(self):
        return self.lista[-1]
    def tamanio(self):
        return self.tope
    def vaciar(self):
        self.tope=0
        return self.tope
pila=Pila(4)
pila.push(1)
pila.push(2)
pila.push(3)
pila.recorrerPila()
print(pila.tamanio())
print(pila.leerUltimo())
pila.vaciar()
pila.recorrerPila()
print("################################")
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.recorrerPila()
pila.push(5)