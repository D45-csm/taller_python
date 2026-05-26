# Taller2_listas.py
# Programa interactivo para gestionar una lista de compras usando una estructura tipo lista.

# Inicializa una lista vacía donde se almacenarán los productos ingresados por el usuario.
lista_compras = []

# Bucle infinito que mantiene el menú activo hasta que el usuario decida salir.
while True:
    # Muestra las opciones disponibles del menú principal.
    print("\n--- MENU LISTA DE COMPRAS ---")
    print("1. Agregar item a la lista")
    print("2. Eliminar item de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")

    # Captura la opción seleccionada por el usuario.
    opcion = input("Elige una opcion: ")

    # Opción 1: agregar un nuevo elemento al final de la lista.
    if opcion == "1":
        item = input("Escribe el item que deseas agregar: ")
        lista_compras.append(item)
        print(f'"{item}" fue agregado a la lista.')

    # Opción 2: eliminar un elemento existente de la lista.
    elif opcion == "2":
        # Valida primero si la lista está vacía para evitar operaciones innecesarias.
        if len(lista_compras) == 0:
            print("La lista está vacía, no hay nada para eliminar.")
        else:
            item = input("Escribe el item que deseas eliminar: ")
            # Verifica si el elemento existe antes de intentar removerlo.
            if item in lista_compras:
                lista_compras.remove(item)
                print(f'"{item}" fue eliminado de la lista.')
            else:
                print("Ese item no está en la lista.")

    # Opción 3: mostrar el contenido completo de la lista.
    elif opcion == "3":
        # Si no hay elementos, informa al usuario que la lista está vacía.
        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            print("\nTu lista de compras:")
            # Recorre la lista con enumerate para imprimir un índice y el valor de cada elemento.
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")

    # Opción 4: finaliza la ejecución del programa.
    elif opcion == "4":
        print("Saliendo del programa...")
        break

    # Manejo de entradas inválidas fuera del rango definido en el menú.
    else:
        print("Opción inválida. Intenta de nuevo.")
