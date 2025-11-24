lista = []

class Registrar_personas:
    def __init__(self, nombre, apellido, edad, ciudad, documento, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
        self.documento = documento
        self.correo = correo

    def datos_persona(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Documento: {self.documento}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Correo: {self.correo}")