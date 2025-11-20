
while True :
    print("-----Menu-----")
    print("1.registrar")
    print("2.consultar")
    print("3.salir")


    opcion = input("ingresa la opcion deseada :")

    if opcion == "1":
        from practicas_datos.persona import Persona
        Persona(Persona)
    
    if opcion == "2":
        from consultar import Consultar
        Consultar(Persona)

    if opcion == "3": 
        print("saliendo del programa salir.")
    else :
        print("opcion no valida intenta de nuevo..")
