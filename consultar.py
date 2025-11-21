from persona import lista

class buscar_documento():

    buscar = input("Ingresa el número de documento: ").strip()

    for persona in lista:
        if persona.documento == buscar:
            print("Documento encontrado:")
            persona.datos_persona()
    print("Documento no encontrado.")


