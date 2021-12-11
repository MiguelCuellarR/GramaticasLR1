
class Estados:

    def __init__(self, nombre, produccion, transicion = None):
        self._nombre = nombre
        self._trancision = transicion
        self._producciones = [produccion]

    def getNombre(self):
        return self._nombre

    def getTransicion(self):
        return self._trancision 

    def addProduccion(self, produccion):
        self._producciones.append(produccion)

    def getProducciones(self):
        return self._producciones

    def Imprimir(self):
        print(self._nombre)
        if self._trancision is not None:
            print('Transiciona con: ' + self._trancision)
        mensaje = ''
        for prod in self._producciones:
            mensaje += prod.Imprimir()
        print(mensaje)