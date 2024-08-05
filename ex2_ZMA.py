def calculate_bmi(poids, taille):
  """
  Calcule l'IMC d'une personne.

  Args:
      poids: Le poids de la personne en kilogrammes.
      taille: La taille de la personne en mètres.

  Returns:
      La valeur de l'IMC calculée arrondie à deux décimales.
  """
  imc = poids / (taille ** 2)
  return round(imc, 2)

poids = float(input("Entrez votre poids en kilogrammes: "))
taille = float(input("Entrez votre taille en mètres: "))

imc = calculate_bmi(poids, taille)

print("Votre IMC est:", imc)

if imc < 18.5:
  print("Insuffisance pondérale")
elif 18.5 <= imc <= 24.9:
  print("Poids normal")
elif 25 <= imc <= 29.9:
  print("Surpoids")
else:
  print("Obésité")

print("\nDéfi Bonus:")
poids_livres = float(input("Entrez votre poids en livres: "))
taille_pouces = float(input("Entrez votre taille en pouces: "))

poids_kg = poids_livres / 2.20462
taille_m = taille_pouces / 39.3701

imc = calculate_bmi(poids_kg, taille_m)

print("Votre IMC est:", imc)

if imc < 18.5:
  print("Insuffisance pondérale")
elif 18.5 <= imc <= 24.9:
  print("Poids normal")
elif 25 <= imc <= 29.9:
  print("Surpoids")
else:
  print("Obésité")