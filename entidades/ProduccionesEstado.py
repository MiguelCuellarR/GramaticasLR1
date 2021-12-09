from Estados import Estados

class ProduccionesEstado:
    
    def __init__(self, produccion):
        self._produccion = produccion
        self._estadoSiguiente = None
        self._produccionR = ""
 
    def getProduccion(self):
        return self._produccion

    def getEstadoSiguiente(self):
        return self._estadoSiguiente

    def getProduccionR(self):
        return self._produccionR

    def setEstadoSiguiente(self, estadoSiguiente):
        self._estadoSiguiente = estadoSiguiente
    
    def setProduccionR(self, produccionR):
        self._produccionR = produccionR
