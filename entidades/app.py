from FuncionesGenerales import FuncionesGenerales as fncGen
from Gramatica import Gramatica
from LR1 import LR1


ruta = 'archivos\gramatica2.json'

gram = Gramatica()
gram = fncGen.leerJson(ruta)

lr1 = LR1(gram)
lr1.analizar()
lr1.imprimir()
