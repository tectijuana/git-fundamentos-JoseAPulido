# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:48:25 2023
imprimir una tabla de potencias de 2 que no exceda al 1000
@author: Flygo
"""
i = 0
while 2**i <= 1000:
    print("2^{} = {}".format(i, 2**i))
    i += 1
