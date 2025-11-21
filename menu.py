
while True:
    print("----- Menú -----")
    print("1. Registrar persona")
    print("2. Consultar por documento")
    print("3. Salir")

    opcion = input("Ingresa la opción deseada: ")

    if opcion == "1":
        from persona import registrar
        registrar()

    elif opcion == "2":
        from consultar import buscar_documento
        buscar_documento()

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")

