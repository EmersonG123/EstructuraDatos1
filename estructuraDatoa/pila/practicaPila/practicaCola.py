class Cola():
    def __init__(self,size):
        self.lista=[]
        self.size=size
    def empty(self):
        if len(self.lista)==0:
            return True
        else:
            return False
    def agregar(self,dato):
        if len(self.lista)<self.size:
            self.lista.append(dato)
        else:
            print("la cola esta llena")

    def pop(self):
        if self.empty():
            print("la cola esta vacia")
        else:
            self.lista=[self.lista[x] for x in range(1,len(self.lista))]
            self.size-=1 
    def leerUltimo(self):
        return self.lista[-1]
    def vaciar(self):
        self.size=0
        return self.size
    def leerLista(self):
        i=0
        while i<self.size-1:
            print(self.lista[i])
            i+=1
        
cola1=Cola(4)
cola1.agregar(20)
cola1.agregar(2)
cola1.agregar(2)
cola1.leerLista()
cola1.leerLista()