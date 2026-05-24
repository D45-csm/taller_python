# Taller_listas.py

def analizar_calificaciones(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    nota_mas_alta = max(calificaciones)
    nota_mas_baja = min(calificaciones)
    return promedio, nota_mas_alta, nota_mas_baja


# Prueba de la función
notas = [4.5, 3.8, 4.9, 2.7, 4.2]
resultado = analizar_calificaciones(notas)

print("Calificaciones:", notas)
print("Promedio:", resultado[0])
print("Nota más alta:", resultado[1])
print("Nota más baja:", resultado[2])
