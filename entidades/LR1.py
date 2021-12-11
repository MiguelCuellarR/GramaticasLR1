from Gramatica import Gramatica
from Estados import Estados
from ProduccionesEstado import ProduccionesEstado
class LR1:

    def __init__(self, gramatica):
        self._estados = []
        self._gramatica = gramatica

    def getEstados(self):
        return self._estados

    def _extenderGramatica(self):
        simbolo = self._gramatica.getSimboloInicial() + "'"
        produccion = simbolo + "::" + self._gramatica.getSimboloInicial()
        self._gramatica.getNoTerminales().add(simbolo)
        self._gramatica.getProducciones().insert(0, produccion)

    def analizar(self):
        self._extenderGramatica()
        partes = self._gramatica.getProducciones()[0].split('::')
        prodEst = ProduccionesEstado(partes[0]+'::.'+partes[1]+' ')
        prodEst.addTerminal('$')
        nombreEst = 'I-' + str(self._estados.__len__())
        self._crearEstado(nombreEst, prodEst)

    def _crearEstado(self, nombre, produccion, trancision = None):
        estado = Estados(nombre, produccion, trancision)
        self._estados.append(estado)
        self._identificarProducciones(produccion, estado)
        estado.Imprimir()
        self._correrPunto(estado)

    def _identificarProducciones(self, produccion, estado):
        partes = produccion.getProduccion().split('::')
        der = partes[1]
        sig = der[der.find('.')+1]
        sigSimb = ''

        if sig != ' ':
           sigSimb = der[der.find('.')+2]

        for prod in self._gramatica.getProducciones():
            part = prod.split('::')
            if part[0] == sig:
                prodEst = ProduccionesEstado(part[0]+'::.'+part[1]+' ')
                if sigSimb == '' or sigSimb == ' ':
                    for term in produccion.getTerminales():
                        prodEst.addTerminal(term)
                else:
                    self._buscarPrimero(sigSimb, prodEst)
                estado.addProduccion(prodEst)
                self._identificarProducciones(prodEst, estado)

        
    def _buscarPrimero(self, simbolo, produccionEst):
        if self._gramatica.getTerminales().__contains__(simbolo):
            produccionEst.addTerminal(simbolo)
        elif self._gramatica.getNoTerminales().__contains__(simbolo):
            for prod in self._gramatica.getProducciones():
                partes = prod.split('::')
                if partes[0] == simbolo:
                    self._buscarPrimero(partes[1][0], produccionEst)


    def _correrPunto(self, estado):
        for produccion in estado.getProducciones():
            partes = produccion.getProduccion().split('::')
            
            posPunto = partes[1].find('.')
            sig = partes[1][posPunto+1]

            
            
        

    
        

        
        
        
