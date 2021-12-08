#Gramatica = Terminales, NoTerminales, SimboloInicial, Producciones
#Estados = id, Lista<String Producciones>
#Analizador = metodos importantes pa identificar LR1

from typing import List, Set

class Gramatica:

    terminales = list()
    noTerminales = list()
    simboloInicial = ""
    producciones = list()

    def getSimboloInicial(self):
        return self.simboloInicial
    
    def getTerminales(self):
        return self.terminales

    def getNoTerminales(self):
        return self.noTerminales

    def getProducciones(self):
        return self.producciones

    def setSimboloInicial(self, simboloInicial):
        self.simboloInicial = simboloInicial

    def addTerminal(self, terminal):
        self.terminales.append(terminal)

    def addNoTerminal(self, noTerminal):
        self.noTerminales.append(noTerminal)

    def addProduccion(self, produccion):
        self.producciones.append(produccion)

    def imprimir(self):
        print('Terminales: ', self.terminales)
        print('No Terminales: ', self.noTerminales)
        print('Simbolo Inicial: ', self.simboloInicial)
        print('Producciones: ', self.producciones)
        
            