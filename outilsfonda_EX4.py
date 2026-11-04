def transposer(matrice):
    nb_lignes = len(matrice)
    nb_colonnes = len(matrice[0])
    transposee = []

    for colonne in range(nb_colonnes):
        elements = []
        for ligne in range(nb_lignes):
            elements += [matrice[ligne][colonne]]
        transposee += [elements]

    return transposee


print("Matrice transposée :", transposer([[1, 2, 3], [4, 5, 6]]))


def multiplication(A, B):
    lignes_A = len(A)
    colonnes_A = len(A[0])
    colonnes_B = len(B[0])

    resultat = [[0 for j in range(colonnes_B)] for i in range(lignes_A)]

    for ligne in range(lignes_A):
        for colonne in range(colonnes_B):
            valeur = 0
            for indice in range(colonnes_A):
                valeur += A[ligne][indice] * B[indice][colonne]
            resultat[ligne][colonne] = valeur

    return resultat


matrice_identite = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matrice_A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]

print("Résultat identique :", multiplication(matrice_A, matrice_identite) == matrice_A)


import random
import time


def creer_matrice(taille):
    resultat = []

    for ligne in range(taille):
        valeurs = []
        for colonne in range(taille):
            valeurs.append(random.random())
        resultat.append(valeurs)

    return resultat


for taille in [40, 80, 120]:
    premiere = creer_matrice(taille)
    seconde = creer_matrice(taille)

    temps_depart = time.perf_counter()
    multiplication(premiere, seconde)
    temps_fin = time.perf_counter()

    duree = temps_fin - temps_depart
    print("Dimension :", taille, "- Durée :", round(duree, 4), "secondes")


import numpy as np

dimension = 120
matrice_1 = creer_matrice(dimension)
matrice_2 = creer_matrice(dimension)

debut_python = time.perf_counter()
multiplication(matrice_1, matrice_2)
duree_python = time.perf_counter() - debut_python

tableau_1 = np.array(matrice_1)
tableau_2 = np.array(matrice_2)

debut_numpy = time.perf_counter()
calcul_numpy = np.dot(tableau_1, tableau_2)
duree_numpy = time.perf_counter() - debut_numpy

print("Durée Python :", round(duree_python, 4), "s")
print("Durée Numpy :", round(duree_numpy, 6), "s")
print("Facteur d'accélération :", round(duree_python / duree_numpy), "fois")


def resolution_systeme(matrice, second_membre, tolerance=1e-14):
    taille = len(matrice)
    tableau = []

    for i in range(taille):
        nouvelle_ligne = matrice[i].copy()
        nouvelle_ligne.append(second_membre[i])
        tableau.append(nouvelle_ligne)

    # Élimination de Gauss avec pivot partiel
    for colonne in range(taille):
        pivot = colonne

        for ligne in range(colonne + 1, taille):
            if abs(tableau[ligne][colonne]) > abs(tableau[pivot][colonne]):
                pivot = ligne

        if abs(tableau[pivot][colonne]) <= tolerance:
            print("Le système ne possède pas de solution unique.")
            return []

        tableau[colonne], tableau[pivot] = tableau[pivot], tableau[colonne]

        for ligne in range(colonne + 1, taille):
            coefficient = tableau[ligne][colonne] / tableau[colonne][colonne]

            for j in range(taille, colonne - 1, -1):
                tableau[ligne][j] -= coefficient * tableau[colonne][j]

    # Remontée
    solution = [0.0 for i in range(taille)]

    for ligne in range(taille - 1, -1, -1):
        resultat = tableau[ligne][taille]

        for colonne in range(ligne + 1, taille):
            resultat -= tableau[ligne][colonne] * solution[colonne]

        solution[ligne] = resultat / tableau[ligne][ligne]

    return solution


matrice_systeme = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
vecteur = [2, -1, 8]

solution = resolution_systeme(matrice_systeme, vecteur)
print("Valeurs obtenues :", solution)


dimension = 50
matrice_grande = creer_matrice(dimension)
second_membre = [random.random() for i in range(dimension)]

