class Pila():
    def __init__(self,size):
        self.lista=[]
        self.tope=0
        self.size=size
    #metodo empty si nuestro pila no tiene elementos
    def empty(self): 
        if (self.tope==0):
            return True
        else: return False
    def push(self,dato):
        if (self.tope<self.size):
            self.lista+=[dato]
            self.tope+=1
            
        else:
            self.size+=5
            self.lista+=[dato] # se combierte en una pila dinamica 
            self.tope+=1
            print("la pila esta llena")
    def pop(self):
        if (self.empty()): 
            print("la pila esta vacia")
        else:
            self.tope-=1
            self.lista=[self.lista[x] for  x in range(self.tope)]
    def recorrerPila(self):
        i=self.tope-1
        while i>=0:
            print( f" elemento: {self.lista[i]} posicion {i}")
            i-=1
    def size(self):
        return self.tope
    def ultimoDate(self):
        return self.lista[-1]
