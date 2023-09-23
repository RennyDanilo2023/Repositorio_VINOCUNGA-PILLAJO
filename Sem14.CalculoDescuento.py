# -*- coding: utf-8 -*-

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento a aplicar (10% por defecto).
    :return: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llama a la función calcular_descuento proporcionando solo el monto total de la compra.
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

# Llama a la función calcular_descuento proporcionando tanto el monto total de la compra como el porcentaje de descuento.
monto_compra2 = 200
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Muestra los resultados de las llamadas a la función con el formato que mencionaste.
print("#LLAMADO 1; Llama a la función calcular_descuento proporcionando solo el monto total de la compra.")
print("Monto de compra 1: $", monto_compra1)
print("Descuento aplicado 1: $", descuento1)
print("Monto final 1 a pagar: $", monto_final1)
print("")
print("#LLAMADO 2; Llama a la función calcular_descuento proporcionando tanto el monto total de la compra como el porcentaje de descuento.")
print("Monto de compra 2: $", monto_compra2)
print("Descuento aplicado 2: $", descuento2)
print("Monto final 2 a pagar: $", monto_final2)