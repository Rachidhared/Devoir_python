def calculate_bmi(poids, taille):
    return round(poids / (taille ** 2), 2)

def main():
    poids = float(input("Entrez votre poids en kilogrammes: "))
    taille = float(input("Entrez votre taille en mètres: "))
    
    imc = calculate_bmi(poids, taille)
    print(f"Votre IMC est: {imc}")
    
    if imc < 18.5:
        print("Catégorie: Insuffisance pondérale")
    elif 18.5 <= imc < 25:
        print("Catégorie: Poids normal")
    elif 25 <= imc < 30:
        print("Catégorie: Surpoids")
    else:
        print("Catégorie: Obésité")

    choix = input("Voulez-vous entrer les mesures en livres et pouces? (oui/non): ").lower()
    if choix == 'oui':
        poids_lb = float(input("Entrez votre poids en livres: "))
        taille_in = float(input("Entrez votre taille en pouces: "))
        
        poids_kg = poids_lb / 2.20462
        taille_m = taille_in / 39.3701
        
        imc = calculate_bmi(poids_kg, taille_m)
        print(f"Votre IMC est: {imc}")
        
        if imc < 18.5:
            print("Catégorie: Insuffisance pondérale")
        elif 18.5 <= imc < 25:
            print("Catégorie: Poids normal")
        elif 25 <= imc < 30:
            print("Catégorie: Surpoids")
        else:
            print("Catégorie: Obésité")

if __name__ == "__main__":
    main()
