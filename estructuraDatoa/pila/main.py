from Pila import Pila
from os import system
system("clear")
class Main:
    pila1=Pila(5)
    pila1.push(23)
    pila1.push(43)
    pila1.push(13)
    pila1.push(93)
    pila1.recorrerPila()
    pila1.pop()
    print("----------")
    pila1.recorrerPila()
    def verEstado():
        pass