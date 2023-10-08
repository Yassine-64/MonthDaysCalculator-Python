
mois = int(input("Veuillez entrer le numéro d'un mois de 1 à 12 : "))


if mois in [1, 3, 5, 7, 8, 10, 12]:
    nbr_jours = 31
elif mois in [4, 6, 9, 11]:
    nbr_jours = 30
elif mois == 2:
    nbr_jours = 28

print("Le mois", mois, "a", nbr_jours, "jours.")
