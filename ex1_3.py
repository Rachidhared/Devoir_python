from datetime import datetime

class Personne:
    def __init__(self, nom, pays, date_de_naissance):
        self.nom = nom
        self.pays = pays
        self.date_de_naissance = datetime.strptime(date_de_naissance, '%Y-%m-%d')
    
    def calculer_age(self):
        aujourd_hui = datetime.now()
        age = aujourd_hui.year - self.date_de_naissance.year - ((aujourd_hui.month, aujourd_hui.day) < (self.date_de_naissance.month, self.date_de_naissance.day))
        return age
    
    def __str__(self):
        return (f"Nom: {self.nom}, "
                f"Pays: {self.pays}, "
                f"Date de Naissance: {self.date_de_naissance.strftime('%d-%m-%Y')}, "
                f"Âge: {self.calculer_age()} ans")

# Exemple d'utilisation
personne1 = Personne("Zack Muse", "Djibouti", "1999-07-23")
print(personne1)
