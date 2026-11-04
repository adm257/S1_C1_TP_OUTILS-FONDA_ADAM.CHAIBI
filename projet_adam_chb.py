import random


def creer_route(nombre_cases, nombre_voitures):
    route = [0] * nombre_cases

    for i in range(nombre_voitures):
        position = random.randint(0, nombre_cases - 1)

        while route[position] != 0:
            position = random.randint(0, nombre_cases - 1)

        route[position] = random.randint(1, 5)

    return route



def calculer_vitesse(route):
    nouvelle_route = route.copy()
    taille = len(route)

    for i in range(taille):
        if route[i] != 0:
            distance = 0


            while distance < taille - 1:
                distance = distance + 1
                position = (i + distance) % taille

                if route[position] != 0:
                    break


            vitesse = min(route[i] + 1, 5)

            if distance <= vitesse:
                vitesse = distance - 1

            nouvelle_route[i] = vitesse

    return nouvelle_route


def avancer_voitures(route):
    taille = len(route)
    nouvelle_route = [0] * taille

    for i in range(taille):
        if route[i] != 0:
            position = (i + route[i]) % taille
            nouvelle_route[position] = route[i]

    return nouvelle_route



def simuler(route, nombre_tours):
    for tour in range(nombre_tours):
        route = calculer_vitesse(route)
        route = avancer_voitures(route)

    return route



def vitesse_moyenne(route):
    total = 0
    nombre = 0

    for vitesse in route:
        if vitesse != 0:
            total = total + vitesse
            nombre = nombre + 1

    if nombre == 0:
        return 0

    return total / nombre


def compter_arrets(route):
    total = 0

    for vitesse in route:
        if vitesse == 1:
            total = total + 1

    return total


def afficher_route(route):
    texte = ""

    for vitesse in route:
        if vitesse == 0:
            texte = texte + ". "
        else:
            texte = texte + "V "

    print(texte)


def programme():
    nombre_cases = 50
    nombre_voitures = 20
    nombre_tours = 30

    route = creer_route(nombre_cases, nombre_voitures)

    print("Situation initiale :")
    afficher_route(route)

    for tour in range(nombre_tours):
        route = calculer_vitesse(route)
        route = avancer_voitures(route)

        print("Tour", tour + 1)
        afficher_route(route)
        print("Vitesse moyenne :", round(vitesse_moyenne(route), 2))
        print("Voitures a l'arret :", compter_arrets(route))
        print()

programme()

