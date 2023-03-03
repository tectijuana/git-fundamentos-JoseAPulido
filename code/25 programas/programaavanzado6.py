# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:29:46 2023
usted tiene 100 y los invierte al 6% de intereses compuestos trimestrales cuantos años transcurriran hasta que tenga 50000
@author: Flygo
"""
import math

principal = 100
tasa_interes_anual = 0.06
composicion_interes = 4
monto_final = 50000

t = (1/composicion_interes) * math.log(monto_final/principal) / math.log(1 + tasa_interes_anual/composicion_interes)

print("Tardará", round(t, 2), "años para alcanzar un monto de", monto_final)

