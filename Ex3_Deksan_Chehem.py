# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:49:38 2024

@author: HASNA
"""



def palindrome(chaine):
    if chaine==chaine[::-1]:
        print("bon")
    else:
        print ('faux')


chaine=str(input("quel est votre mot"))

palindrome(chaine)


