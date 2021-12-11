from FuncionesGenerales import FuncionesGenerales as fncGen
from Gramatica import Gramatica
from LR1 import LR1

ruta = 'archivos\gramatica1.json'

gram = Gramatica()
gram = fncGen.leerJson(ruta)

lr1 = LR1(gram)
#ram.imprimir()

lr1.analizar()

#pal = ['hola.']
lr1.imprimir()
#print(pal[:pal.find('.')])
#print(pal.__len__())

