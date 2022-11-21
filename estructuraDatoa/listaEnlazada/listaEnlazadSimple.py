from nodo  import Nodo 
class listaSimpleEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def listaVacia(self):
        return self.primero==None
    def agregarUltimo(self,dato):
        if self.listaVacia()==True:
            self.primero=self.ultimo=Nodo(dato)
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente=Nodo(dato)
    #eliminar ultimo dato
    def eliminarUltimo(self):
        aux=self.primero
        while(aux.siguiente != self.ultimo):
            aux=aux.siguiente
        aux.siguiente=None
        self.ultimo=aux
    #agregar inicio
    def AgregarInicio(self,dato):
        if (self.listaVacia==True):
            self.primero=self.ultimo=Nodo(dato)
        else:
            aux=Nodo(dato)
            aux.siguiente=self.primero
            self.primero=aux
    #eliminar inicio
    def eliminarInicio(self):
        self.primero=self.primero.siguiente    
            

    def recorridos(self):
        aux=self.primero
        while aux!=None:
            print(aux.dato)
            aux=aux.siguiente
    def buscar(self,da):
        cont=0
        aux=self.primero
        while aux!=None:
            if(aux.dato==da):
                print("se encontro el dato en el nodo numero :",cont)

            cont+=1  
            aux=aux.siguiente
        

