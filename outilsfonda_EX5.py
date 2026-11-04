
def convertir_lettre(lettre):
    return ord(lettre) - 65


def convertir_nombre(valeur):
    return chr((valeur % 26) + 65)


print("Valeur de C :", convertir_lettre("C"))
print("Lettre correspondant à 2 :", convertir_nombre(2))


import unicodedata


def preparer_texte(chaine):
    decomposition = unicodedata.normalize("NFD", chaine)
    resultat = ""

    for caractere in decomposition:
        if unicodedata.category(caractere) != "Mn":
            lettre = caractere.upper()

            if lettre >= "A" and lettre <= "Z":
                resultat += lettre

    return resultat


print("Résultat du nettoyage :", preparer_texte("Été, à Paris !"))


def codage_affine(chaine, coefficient, decalage):
    texte = preparer_texte(chaine)
    code = ""

    for lettre in texte:
        position = convertir_lettre(lettre)
        nouvelle_position = (coefficient * position + decalage) % 26
        code += convertir_nombre(nouvelle_position)

    return code


texte_initial = "ATTAQUEALAUBE"

print("Résultat affine :", codage_affine(texte_initial, 5, 8))
print("Résultat César :", codage_affine(texte_initial, 1, 3))


def calcul_pgcd(x, y):
    while y > 0:
        x, y = y, x % y

    return x


coefficients_valides = []

for valeur in range(1, 26):
    if calcul_pgcd(valeur, 26) == 1:
        coefficients_valides += [valeur]


print("Coefficients autorisés :", coefficients_valides)
print("Total des coefficients :", len(coefficients_valides))


def trouver_inverse(valeur, modulo):
    valeur = valeur % modulo

    for nombre in range(modulo):
        if (valeur * nombre) % modulo == 1:
            return nombre

    raise ValueError("Aucun inverse pour " + str(valeur) + " modulo " + str(modulo))


print("Inverse de 5 :", trouver_inverse(5, 26))

try:
    trouver_inverse(4, 26)
except ValueError as probleme:
    print("Erreur prévue :", probleme)


def decoder_affine(chaine, coefficient, decalage):
    inverse = trouver_inverse(coefficient, 26)
    texte = preparer_texte(chaine)
    resultat = ""

    for caractere in texte:
        position = convertir_lettre(caractere)
        position_initiale = inverse * (position - decalage)
        resultat += convertir_nombre(position_initiale)

    return resultat


message_clair = preparer_texte("Attaque a l aube")
message_code = codage_affine(message_clair, 5, 8)

print("Texte codé :", message_code)
print("Texte retrouvé :", decoder_affine(message_code, 5, 8))

print("Correspondance :", decoder_affine(message_code, 5, 8) == message_clair)


try:
    decoder_affine(message_code, 4, 7)
except ValueError as probleme:
    print("Clé incorrecte :", probleme)


def tester_cles(texte_code):
    possibilites = []

    for coefficient in coefficients_valides:
        for decalage in range(26):
            clair = decoder_affine(texte_code, coefficient, decalage)
            possibilites.append((coefficient, decalage, clair))

    return possibilites


liste_essais = tester_cles(message_code)

print("Nombre de combinaisons :", len(liste_essais))

for coefficient, decalage, clair in liste_essais:
    if clair == message_clair:
        print("Clé retrouvée : a =", coefficient, "et b =", decalage)


texte_analyse = preparer_texte(
    "Le chiffrement affine est un chiffrement par substitution monoalphabetique. "
    "Chaque lettre du message est remplacee par une autre lettre, toujours la meme, "
    "ce qui laisse intactes les frequences relatives des lettres et permet de casser "
    "le code sans essayer toutes les clefs possibles."
)

texte_chiffre = codage_affine(texte_analyse, 7, 12)


compteur = {}

for caractere in texte_chiffre:
    if caractere not in compteur:
        compteur[caractere] = 1
    else:
        compteur[caractere] += 1


lettre_max = ""
effectif_max = 0

for caractere, effectif in compteur.items():
    if effectif > effectif_max:
        effectif_max = effectif
        lettre_max = caractere


print("Lettre dominante :", lettre_max)


position_frequente = convertir_lettre(lettre_max)
hypotheses = []

for coefficient in coefficients_valides:
    decalage = (position_frequente - 4 * coefficient) % 26
    texte_possible = decoder_affine(texte_chiffre, coefficient, decalage)

    hypotheses.append((coefficient, decalage, texte_possible))


print("Nombre d'hypothèses :", len(hypotheses))

for coefficient, decalage, clair in hypotheses:
    if clair[:13] == "LECHIFFREMENT":
        print("Clé identifiée : a =", coefficient, ", b =", decalage)
        print("Texte obtenu :", clair[:60])


import random


def calculer_IC(chaine):
    longueur = len(chaine)

    if longueur < 2:
        return 0

    repetitions = {}

    for caractere in chaine:
        repetitions[caractere] = repetitions.get(caractere, 0) + 1

    total = 0

    for nombre in repetitions.values():
        total += nombre * (nombre - 1)

    return total / (longueur * (longueur - 1))


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
texte_aleatoire = ""

for indice in range(len(texte_analyse)):
    texte_aleatoire += random.choice(alphabet)


print("IC du message initial :", round(calculer_IC(texte_analyse), 4))
print("IC du message affine :", round(calculer_IC(texte_chiffre), 4))
print("IC du message aléatoire :", round(calculer_IC(texte_aleatoire), 4))


def coder_vigenere(chaine, cle):
    message = preparer_texte(chaine)
    cle_preparee = preparer_texte(cle)

    resultat = ""
    taille_cle = len(cle_preparee)

    for indice in range(len(message)):
        valeur_message = convertir_lettre(message[indice])
        valeur_cle = convertir_lettre(cle_preparee[indice % taille_cle])

        resultat += convertir_nombre(valeur_message + valeur_cle)

    return resultat


code_vigenere = coder_vigenere(texte_analyse, "CLE")

print("Début du chiffrement Vigenère :", code_vigenere[:40])
print("Indice de coïncidence Vigenère :", round(calculer_IC(code_vigenere), 4))


for longueur_cle in range(1, 8):
    total_indices = 0

    for depart in range(longueur_cle):
        groupe = ""

        for indice in range(depart, len(code_vigenere), longueur_cle):
            groupe += code_vigenere[indice]

        total_indices += calculer_IC(groupe)
    indice_moyen = total_indices / longueur_cle
    print("Taille de clé :", longueur_cle,
          "-> Indice moyen :", round(indice_moyen, 4))
