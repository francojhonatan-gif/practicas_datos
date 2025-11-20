lista=[]

class Personas :
    def __init__(self,nombre,apellido,edad,ciudad,documento,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.ciudad = ciudad
        self.correo = correo
    
    def datos_persona(self):
        print("nombre :", self.nombre)
        print("apellido :", self.apellido)
        print("edad :" , self.edad)
        print("documento :", self.documento)
        print("ciudad :" , self.ciudad)
        print("correo :" , self.correo)

    def persona_registrada():
        if len(lista) == 0:
            print("No hay personas registradas.")
        else:
            print("Personas registradas:")
        for p in lista:
            p.datos_persona()
            print()

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
documento = str(input("Ingresa el número de identificación: "))
ciudad = input("Ingresa la ciudad: ")
correo = input("Ingresa tu correo: ")
                
persona = Personas(nombre, apellido, edad, ciudad, documento, correo)

lista.append(persona)

persona.datos_persona()

Personas.persona_registrada()


