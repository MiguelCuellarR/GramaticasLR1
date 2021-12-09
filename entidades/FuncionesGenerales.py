import json
from Gramatica import Gramatica

class FuncionesGenerales:

    def leerJson(rutaArchivo):
        gram = Gramatica()
        with open(rutaArchivo, 'r') as file:
            data = json.load(file)

            for terminal in data["terminales"]:
                gram.addTerminal(terminal)
            
            for noTerminal in data["noTerminales"]:
                gram.addNoTerminal(noTerminal)

            gram.setSimboloInicial(data["simboloInicial"])

            for produccion in data["producciones"]:
                gram.addProduccion(produccion)

        return gram
	