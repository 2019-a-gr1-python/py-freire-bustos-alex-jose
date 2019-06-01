#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:14:25 2019

@author: usrdel
"""

print("Hola")

nombre = "Adrian"
edad = 29

print(nombre)


import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

numeros_serie_a = pd.Series(lista_numeros)
numeros_serie_b = pd.Series(tupla_numeros)
numeros_serie_c = pd.Series(np_numeros)
numeros_serie_d = pd.Series([
        True,
        False,
        12,
        12.21,
        "Asad",
        None,
        (),
        [],
        {"nombre":"Adrian"}])

numeros_serie_a[0]

lista_ciudades = ["Ambato","Cuenca","Loja",
                  "Quito"]
serie_ciudades = pd.Series(lista_ciudades,
                           index=["A","C","L",
                                  "Q"])
serie_ciudades["Q"]
serie_ciudades[0]
serie_ciudades[1]
serie_ciudades[2]
serie_ciudades[3]

print(type(serie_ciudades))

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }
serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[0]


ciudades_menores_5000 = serie_valor_ciudad == 3300

serie_menor_5000 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = 8750


print("Lima" in serie_valor_ciudad)  # False
print("Loja" in serie_valor_ciudad)  # True


np.square(serie_valor_ciudad)
np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
            "Loja":4000,
            "Guayaquil":10000
        })

ciudades_dos = pd.Series({
            "Montañita":300,
            "Guayaquil":10000,
            "Quito":2000
        })

print(ciudades_uno * ciudades_dos)


randomico = np.random.rand(3)

serie_tres_rand = pd.Series(randomico)

ciudades_uno.index

# Concatenar series

ciudades_uno = pd.Series({
            "Loja":4000,
            "Guayaquil":10000
        })

ciudades_dos = pd.Series({
            "Montañita":300,
            "Guayaquil":10000,
            "Quito":2000
        })

# Suma los valores
ciudades_add = ciudades_uno.add(ciudades_dos)


ciudades_uno = pd.Series({
            "Loja":4000,
            "Guayaquil":1200,
            "Quito":3000
        })

ciudades_dos = pd.Series({
            "Montañita":300,
            "Guayaquil":10000,
            "Quito":2000
        })


ciudades_concat = pd.concat([ciudades_uno,
                            ciudades_dos])

ciudades_concat_v = pd.concat([ciudades_uno,
                            ciudades_dos],
                verify_integrity=True)


ciudades_append = ciudades_uno.append(ciudades_dos)
# Anadir un indice valor a una serie

# Maximo

ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)
# Minimo

ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

# Estadisticas (Avg Mean ...)
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

# Primer (5)
ciudades_uno.head(2)

# Ultimos (5)
ciudades_uno.tail(2)

ciudades_uno.sort_values().head(2)
ciudades_uno.sort_values().tail(2)

ciudades_uno.sort_values(ascending = False).head(2)
ciudades_uno.sort_values(ascending = False).tail(2)


# 0 >= 1000      5%
# 1000 >= 10000  10%
# 10000 >        15%

def calculo(valor):
    if(valor <=1000):
        return valor * 1.05
    if(valor >1000 and valor <= 10000):
        return valor * 1.10
    if(valor >10000):
        return valor * 1.15

ciudades_uno.map(calculo)


ciudad_uno.where(ciudad_uno > 1000,ciudad_uno * 1.05 )

#
#





























