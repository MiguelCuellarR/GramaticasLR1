class ProduccionesEstado:
    
    def __init__(self, produccion):
        self._produccion = produccion
        self._terminales = set()
        self._estadoSiguiente = ""
        self._produccionR = ""
 
    def getProduccion(self):
        return self._produccion

    def getTerminales(self):
        return self._terminales

    def getEstadoSiguiente(self):
        return self._estadoSiguiente

    def getProduccionR(self):
        return self._produccionR

    def addTerminal(self, terminal):
        self._terminales.add(terminal)

    def setEstadoSiguiente(self, estadoSiguiente):
        self._estadoSiguiente = estadoSiguiente
    
    def setProduccionR(self, produccionR):
        self._produccionR = produccionR

    def Imprimir(self):
        mensaje = self._produccion + '  , '
        for term in self._terminales:
            mensaje += term + '| '
        mensaje += '\n' + 'Siguiente: ' + self._estadoSiguiente
        if self._produccionR != '':
            mensaje += '\n' + self._produccionR
        mensaje += '\n'
        return mensaje