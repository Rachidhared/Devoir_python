#Exercice_2

def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    return round(imc, 2)
def categorie_sante(imc):
    if imc < 18.5:
        return "Insuffisance pondérale"
    elif 18.5 <= imc < 25:
        return "Poids normal"
    elif 25 <= imc < 30:
        return "Surpoids"
    else:
        return "Obésité"
def main():
    # Demander à l'utilisateur de choisir l'unité
    mode = input("Voulez-vous entrer votre poids et votre taille en (1) kilogrammes et mètres ou (2) livres et pouces ?: ")

    if mode == '1':
        poids = float(input("Entrez votre poids en kilogrammes : "))
        taille = float(input("Entrez votre taille en mètres : "))
    elif mode == '2':
        poids_lbs = float(input("Entrez votre poids en livres : "))
        taille_in = float(input("Entrez votre taille en pouces : "))

        # Conversion en kilogrammes et mètres
        poids = poids_lbs / 2.20462
        taille = taille_in / 39.3701
    else:
        print("Choix invalide.")
        return

    imc = calculer_imc(poids, taille)
    categorie = categorie_sante(imc)

    print(f"Votre IMC est : {imc}")
    print(f"Votre Catégorie de santé : {categorie}")


if __name__ == "__main__":
    main()
