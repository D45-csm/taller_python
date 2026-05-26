# Taller2_listas.py
# Lista de compras interactiva

lista_compras = []
# Menu interactivo  
while True:
    print("\n--- MENÚ LISTA DE COMPRAS ---")
    print("1. Agregar ítem a la lista")
    print("2. Eliminar ítem de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")
    #ingreso de opcion 
    opcion = input("Elige una opción: ")

    #accion de cada opcion 
    if opcion == "1":
        item = input("Escribe el ítem que deseas agregar: ")
        lista_compras.append(item)
        print(f'"{item}" fue agregado a la lista.')

    elif opcion == "2":
        if len(lista_compras) == 0:
            print("La lista está vacía, no hay nada para eliminar.")
        else:
            item = input("Escribe el ítem que deseas eliminar: ")
            if item in lista_compras:
                lista_compras.remove(item)
                print(f'"{item}" fue eliminado de la lista.')
            else:
                print("Ese ítem no está en la lista.")

    elif opcion == "3":
        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            print("\nTu lista de compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
