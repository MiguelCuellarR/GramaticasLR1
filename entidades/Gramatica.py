class Gramatica:

    def __init__(self):    
        self._terminales = set()
        self._noTerminales = set()
        self._simboloInicial = ""
        self._producciones = []

    def getSimboloInicial(self):
        return self._simboloInicial
    
    def getTerminales(self):
        return self._terminales

    def getNoTerminales(self):
        return self._noTerminales

    def getProducciones(self):
        return self._producciones

    def setSimboloInicial(self, simboloInicial):
        self._simboloInicial = simboloInicial

    def addTerminal(self, terminal):
        self._terminales.add(terminal)

    def addNoTerminal(self, noTerminal):
        self._noTerminales.add(noTerminal)

    def addProduccion(self, produccion):
        self._producciones.append(produccion)

    def imprimir(self):
        print('Terminales: ', self._terminales)
        print('No Terminales: ', self._noTerminales)
        print('Simbolo Inicial: ', self._simboloInicial)
        print('Producciones: ', self._producciones)
        
            