# Taller_listas.py
# Script para procesar una lista de calificaciones y obtener métricas básicas.

def analizar_calificaciones(calificaciones):
    # Calcula el promedio aritmético dividiendo la suma total entre la cantidad de elementos.
    promedio = sum(calificaciones) / len(calificaciones)
    # Obtiene la calificación más alta de la lista.
    nota_mas_alta = max(calificaciones)
    # Obtiene la calificación más baja de la lista.
    nota_mas_baja = min(calificaciones)
    # Retorna una tupla con los tres valores calculados.
    return promedio, nota_mas_alta, nota_mas_baja


# Datos de prueba: lista de notas almacenadas en una estructura de tipo lista.
notas = [4.5, 3.8, 4.9, 2.7, 4.2]
# Invoca la función y guarda la tupla de resultados en la variable resultado.
resultado = analizar_calificaciones(notas)

# Muestra en consola la lista original y cada métrica calculada.
print("Calificaciones:", notas)
print("Promedio:", resultado[0])
print("Nota mas alta:", resultado[1])
print("Nota mas baja:", resultado[2])
