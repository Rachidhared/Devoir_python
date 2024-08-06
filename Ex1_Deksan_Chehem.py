# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def taillelim(lignes, colonnes, l_tresor, c_tresor):
    if l_tresor > lignes or l_tresor < 0 or c_tresor > colonnes or c_tresor < 0:
        print("erreur veuillez saisir un endroit valide")
    else:
        print("La position du trésor est bien une valeur correcte")
    return 0



def creer_grille(lignes, colonnes, l_tresor, c_tresor):
  
    grille = [['*' for _ in range(colonnes)] for _ in range(lignes)]
    
   
    if 0 <= l_tresor < lignes and 0 <= c_tresor < colonnes:
        grille[l_tresor][c_tresor] = 'T'
    else:
        print("Erreur : La position du trésor est en dehors des limites de la grille.")
        return None
    
    return grille

def afficher_grille(grille):
    if grille is None:
        return
    for ligne in grille:
        print(' '.join(ligne))

lignes = int(input("Quel est le nombre de lignes : "))
colonnes = int(input("Quel est le nombre de colonnes : "))

l_tresor = int(input("Quel est la ligne où le trésor est caché : "))
c_tresor = int(input("Quel est la colonne où le trésor est caché : "))

taillelim(lignes, colonnes, l_tresor, c_tresor)
grille = creer_grille(lignes, colonnes, l_tresor, c_tresor)
afficher_grille(grille)













