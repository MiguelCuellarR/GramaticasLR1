
class Estados:

    def __init__(self, nombre, transicion = None):
        self._nombre = nombre
        self._trancision = transicion
        self._producciones = []

    def getNombre(self):
        return self._nombre

    def addProduccion(self, produccion):
        self._producciones.append(produccion)

    def getProducciones(self):
        return self._producciones