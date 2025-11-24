from gestionar_p import registrar
from gestionar_p import buscar_documento
from gestionar_p import modificar_persona
from gestionar_p import eliminar_persona

while True:
    print("----- MENÚ -----")
    print("1. Registrar persona")
    print("2. Consultar persona por documento")
    print("3. Modificar persona")
    print("4. Eliminar persona")
    print("5. Salir")

    opcion = input("Ingresa la opción deseada: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        buscar_documento()
    elif opcion == "3":
        modificar_persona()
    elif opcion == "4":
        eliminar_persona()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print(" Opción no válida, intenta de nuevo.")
