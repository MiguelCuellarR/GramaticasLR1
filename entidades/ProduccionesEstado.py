class ProduccionesEstado:
    
    def __init__(self, produccion):
        self._produccion = produccion
        self._terminales = set()
        self._estadoSiguiente = ''
        self._produccionR = ''
 
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

    def setEstadoSiguiente(self, estSiguiente):
        self._estadoSiguiente = estSiguiente
    
    def setProduccionR(self, produccionR):
        self._produccionR = produccionR

    def Imprimir(self):
        cont = 0
        mensaje = self._produccion + '   , '
        for term in self._terminales:
            if cont == 0:
                mensaje += term
            else:
                mensaje += ' | ' + term
            cont += 1
        if self._produccionR != '':
            mensaje += '\n' + self._produccionR
        else:
            mensaje += '       - ' + 'Siguiente: ' + self._estadoSiguiente
        mensaje += '\n'
        return mensaje