#ejercicio 4
#Conversor de Unidades

#proporciones de conversion para cada categoria
proporciones = {
    "distancia": {     
        "kilometros": 1000.0,
        "decimetros": 10.0,
        "metros": 1.0,
        "centimetros": 0.01,
        "milimetros": 0.001,
        #unidad estadounidense
        "millas": 1609.34,
        "yardas": 0.9144,
        "pies": 0.3048,
        "pulgadas": 0.0254
    },
    "masa": {
        "Kilogramos": 1.0,
        "gramos": 0.001,
        "miligramos": 0.000001,
        #unidad estadounidense
        "libras": 0.453592,
        "onzas": 0.0283495
    },
}

#funcion para la conversion de unidades
def conversor_unidades(valor, unidad_origen, unidad_destino, categoria):

    # Convertir el valor a la unidad base (metro para distancia, kilogramo para masa)
    valor_base = valor * proporciones[categoria][unidad_origen]    

    # Convertir el valor base a la unidad destino
    valor_destino= valor_base/float(proporciones[categoria][unidad_destino])
    return valor_destino

print("Bienvenido al sistema de conversión de unidades")

#ciclo para permitir al usuario realizar múltiples conversiones hasta que decida salir
while True:
#solicitar al usuario que ingrese la categoría, unidades y valor a convertir
    categoria= input("ingrsa una categoria (distancia o masa) o 'salir' para terminar: ").lower()

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
         
  #solicitar al usuario que ingrese las unidades de origen y destino, validando su existencia para la categoría seleccionada

    #imprimir lista de unidades de medida disponibles  dependiendo la categoria
    if categoria=="distancia":
        print("\n kilometros \n decimetros \n metros \n centimetros \n milimetros \n millas \n yardas \n pies \n pulgadas \n salir para terminar ")
    else:
        print("\n kilogramos \n gramos \n miligramos \n libras \n onzas \n salir para terminar ")
    #unidad de medida de origen
    unidad_origen = input("Ingrese la unidad de medida de origen: ").lower()
    if unidad_origen == "salir" :
        print("Gracias por usar el sistema de conversión de unidades.")
        break
    #validar si existe la opcion ingresada
    while unidad_origen not in proporciones[categoria]:
        print("Unidad no válida. Por favor, elige una unidad válida para la categoría.")
        unidad_origen = input("Ingrese la unidad de medida de origen : ").lower()
        if unidad_origen == "salir":
            print("Gracias por usar el sistema de conversión de unidades.")
            break
    #unidad de medida destino
    unidad_destino = input("Ingrese la unidad de medida de destino: ").lower()
    if unidad_destino == "salir":
        print("Gracias por usar el sistema de conversión de unidades.")
        break
    #validar si existe la opcion ingresada
    while unidad_destino not in proporciones[categoria]:
        print("Unidad no válida. Por favor, elige una unidad válida para la categoría.")
        unidad_destino = input("Ingrese la unidad de medida de destino (ej: metro): ").lower()
        if unidad_destino == "salir":
            print("Gracias por usar el sistema de conversión de unidades.")
            break

    #solicitar al usuario que ingrese el valor a convertir
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = conversor_unidades(valor, unidad_origen, unidad_destino, categoria) 
    if resultado is not None:
        print(f"{valor} {unidad_origen} son equivalentes a {resultado :.2f} {unidad_destino}.")

    #preguntar al usuario si desea realizar otra conversión o salir del programa
    respuesta = input("\n ¿Desea realizar otra conversión? (si/no): ")
    if respuesta.lower() != "si":
        print("Gracias por usar el sistema de conversión de unidades.")
        break