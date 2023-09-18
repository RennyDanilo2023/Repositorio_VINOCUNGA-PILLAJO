# -*- coding: utf-8 -*-

# Crear matriz de datos
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 72},
            {"day": "Martes", "temp": 74},
            {"day": "Miércoles", "temp": 76},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 85}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 82},
            {"day": "Domingo", "temp": 87}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 79},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 88}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 77},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 81},
            {"day": "Domingo", "temp": 86}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 84},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 88},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 76}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 83},
            {"day": "Martes", "temp": 86},
            {"day": "Miércoles", "temp": 87},
            {"day": "Jueves", "temp": 84},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 75}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 85},
            {"day": "Martes", "temp": 88},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 86},
            {"day": "Viernes", "temp": 83},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 77}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 82},
            {"day": "Martes", "temp": 85},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 83},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 74}
        ]
    ]
]

# Calcular promedios por semana
promedios_por_semana = []
for ciudad in temperaturas:
    promedios_ciudad = []
    for semana in ciudad:
        suma_temperaturas = 0
        for dia in semana:
            suma_temperaturas += dia["temp"]
        promedio_semana = suma_temperaturas / len(semana)
        promedios_ciudad.append(promedio_semana)

    promedios_por_semana.append(promedios_ciudad)

# Calcular promedios totales por ciudad
for i, promedios_ciudad in enumerate(promedios_por_semana):
    suma = 0
    for promedio_semana in promedios_ciudad:
        suma += promedio_semana
    promedio_total = suma / len(promedios_ciudad)

    print("Promedio ciudad {}: {}".format(i + 1, promedio_total))

