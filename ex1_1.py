import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def surface(self):
        """Retourne la surface du cercle."""
        return math.pi * self.rayon * self.rayon
    
    def perimetre(self):
        """Retourne le périmètre du cercle."""
        return 2 * math.pi * self.rayon

# Exemple d'utilisation
rayon_du_cercle = 10
mon_cercle = Cercle(rayon_du_cercle)

print("Rayon:", mon_cercle.rayon)
print("Surface:", mon_cercle.surface())
print("Périmètre:", mon_cercle.perimetre())
