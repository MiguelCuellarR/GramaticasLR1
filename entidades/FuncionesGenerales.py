import json
from Gramatica import Gramatica as gram

class FuncionesGenerales:

    def leerJson(rutaArchivo):
        with open(rutaArchivo, 'r') as file:
            data = json.load(file)
            print(data)

            for terminal in data["terminales"]:
                gram.addTerminal(gram, terminal)
            
            for noTerminal in data["noTerminales"]:
                gram.addNoTerminal(gram, noTerminal)

            gram.setSimboloInicial(gram, data["simboloInicial"])

            for produccion in data["producciones"]:
                gram.addProduccion(gram, produccion)

            gram.imprimir(gram)
	