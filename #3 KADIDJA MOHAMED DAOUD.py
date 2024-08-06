#Exercice_3

import re
def nettoyer_chaine(input_string: str) -> str:
    # Utilise une expression régulière pour garder seulement les caractères alphanumériques
    return re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()

def is_palindrome_while(input_string: str) -> bool:
    # Nettoyer la chaîne d'entrée
    nettoyage_chaine = nettoyer_chaine(input_string)
    gauche = 0
    droite = len(nettoyage_chaine) - 1

    while gauche < droite:
        if nettoyage_chaine[gauche] != nettoyage_chaine[droite]:
            return False
        gauche += 1
        droite -= 1

    return True
def is_palindrome_for(input_string: str) -> bool:
    # Nettoyer la chaîne d'entrée
    nettoyage_chaine = nettoyer_chaine(input_string)

    for i in range(len(nettoyage_chaine) // 2):
        if nettoyage_chaine[i] != nettoyage_chaine[len(nettoyage_chaine) - 1 - i]:
            return False

    return True

# Tests des fonctions
exemples = [
    "A man, a plan, a canal, Panama",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon",
    "Hello, World!",
    "Madam, in Eden, I'm Adam"
]

for exemple in exemples:
    print(f"'{exemple}' est un palindrome (while): {is_palindrome_while(exemple)}")
    print(f"'{exemple}' est un palindrome (for): {is_palindrome_for(exemple)}")
