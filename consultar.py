
class Consultar :
    def __init__(self,documento):
        self.documento = documento

    def mostrar(self):
        print("Documento:", self.documento)

from practicas_datos.persona import Personas

buscar = input("Ingresa el número de documento: ")
encontrado = False
for p in Personas:
    if p.documento == buscar:
        print("Documento encontrado:")
        p.datos_persona()
        encontrado = True
        break

if not encontrado:
    print("Documento no encontrado.")

