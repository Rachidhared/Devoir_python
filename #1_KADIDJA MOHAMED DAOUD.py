#Exercice_1

import random
def creer_plateau(n, m):
    # Crée un plateau de n x m avec des '*'
    return [['*' for _ in range(m)] for _ in range(n)]

def afficher_plateau(plateau):
    # Affiche le plateau
    for ligne in plateau:
        print(' '.join(ligne))
    print()

def placer_trésor(plateau, ligne, colonne):
    plateau[ligne][colonne] = 'T'

def placer_piège(plateau, ligne_trésor, colonne_trésor):
    n = len(plateau)
    m = len(plateau[0])
    while True:
        ligne_piège = random.randint(0, n - 1)
        colonne_piège = random.randint(0, m - 1)
        if (ligne_piège, colonne_piège) != (ligne_trésor, colonne_trésor):
            plateau[ligne_piège][colonne_piège] = 'X'
            break
def deviner_emplacement(plateau, ligne, colonne):
    if plateau[ligne][colonne] == 'T':
        return "Félicitations ! Vous avez trouvé le trésor !"
    elif plateau[ligne][colonne] == 'X':
        return "Oh non ! Vous êtes tombé dans un piège !"
    else:
        return "Essayez à nouveau !"

def main():
    # Demander la taille du plateau
    n = int(input("Entrez le nombre de lignes du plateau : "))
    m = int(input("Entrez le nombre de colonnes du plateau : "))

    # Créer le plateau
    plateau = creer_plateau(n, m)

    # Demander l'emplacement du trésor
    while True:
        try:
            ligne_trésor = int(input("Entrez la ligne pour cacher le trésor (0 à {}): ".format(n - 1)))
            colonne_trésor = int(input("Entrez la colonne pour cacher le trésor (0 à {}): ".format(m - 1)))
            if 1 <= ligne_trésor < n and 1 <= colonne_trésor < m:
                break
            else:
                print("Emplacement invalide.. Veuillez réessayer !")
        except ValueError:
            print("Veuillez entrer des nombres valides !")

    # Placer le trésor
    placer_trésor(plateau, ligne_trésor, colonne_trésor)

    # Placer le piège
    placer_piège(plateau, ligne_trésor, colonne_trésor)

    # Afficher le plateau
    afficher_plateau(plateau)

    # Demander au joueur de deviner l'emplacement du trésor
    while True:
        try:
            ligne_devine = int(input("Devinez la ligne du trésor (0 à {}): ".format(n - 1)))
            colonne_devine = int(input("Devinez la colonne du trésor (0 à {}): ".format(m - 1)))
            if 0 <= ligne_devine < n and 0 <= colonne_devine < m:
                break
            else:
                print("Emplacement invalide.. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer des nombres valides !!")

    # Vérifie la devinette
    resultat = deviner_emplacement(plateau, ligne_devine, colonne_devine)
    print(resultat)

# Exécute le jeu de chasse au Tresor
if __name__ == "__main__":
    main()
