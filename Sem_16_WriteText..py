# -*- coding: utf-8 -*-

# Abre el archivo en modo escritura (w)
with open('my_notes.txt', 'w') as archivo:
    # Escribe las notas personales en el archivo
    archivo.write("Nota 1: Este es un deber de FUNDAMENTOS DE PROGRAMACION (A) -- UEA-L-UFB-026-A .\n")
    archivo.write("Nota 2: La tarea pertenece a la (Semana 16) Tarea: Trabajo con Archivos de Texto en Python\n")
    archivo.write("Nota 3: La tarea fue elaborado por el Ing. VINOCUNGA-PILLAJO\n")

# Abre el archivo en modo lectura (r)
with open('my_notes.txt', 'r') as archivo:
    print("Contenido del archivo my_notes.txt:")
    # Lee el contenido línea por línea
    for linea in archivo.readlines():
        # Imprime cada línea en la consola
        print(linea.strip())  # strip() elimina los saltos de línea al final de cada línea
