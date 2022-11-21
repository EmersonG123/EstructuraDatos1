from listaEnlazadSimple import listaSimpleEnlazada
class Main:
    lista=listaSimpleEnlazada()
    lista.agregarUltimo(12)
    lista.agregarUltimo(18)
    lista.agregarUltimo(13)
    lista.agregarUltimo(14)
    lista.agregarUltimo(28)

    lista.eliminarInicio()
    lista.eliminarUltimo()
    lista.AgregarInicio(9)
    lista.buscar(18)


    lista.recorridos()