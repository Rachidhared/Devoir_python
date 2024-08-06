def calculate_bmi(weight, height):
    """Calculer l'IMC et le retourner arrondi à deux décimales."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def determine_category(bmi):
    """Déterminer la catégorie de l'IMC."""
    if bmi < 18.5:
        return "Insuffisance pondérale"
    elif 18.5 <= bmi < 25:
        return "Poids normal"
    elif 25 <= bmi < 30:
        return "Surpoids"
    else:
        return "Obésité"

def convert_pounds_to_kg(pounds):
    """Convertir les livres en kilogrammes."""
    return pounds / 2.20462

def convert_inches_to_meters(inches):
    """Convertir les pouces en mètres."""
    return inches / 39.3701

def main():
    # Demander à l'utilisateur le type d'entrée
    choice = input("Voulez-vous entrer votre poids en kilogrammes ou en livres ? (kg/lb): ").strip().lower()
    
    if choice == 'kg':
        weight = float(input("Entrez votre poids en kilogrammes : "))
        height = float(input("Entrez votre taille en mètres : "))
    elif choice == 'lb':
        pounds = float(input("Entrez votre poids en livres : "))
        weight = convert_pounds_to_kg(pounds)
        inches = float(input("Entrez votre taille en pouces : "))
        height = convert_inches_to_meters(inches)
    else:
        print("Choix invalide.")
        return
    
    # Calculer l'IMC
    bmi = calculate_bmi(weight, height)
    
    # Déterminer la catégorie
    category = determine_category(bmi)
    
    # Afficher les résultats
    print(f"Votre IMC est : {bmi}")
    print(f"Catégorie : {category}")

if __name__ == "__main__":
    main()
