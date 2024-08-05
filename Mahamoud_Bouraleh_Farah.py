# Exercice 1 grille 
n = int(input("Saisir le nombre de lignes: "))
m = int(input("Saisir le nombre de colonnes: "))

for i in range(0, n):
    print()
    for j in range(0, m):
        print("*", end="")


el = int(input(" \n Saisir votre emplacement en ligne  : "))
ec = int(input("Saisir votre emplacement en  colonne : "))

if el > n or ec > m:
    print("Erreur d'emplacement")
else:
    
    for i in range(1, n):
        print()
        for j in range(1, m):
            if i == el and j == ec:
                print("T", end="")
            else:
                print("*", end="")

print("\nDevinez l'emplacement du trésor")
lg = int(input())
cl = int(input())

if lg == 4 and cl == 4:
    print("Vous êtes piégé")
else:
    if lg == el and cl == ec:
        print("Bravo")
    else:
        print("Désolé, vous n'avez pas trouvé le bon emplacement")


# Exercice 2  IMC 
def calculate_bmi():
    unit = input("Voulez-vous entrer les données en (K)ilogrammes et mètres ou en (L)ivres et pouces ? ").strip().upper()
    
    if unit == 'L':
        poid = float(input("Entrez votre poids en livres : "))
        taill = float(input("Entrez votre taille en pouces : "))
        
        poids = poid / 2.20462
        taille = taill * 0.0254
    elif unit == 'K':
        poids = float(input("Entrez votre poids en kilogrammes : "))
        taille = float(input("Entrez votre taille en mètres : "))
    else:
        print("L'unite que vous avez saisis est incorrecte. Veuillez entrer 'K' pour kilogrammes/mètres ou 'L' pour livres/pouces.")
        return
    
    bmi = poids / (taille ** 2)
    bmi_arrondi = round(bmi, 2)
    
    if bmi_arrondi < 18.5:
        category = "Insuffisance pondérale"
    elif 18.5 <= bmi_arrondi < 25:
        category = "Poids normal"
    elif 25 <= bmi_arrondi < 30:
        category = "Surpoids"
    else:
        category = "Obésité"
    
    print(f"Votre IMC est : {bmi_arrondi}")
    print(f"Catégorie : {category}")


calculate_bmi()


# Exercice 3 plindrome
import string

input_string = input("Entrez un mot ou une phrase : ")

input_string = input_string.lower()

processed_string = ''.join(char for char in input_string if char.isalnum())
left, right = 0, len(processed_string) - 1
is_palindrome_while = True
while left < right:
    if processed_string[left] != processed_string[right]:
        is_palindrome_while = False
        break
    left += 1
    right -= 1

is_palindrome_for = True
for i in range(len(processed_string) // 2):
    if processed_string[i] != processed_string[-(i + 1)]:
        is_palindrome_for = False
        break

print(f"Utilisation de la boucle while : {'C\'est un palindrome.' if is_palindrome_while else 'Ce n\'est pas un palindrome.'}")
print(f"Utilisation de la boucle for : {'C\'est un palindrome.' if is_palindrome_for else 'Ce n\'est pas un palindrome.'}")
