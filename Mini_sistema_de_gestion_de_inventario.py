#ejercicio 5
#MIni sistema de gestion de inventario

inventario = [
    {"nombre": "Camiseta", "precio": 20000, "cantidad": 89},
    {"nombre": "Pantalon", "precio": 35700, "cantidad": 100},
    {"nombre": "Zapatos", "precio": 80000, "cantidad": 31}
]
#FUNCIONES PARA EL MENU
#agregar producto
def agregar_producto (nombre, precio, cantidad):
    for producto in inventario:
        if producto["nombre"].lower()==nombre.lower():
            print("el produccto ya existe ")
            break
    else:
        producto={"nombre": nombre , "precio": precio , "cantidad": cantidad}
        inventario.append(producto)
        print(f"producto {nombre} con precio {precio} y cantidad {cantidad} han sido agregados")

#realizar venta
def realizar_venta(nombre_producto, cantidad_a_vender):
    # Buscamos el producto en la lista
    for producto in inventario:
        # Usamos .lower() para que no importe si escriben con mayúsculas o minúsculas
        if producto["nombre"].lower() == nombre_producto.lower():
            
            # Verificar si hay suficiente stock
            if producto["cantidad"] >= cantidad_a_vender:
                # Restar la cantidad del inventario
                producto["cantidad"] -= cantidad_a_vender
                
                # Calcular el total
                total = producto["precio"] * cantidad_a_vender
                
                print(f"venta realizada, se vendieron {cantidad_a_vender}x {producto['nombre']}")
                print(f"costo total: ${total:.2f}")
                print(f"stock restante de {producto['nombre']}: {producto['cantidad']}")
                return 
            #caso en que no aya sufisiente stock    
            else:
                print(f" no hay suficiente stock. Solo quedan {producto['cantidad']} unidades")
                
                
    # Si el bucle termina y no encontró el producto
    print(f" el producto '{nombre_producto}' no existe en el inventario")

#mostrar inventario
def mostrar_inventario ():
    for producto in inventario:
        print(f"producto: {producto["nombre"]} precio: {producto["precio"]} cantidad disponible: {producto["cantidad"]} ")


#MENU INTERACTIVO
print("sistema de inventario")
while True:
    #opciones disponibles
    print("\n 1) agregar producto \n 2) realizar venta \n 3) mostrar inventario \n 4) salir" )
    opcion= input("ingresa una opcion (1-4): ")

    #verificar que opcion se tomo para saber que se devuelve
    match opcion:
        case "1":
            nombre=input("nombre del producto: ")
            precio=input("precio del producto: ")
            cantidad= input("cantidad del producto: ")
            agregar_producto(nombre, precio, cantidad)
        case "2":
            nombre=input("nombre del producto: ")
            cantidad= int(input("cantidad a vender: "))
            realizar_venta(nombre, cantidad)
        case "3":
            mostrar_inventario()
        case "4":
            print("gracias por usar el inventario")
            break