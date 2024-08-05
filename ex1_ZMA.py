import random

def creer_plateau(n, m):
    """Crée un plateau de jeu de taille n x m rempli d'astérisques."""
    plateau = []
    for i in range(n):
        ligne = ["*"] * m
        plateau.append(ligne)
    return plateau

def choisir_emplacement(n, m):
    """Demande au joueur de choisir un emplacement valide pour le trésor."""
    while True:
        ligne = int(input(f"Choisissez une ligne pour le trésor (1-{n}) : ")) - 1
        colonne = int(input(f"Choisissez une colonne pour le trésor (1-{m}) : ")) - 1
        if 0 <= ligne < n and 0 <= colonne < m:
            return ligne, colonne
        else:
            print("Emplacement invalide. Veuillez entrer des coordonnées valides.")

def placer_tresor_et_piege(plateau, ligne_tresor, colonne_tresor):
    """Place le trésor et un piège aléatoire sur le plateau."""
    plateau[ligne_tresor][colonne_tresor] = "T"

    while True:
        ligne_piege = random.randint(0, len(plateau) - 1)
        colonne_piege = random.randint(0, len(plateau[0]) - 1)
        if (ligne_piege, colonne_piege) != (ligne_tresor, colonne_tresor):
            plateau[ligne_piege][colonne_piege] = "X"
            break

def afficher_plateau(plateau):
    """Affiche le plateau de jeu."""
    for ligne in plateau:
        print(" ".join(ligne))

if __name__ == "__main__":
    n = int(input("Entrez le nombre de lignes pour le plateau de jeu : "))
    m = int(input("Entrez le nombre de colonnes pour le plateau de jeu : "))

    plateau = creer_plateau(n, m)

    ligne_tresor, colonne_tresor = choisir_emplacement(n, m)
    placer_tresor_et_piege(plateau, ligne_tresor, colonne_tresor)

    print("\nVoici votre plateau de jeu :")
    afficher_plateau(plateau)