solution_personnelle = resolution_systeme(matrice_grande, second_membre)
solution_reference = np.linalg.solve(np.array(matrice_grande), np.array(second_membre))

difference = 0

for i in range(dimension):
    valeur_ecart = abs(solution_personnelle[i] - solution_reference[i])
    difference = max(difference, valeur_ecart)

print("Différence maximale :", difference)
print("Résultats proches :", difference < 1e-9)


def construire_hilbert(taille):
    H = []

    for i in range(taille):
        ligne = []
        for j in range(taille):
            terme = 1.0 / (i + j + 1)
            ligne.append(terme)
        H.append(ligne)

    return np.array(H)


dimension = 12
H = construire_hilbert(dimension)
solution_connue = np.ones(dimension)
second_membre = H.dot(solution_connue)

solution_directe = np.linalg.solve(H, second_membre)
solution_inverse = np.linalg.inv(H).dot(second_membre)

print("Erreur de la résolution :", float(np.max(np.abs(solution_directe - solution_connue))))
print("Erreur avec l'inverse :", float(np.max(np.abs(solution_inverse - solution_connue))))


def matrice_rotation(angle):
    cosinus = np.cos(angle)
    sinus = np.sin(angle)

    return np.array([[cosinus, -sinus],
                     [sinus, cosinus]])


rotation_1 = matrice_rotation(np.pi / 3)
rotation_2 = matrice_rotation(np.pi / 6)

composition = rotation_1 @ rotation_2
rotation_finale = matrice_rotation(np.pi / 2)

print("Même transformation :", np.allclose(composition, rotation_finale))


def calcul_determinant(matrice):
    taille = len(matrice)
    copie = [ligne.copy() for ligne in matrice]
    resultat = 1.0

    for colonne in range(taille):
        pivot = colonne

        for ligne in range(colonne + 1, taille):
            if abs(copie[ligne][colonne]) > abs(copie[pivot][colonne]):
                pivot = ligne

        if abs(copie[pivot][colonne]) < 1e-14:
            return 0.0

        if pivot != colonne:
            copie[colonne], copie[pivot] = copie[pivot], copie[colonne]
            resultat *= -1

        resultat *= copie[colonne][colonne]

        for ligne in range(colonne + 1, taille):
            facteur = copie[ligne][colonne] / copie[colonne][colonne]

            for j in range(colonne, taille):
                copie[ligne][j] -= facteur * copie[colonne][j]

    return resultat


matrice_determinant = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]

print("Calcul manuel :", calcul_determinant(matrice_determinant))
print("Calcul Numpy :", float(np.linalg.det(np.array(matrice_determinant, dtype=float))))


from fractions import Fraction


def hilbert_fraction(taille):
    resultat = []

    for i in range(taille):
        ligne = []

        for j in range(taille):
            fraction = Fraction(1, i + j + 1)
            ligne.append(fraction)

        resultat.append(ligne)

    return resultat


dimension = 12
matrice_fraction = hilbert_fraction(dimension)

vecteur_exact = []

for ligne in matrice_fraction:
    total = sum(ligne)
    vecteur_exact.append(total)

solution_fraction = resolution_systeme(matrice_fraction, vecteur_exact, tolerance=0)

print("Solution obtenue avec les fractions :", solution_fraction)


def matrice_translation(decalage_x, decalage_y):
    return np.array([[1.0, 0.0, decalage_x],
                     [0.0, 1.0, decalage_y],
                     [0.0, 0.0, 1.0]])


def rotation_homogene(angle):
    cosinus = np.cos(angle)
    sinus = np.sin(angle)

    return np.array([[cosinus, -sinus, 0.0],
                     [sinus, cosinus, 0.0],
                     [0.0, 0.0, 1.0]])


point_initial = np.array([1.0, 0.0, 1.0])

deplacement = matrice_translation(3, 1)
rotation = rotation_homogene(np.pi / 2)

premier_ordre = rotation @ deplacement @ point_initial
second_ordre = deplacement @ rotation @ point_initial

print("Déplacement puis rotation :", np.round(premier_ordre, 10))
print("Rotation puis déplacement :", np.round(second_ordre, 10))
