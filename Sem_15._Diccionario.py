# -*- coding: utf-8 -*-

# Crear el diccionario de información personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Ciudad A",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Ciudad B"

# Agregar una nueva clave-valor para representar la "profesion"
informacion_personal["profesion"] = "Desarrollador"

# Verificar si la clave "telefono" existe y, si no existe, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
