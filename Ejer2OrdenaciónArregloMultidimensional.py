# -*- coding: utf-8 -*-

# Importar módulo random
import random

# Función para imprimir una matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print elemento, "\t",
        print

# Función para ordenar una fila con Bubble Sort
def ordenar_fila(matriz, fila):
    if fila < 0 or fila >= len(matriz):
        print "Fila no válida"
        return

    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Crear una matriz 3x3 con valores aleatorios
matriz = [[random.randint(1, 30) for _ in range(3)] for _ in range(3)]

# Imprimir la matriz original
print "Matriz Original:"
imprimir_matriz(matriz)

# Ordenar la segunda fila (recuerda que las filas se indexan desde 0)
ordenar_fila(matriz, 1)

# Imprimir la matriz con la fila ordenada
print "\nMatriz con la Fila 2 Ordenada:"
imprimir_matriz(matriz)
