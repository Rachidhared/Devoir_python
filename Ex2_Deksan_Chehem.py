# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:27:01 2024

@author: HASNA
"""

def calculate_bmi(taille,poids):
    IMC=poids/(taille**2)
    if imc < 18.5:
        return "Insuffisance pondérale"
    elif 18.5 <= imc < 25:
        return "Poids normal"
    elif 25 <= imc < 30:
        return "Surpoids"
    else:
        return "Obésité"
    return round(IMC,2)

poids=int(input("quel est votre poids"))
taille=int(input("quel est votre taille"))

calculate_bmi(taille,poids)