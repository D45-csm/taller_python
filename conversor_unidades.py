#ejercicio 4
#Conversor de Unidades

#proporciones de conversion para cada categoria
proporciones = {
    "distancia": {     
        "kilometro": 1000.0,
        "decimetro": 10.0,
        "metro": 1.0,
        "centimetro": 0.01,
        "milimetro": 0.001,
        #unidad estadounidense
        "milla": 1609.34,
        "yarda": 0.9144,
        "pie": 0.3048,
        "pulgada": 0.0254
    },
    "masa": {
        "kilogramo": 1.0,
        "gramo": 0.001,
        "miligramo": 0.000001,
        #unidad estadounidense
        "libra": 0.453592,
        "onzas": 0.0283495
    },
}

#funcion para la conversion de unidades
def conversor_unidades(valor, unidad_origen, unidad_destino, categoria):
    if categoria not in proporciones:
        print("Categoría no válida. Por favor, elige 'distancia' o 'masa'.")
        return None
    
    if unidad_origen not in proporciones[categoria] or unidad_destino not in proporciones[categoria]:
        print("Unidad no válida. Por favor, elige unidades válidas para la categoría.")
        return None
    # Convertir el valor a la unidad base (metro para distancia, kilogramo para masa)
    valor_base = valor * proporciones[categoria][unidad_origen]    
    # Convertir el valor base a la unidad destino
    valor_destino= valor_base/float(proporciones[categoria][unidad_destino])
    return valor_destino

print("Bienvenido al sistema de conversión de unidades")

#ciclo para permitir al usuario realizar múltiples conversiones hasta que decida salir
while True:
    #solicitar al usuario que ingrese la categoría, unidades y valor a convertir
    categoria= input("ingrsa una categoria (distancia o masa) o 'salir' para terminar: ")
    #verificar si el usuario desea salir antes de continuar con la conversión
    if categoria == "salir":
        print("Gracias por usar el sistema de conversión de unidades.")
        break
    #validar si la categoría ingresada por el usuario existe
    while categoria != "distancia" and categoria != "masa":
         print("Categoría no válida. Por favor, elige 'distancia' o 'masa' o 'salir'.")
         categoria= input("ingrsa una categoria (distancia o masa) o 'salir' para terminar: ")
         if categoria == "salir":
            print("Gracias por usar el sistema de conversión de unidades.")
            break
         
    #solicitar al usuario que ingrese las unidades de origen y destino, validando que sean válidas para la categoría seleccionada
    unidad_origen = input("Ingrese la unidad de medida de origen (ej: kilometro) o 'salir' para terminar: ")
    if unidad_origen == "salir" :
        print("Gracias por usar el sistema de conversión de unidades.")
        break

    while unidad_origen not in proporciones[categoria]:
        print("Unidad no válida. Por favor, elige una unidad válida para la categoría.")
        unidad_origen = input("Ingrese la unidad de medida de origen (ej: kilometro): ")
        if unidad_origen == "salir":
            print("Gracias por usar el sistema de conversión de unidades.")
            break
    
    unidad_destino = input("Ingrese la unidad de medida de destino (ej: metro) o 'salir' para terminar: ")
    if unidad_destino == "salir":
        print("Gracias por usar el sistema de conversión de unidades.")
        break

    while unidad_destino not in proporciones[categoria]:
        print("Unidad no válida. Por favor, elige una unidad válida para la categoría.")
        unidad_destino = input("Ingrese la unidad de medida de destino (ej: metro): ")
        if unidad_destino == "salir":
            print("Gracias por usar el sistema de conversión de unidades.")
            break

    #solicitar al usuario que ingrese el valor a convertir
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = conversor_unidades(valor, unidad_origen, unidad_destino, categoria) 
    if resultado is not None:
        print(f"{valor} {unidad_origen} son equivalentes a {resultado} {unidad_destino}.")
    #preguntar al usuario si desea realizar otra conversión o salir del programa
    respuesta= input(f"\n ¿Desea realizar otra conversión? (si/no): ")
    if respuesta.lower() != "si":
        print("Gracias por usar el sistema de conversión de unidades.")
        break