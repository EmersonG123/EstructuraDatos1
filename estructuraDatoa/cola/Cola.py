class Cola():
    def __init__(self):
        self.cola=[]
        self.size=0
    def empty(self):
        return len(self.cola)==0
    def  push(self,dato):
        self.cola.append(dato)
        self.size+=1
    def pop(self):
        if self.empty():
            print("la cola esta vacia")
        else:
            self.cola=[self.cola[x] for x in range(1,self.size)]
            self.size-=1
    def recorrerCola(self):
        n=self.size-1
        while n>=0:
            print(f" {[n]} => {self.cola[n]}")
            n-=1
    def Front(self):
        if self.empty()!=False:
            return f" ultimo dato => {self.cola[0]}"
        else:
            print("no existe elementos en la cola")
