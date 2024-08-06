import random

def create_board(n, m):
    return [['*' for _ in range(m)] for _ in range(n)]

def display_board(board):
    for row in board:
        print(' '.join(row))

def place_treasure(board, x, y):
    board[x][y] = 'T'

def place_trap(board, n, m):
    while True:
        trap_x = random.randint(0, n - 1)
        trap_y = random.randint(0, m - 1)
        if board[trap_x][trap_y] != 'T':
            board[trap_x][trap_y] = 'X'
            break

def main():
    n = int(input("Entrez le nombre de lignes: "))
    m = int(input("Entrez le nombre de colonnes: "))
    
    board = create_board(n, m)
    
    while True:
        try:
            treasure_x = int(input(f"Entrez la ligne (0-{n-1}) pour cacher le trésor: "))
            treasure_y = int(input(f"Entrez la colonne (0-{m-1}) pour cacher le trésor: "))
            if 0 <= treasure_x < n and 0 <= treasure_y < m:
                break
            else:
                print("Coordonnées invalides, veuillez réessayer.")
        except ValueError:
            print("Entrée invalide, veuillez entrer des nombres.")
    
    place_treasure(board, treasure_x, treasure_y)
    place_trap(board, n, m)
    
    display_board(board)

    while True:
        try:
            guess_x = int(input(f"Devinez la ligne (0-{n-1}): "))
            guess_y = int(input(f"Devinez la colonne (0-{m-1}): "))
            if guess_x == treasure_x and guess_y == treasure_y:
                print("Félicitations! Vous avez trouvé le trésor!")
                break
            elif board[guess_x][guess_y] == 'X':
                print("Oh non! Vous êtes tombé dans un piège!")
                break
            else:
                print("Essayez encore!")
        except ValueError:
            print("Entrée invalide, veuillez entrer des nombres.")

if __name__ == "__main__":
    main()
