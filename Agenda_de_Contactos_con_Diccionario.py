#Agenda de Contactos con Diccionario

agenda_contactos = {
    "Sebastian": "3027894567",
    "Maria": "3012345678",
    "Juan": "3009876543",
    "Ana": "3056789012",
    "Carlos": "3045678901",
    "Ivan": "3034567890",
    "Laura": "3067890123"
}

#añadir contacto
def agregar_contacto(nombre, numero):
    if nombre  in agenda_contactos or numero in agenda_contactos.values():
        print("El contacto ya existe en la agenda.")
    else:
        agenda_contactos[nombre] = numero
        print(f"Contacto {nombre} con número {numero} fue agregado exitosamente.")

#buscar contacto por su nombre
def buscar_contacto(nombre):
    if nombre in agenda_contactos:
        print(f"El número de {nombre} es: {agenda_contactos[nombre]}")
    else:
        print("El contacto no se encuentra en la agenda.")

#mostrar todos los contactos
def mostrar_contactos():
    if agenda_contactos:
        print("Agenda de Contactos:")
        for nombre, numero in agenda_contactos.items():
            print(f"{nombre}: {numero}")
    else:
        print("La agenda de contactos está vacía.")

#menú de opciones
while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")
#acciones según la opción seleccionada
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el número de teléfono del contacto: ")
            agregar_contacto(nombre, numero)
        case "2":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        case "3":
            mostrar_contactos()
        case "4":
            print("Saliendo de la agenda de contactos.")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")
