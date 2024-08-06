import re


def est_palindrome_while(chaine):
   
    chaine_nettoyee = re.sub(r'[^A-Za-z0-9]', '', chaine).lower()
    gauche = 0
    droite = len(chaine_nettoyee) - 1
    
    while gauche < droite:
        if chaine_nettoyee[gauche] != chaine_nettoyee[droite]:
            return False
        gauche += 1
        droite -= 1
    return True


def est_palindrome_for(chaine):
    chaine_nettoyee = re.sub(r'[^A-Za-z0-9]', '', chaine).lower() 
    for i in range(len(chaine_nettoyee) // 2):
        if chaine_nettoyee[i] != chaine_nettoyee[-(i + 1)]:
            return False
    return True
def principal():
    chaines_test = [
        "Un radar",
        "Élu par cette crapule",
        "Un bon snob nu",
        "Pas un palindrome"
    ]
    
    for c in chaines_test:
        print(f"Test de: {c}")
        print(f"Vérification avec while: {'Palindrome' if est_palindrome_while(c) else 'Pas un palindrome'}")
        print(f"Vérification avec for: {'Palindrome' if est_palindrome_for(c) else 'Pas un palindrome'}")
        print()

if __name__ == "__main__":
    principal()
