import numpy as np

def crear_tabla():
    # Inicializar una lista para almacenar los datos
    datos = []

    # Solicitar al usuario que ingrese los elementos por columna
    for j in range(3):  # 3 columnas
        columna = []
        for i in range(4):  # 4 filas
            elemento = input(f"Ingrese el elemento para la posición ({i+1},{j+1}): ")
            columna.append(elemento)
        datos.append(columna)

    # Transponer los datos para que se muestre en formato 4x3
    tabla = np.array(datos).T  # Transponer para que las filas y columnas se intercambien

    return tabla

def eliminar_columna(tabla):
    # Mostrar la tabla actual
    print("\nTabla actual:")
    print(tabla)
    
    # Pedir al usuario que elija una columna para eliminar
    while True:
        try:
            columna_a_eliminar = int(input("Ingrese el número de la columna a eliminar (1-3): ")) - 1
            if columna_a_eliminar in [0, 1, 2]:
                break
            else:
                print("Número de columna inválido. Debe ser entre 1 y 3.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
    
    # Eliminar la columna seleccionada
    nueva_tabla = np.delete(tabla, columna_a_eliminar, axis=1)
    
    return nueva_tabla

# Crear y mostrar la tabla
tabla = crear_tabla()

# Eliminar una columna y mostrar la nueva tabla
tabla_actualizada = eliminar_columna(tabla)
print("\nTabla actualizada:")
print(tabla_actualizada)