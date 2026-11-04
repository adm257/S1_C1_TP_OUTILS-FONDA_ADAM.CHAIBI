import math

def creer_vecteur(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return (dx, dy)

def scalaire(vecteur1, vecteur2):
    resultat = vecteur1[0] * vecteur2[0]
    resultat += vecteur1[1] * vecteur2[1]
    return resultat

def longueur(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

def calcul_angle(v1, v2):
    valeur = scalaire(v1, v2) / (longueur(v1) * longueur(v2))
    
    valeur = max(-1.0, min(1.0, valeur))
    
    return math.degrees(math.acos(valeur))

print("Longueur du vecteur :", longueur((3, 4)))
print("Scalaire :", scalaire((1, 2), (3, 4)))
print("Premier angle :", calcul_angle((1, 0), (1, 1)))
print("Deuxième angle :", calcul_angle((1, 0), (0, 1)))
print("Troisième angle :", calcul_angle((2, 0), (2, 0)))

def calcul_determinant(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def distance_droite(point, debut, fin):
    direction = creer_vecteur(debut, fin)
    position = creer_vecteur(debut, point)
    
    determinant_val = abs(calcul_determinant(direction, position))
    longueur_droite = longueur(direction)
    
    return determinant_val / longueur_droite


d1 = distance_droite((0, 0), (0, 1), (1, 0))
attendu = math.sqrt(2) / 2

print("\nPremière distance :", d1, "| Valeur attendue :", attendu)

d2 = distance_droite((3, 4), (0, 0), (1, 0))
print("Deuxième distance :", d2)


def sens_rotation(A, B, C):
    vecteur_AB = creer_vecteur(A, B)
    vecteur_AC = creer_vecteur(A, C)
    
    valeur = calcul_determinant(vecteur_AB, vecteur_AC)
    
    if valeur > 0:
        return 1
    
    if valeur < 0:
        return -1
    
    return 0


print("\nSens 1 :", sens_rotation((0, 0), (1, 0), (1, 1)))
print("Sens 2 :", sens_rotation((0, 0), (1, 0), (1, -1)))
print("Sens 3 :", sens_rotation((0, 0), (1, 1), (2, 2)))


def calcul_aire(sommets):
    total = 0
    nombre_points = len(sommets)
    
    for indice in range(nombre_points):
        point_actuel = sommets[indice]
        point_suivant = sommets[(indice + 1) % nombre_points]
        
        total += point_actuel[0] * point_suivant[1]
        total -= point_suivant[0] * point_actuel[1]
        
    return abs(total) * 0.5


polygone_carre = [(0, 0), (1, 0), (1, 1), (0, 1)]
polygone_triangle = [(0, 0), (4, 0), (0, 3)]
polygone_maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]

print("\nSurface du carré :", calcul_aire(polygone_carre))
print("Surface du triangle :", calcul_aire(polygone_triangle))
print("Surface de la maison :", calcul_aire(polygone_maison))


def segments_croises(A, B, C, D):
    signe1 = sens_rotation(A, B, C)
    signe2 = sens_rotation(A, B, D)
    signe3 = sens_rotation(C, D, A)
    signe4 = sens_rotation(C, D, B)
    
    return signe1 * signe2 < 0 and signe3 * signe4 < 0


print("\nPremier croisement :", segments_croises((0, 0), (1, 1), (0, 1), (1, 0)))
print("Deuxième croisement :", segments_croises((0, 0), (1, 0), (0, 1), (1, 1)))
print("Troisième croisement :", segments_croises((0, 0), (1, 1), (2, 2), (3, 3)))


def trouver_intersection(A, B, C, D):
    direction1 = creer_vecteur(A, B)
    direction2 = creer_vecteur(C, D)
    
    denominateur = calcul_determinant(direction1, direction2)
    
    if denominateur == 0:
        return None
    
    ecart = creer_vecteur(A, C)
    
    parametre1 = calcul_determinant(ecart, direction2) / denominateur
    parametre2 = calcul_determinant(ecart, direction1) / denominateur
    
    if 0 <= parametre1 <= 1 and 0 <= parametre2 <= 1:
        abscisse = A[0] + parametre1 * direction1[0]
        ordonnee = A[1] + parametre1 * direction1[1]
        
        return (abscisse, ordonnee)
    
    return None


print("\nPremière intersection :", trouver_intersection((0, 0), (2, 2), (0, 2), (2, 0)))
print("Deuxième intersection :", trouver_intersection((0, 0), (1, 0), (0, 1), (1, 1)))
print("Troisième intersection :", trouver_intersection((0, 0), (1, 1), (2, 2), (3, 3)))


def dedans(point, forme):
    px, py = point
    nombre_sommets = len(forme)
    resultat = False
    
    for indice in range(nombre_sommets):
        premier = forme[indice]
        second = forme[(indice + 1) % nombre_sommets]
        
        x1, y1 = premier
        x2, y2 = second
        
        if (y1 > py) != (y2 > py):
            abscisse_intersection = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            
            if px < abscisse_intersection:
                resultat = not resultat
    
    return resultat


print("\nVérification de l'appartenance à la maison :")

liste_points = [(1, 1), (1, 2.4), (3, 1), (0.2, 2.2)]

for point in liste_points:
    print("Point :", point, "-> À l'intérieur :", dedans(point, polygone_maison))
