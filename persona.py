lista = []

class Registrar_personas:
    def __init__(self, nombre, apellido, edad, ciudad, documento, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.ciudad = ciudad
        self.correo = correo

    def datos_persona(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad)
        print("Documento:", self.documento)
        print("Ciudad:", self.ciudad)
        print("Correo:", self.correo)

def registrar():
    print(" Registro de persona")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
documento = input("Ingresa el número de identificación: ")
ciudad = input("Ingresa la ciudad: ")
correo = input("Ingresa tu correo: ")
persona = Registrar_personas(nombre, apellido, edad, ciudad, documento, correo)
lista.append(persona)

print("Persona registrada correctamente.")