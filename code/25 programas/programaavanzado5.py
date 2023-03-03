# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:27:54 2023
un trabajo x dura 30 dias y se paga 10 diarios y otro lo pagan 1 el primer dia, 2 el segundo dia y asi sucesivamente, cual es el mejor pagado
@author: Flygo
"""
# Calcular el ingreso total del primer trabajo
ingreso_primer_trabajo = 10 * 30

# Calcular el ingreso total del segundo trabajo
ingreso_segundo_trabajo = sum([i for i in range(1, 31)])

# Comparar los ingresos totales
if ingreso_primer_trabajo > ingreso_segundo_trabajo:
    print("El primer trabajo es mejor pagado.")
else:
    print("El segundo trabajo es mejor pagado.")

