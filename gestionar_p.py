from persona import lista, Registrar_personas

from persona import lista

def registrar():
    print("--- Registro de Persona ---")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Ingresa tu edad: "))
    documento = input("Ingresa el número de identificación: ")
    ciudad = input("Ingresa tu ciudad: ")
    correo = input("Ingresa tu correo: ")

    persona = Registrar_personas(nombre, apellido, edad, ciudad, documento, correo)
    lista.append(persona)

    print(" Persona registrada correctamente")

def buscar_documento():
    print("--- Consultar Persona ---")
    buscar = input("Ingresa el número de documento: ")

    for persona in lista:
        if persona.documento == buscar:
            print("Persona encontrada:")
            persona.datos_persona()
            print()
            return

    print("Documento no encontrado.")


def eliminar_persona():
    print("--- Eliminar Persona ---")
    doc = input("Ingresa el número de documento de la persona a eliminar: ")

    for persona in lista:
        if persona.documento == doc:
            print("Persona encontrada:")
            persona.datos_persona()
            confirm = input("\n¿Deseas eliminarla? (s/n): ").lower()
            if confirm == "s":
                lista.remove(persona)
                print("Persona eliminada correctamente\n")
            else:
                print(" Eliminación cancelada\n")
            return

    print(" Persona no encontrada.")


def modificar_persona():
    print("--- Modificar Persona ---")
    doc = input("Ingresa el número de documento de la persona a modificar: ")

    for persona in lista:
        if persona.documento == doc:
            print("Persona encontrada:")
            persona.datos_persona()
            print("¿Qué deseas modificar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Edad")
            print("4. Ciudad")
            print("5. Correo")
            opcion = input("Selecciona opción: ")

            if opcion == "1":
                persona.nombre = input("Nuevo nombre: ")
            elif opcion == "2":
                persona.apellido = input("Nuevo apellido: ")
            elif opcion == "3":
                persona.edad = int(input("Nueva edad: "))
            elif opcion == "4":
                persona.ciudad = input("Nueva ciudad: ")
            elif opcion == "5":
                persona.correo = input("Nuevo correo: ")
            else:
                print(" Opción inválida")
                return

            print(" Persona modificada correctamente:")
            persona.datos_persona()
            print()
            return

    print(" Persona no encontrada.")