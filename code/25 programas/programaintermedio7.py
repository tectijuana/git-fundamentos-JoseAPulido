# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:06:07 2023
convertir numeros romanos a arabigos
@author: Flygo
"""
def roman_to_arabic(roman_numeral):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic_num = 0
    prev_digit = 0
    for digit in roman_numeral[::-1]:
        if roman_dict[digit] >= prev_digit:
            arabic_num += roman_dict[digit]
        else:
            arabic_num -= roman_dict[digit]
        prev_digit = roman_dict[digit]
    return arabic_num

roman_numeral = input("Ingrese un número romano: ")
arabic_num = roman_to_arabic(roman_numeral)
print("El número romano", roman_numeral, "es equivalente a", arabic_num, "en arábigo")

