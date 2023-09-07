def buscar_valor(matriz, valor_a_buscar):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                return f"El valor {valor_a_buscar} se encontró en la posición ({i}, {j})."
    return f"El valor {valor_a_buscar} no se encontró en la matriz."

# Definimos una matriz de ejemplo (3x3)
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que queremos buscar en la matriz
valor_buscar = 5

# Llamamos a la función de búsqueda e imprimimos el resultado
resultado = buscar_valor(matriz_ejemplo, valor_buscar)
print(resultado)

