#ejercicio 5
#MIni sistema de gestion de inventario

inventario = [
    {"nombre": "Camiseta", "precio": 20000, "cantidad": 89},
    {"nombre": "Pantalón", "precio": 35700, "cantidad": 100},
    {"nombre": "Zapatos", "precio": 80000, "cantidad": 31}
]

#agregar producto
def agregar_producto (nombre, precio, cantidad):
    if nombre in inventario:
        print("el producto ya existe en el inventario")
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
                
                print(f"¡Venta exitosa! Se vendieron {cantidad_a_vender}x {producto['nombre']}.")
                print(f"Total a pagar: ${total:.2f}")
                print(f"Stock restante de {producto['nombre']}: {producto['cantidad']}")
                return  # Salimos de la función porque la venta ya se hizo
            else:
                print(f"Error: No hay suficiente stock. Solo quedan {producto['cantidad']} unidades.")
                return
                
    # Si el bucle termina y no encontró el producto
    print(f"Error: El producto '{nombre_producto}' no existe en el inventario.")


#mostrar inventario
def mostrar_inventario ():
    for producto in inventario:
        print(f"producto: {producto["nombre"]} precio: {producto["precio"]} cantidad disponible: {producto["cantidad"]} ")

#menu interactivo
print("sistema de inventario")
while True:
    #opciones disponibles
    print(f"\n 1) agregar producto \n 2) realizar venta \n 3) mostrar inventario \n 4) salir" )
    opcion= input("ingresa una opcion (1-4): ")

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




