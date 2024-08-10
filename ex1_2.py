class Calculatrice:
    def additionner(self, a, b):
        return a + b
    
    def soustraire(self, a, b):
        return a - b
    
    def multiplier(self, a, b):
        return a * b
    
    def diviser(self, a, b):
        if b == 0:
            return "Erreur : Division par zéro"
        return a / b

# Exemple d'utilisation
calc = Calculatrice()

print("Addition:", calc.additionner(10, 5))
print("Soustraction:", calc.soustraire(10, 5))
print("Multiplication:", calc.multiplier(10, 5))
print("Division:", calc.diviser(10, 5))
print("Division par zéro:", calc.diviser(10, 0))
