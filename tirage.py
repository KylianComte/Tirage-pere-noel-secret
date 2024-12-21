# Tirage de pere noel secret by Kylian COMTE #

import random

liste_donneurs = ["Kylian","Rayan","Mathieu","Martin","Youssef","Mathis","Arno","Mael","Corentin","Quentin"]

liste_receveurs = liste_donneurs.copy()
random.shuffle(liste_receveurs)

nok = True

while nok:
    nok = False
    for i in range(len(liste_donneurs)):
        if liste_donneurs[i] == liste_receveurs[i]:
            nok = True
            random.shuffle(liste_receveurs)
            break

for i in range(len(liste_donneurs)):
    with open(f"{liste_donneurs[i]}.txt", "w") as file:
        file.write(f"Ton cadeau ira à {liste_receveurs[i]}")
