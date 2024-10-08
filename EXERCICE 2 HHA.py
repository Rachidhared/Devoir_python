# -*- coding: utf-8 -*-
"""hassan houssein .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fWjpuCbbrSZOyOz2czf3o2VVrEuxk06m

## **Exerce 2**
"""

def calculate_bmi(poids, taille):
    """Calculer l'Indice de Masse Corporelle (IMC)."""
    return round(poids / (taille ** 2), 2)

def afficher_categorie(imc):
    """Afficher la catégorie de santé en fonction de l'IMC."""
    if imc < 18.5:
        return "Insuffisance pondérale"
    elif 18.5 <= imc < 24.9:
        return "Poids normal"
    elif 25 <= imc < 29.9:
        return "Surpoids"
    else:
        return "Obésité"

def main():
    print("Choisissez le mode d'entrée :")
    print("1. Poids en kilogrammes et taille en mètres")
    print("2. Poids en livres et taille en pouces")

    mode = input("Entrez '1' ou '2' : ")

    if mode == '1':
        poids = float(input("Entrez votre poids en kilogrammes : "))
        taille = float(input("Entrez votre taille en mètres : "))
    elif mode == '2':
        poids_livres = float(input("Entrez votre poids en livres : "))
        taille_pouces = float(input("Entrez votre taille en pouces : "))

        # Conversion en kilogrammes et mètres
        poids = poids_livres / 2.20462
        taille = taille_pouces / 39.3701
    else:
        print("Mode non valide. Utilisation du mode par défaut (kilogrammes et mètres).")
        poids = float(input("Entrez votre poids en kilogrammes : "))
        taille = float(input("Entrez votre taille en mètres : "))

    # Calculer l'IMC
    imc = calculate_bmi(poids, taille)

    # Afficher le résultat
    print(f"Votre IMC est {imc}.")
    print(f"Catégorie : {afficher_categorie(imc)}")

if __name__ == "__main__":
    main()
