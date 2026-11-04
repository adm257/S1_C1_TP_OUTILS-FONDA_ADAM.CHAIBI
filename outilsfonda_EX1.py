nb= 2026
b= 7
q= n// b
r= n % b
print(q,r)
print(q* b + r)


dc = 123456789 % 10  #


sdc = 123456789 // 10  

print(dc, sdc)

res = 0


for i in range(1000):
    res += 0.1

ecart = res - 100

print(res)
print(ecart)


def presque_egaux(a, b):
    to = 0.000000009
    return abs(a - b) < to

print(0.1 + 0.2 == 0.3)
print(presque_egaux(0.1 + 0.2, 0.3))


for i in range(1, 11):
    produit = 7 * i
    print("7 x", i, "=", produit)


somme = 0
for i in range(1, 101):
    somme = somme + i

n = 100
resu = n * (n + 1) // 2

print("Somme boucle :", somme)
print("Somme formule :", resu)

def nombre_de_chiffres(n):
    c = 0
    if n == 0:
        return 1
    while n > 0:
        n = n // 10
        c = c + 1
    return c

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))

import math

def heron(a, tolerance=1e-12):
    """Racine carrée de a par la méthode de Héron."""
    
    if a < 0:
        
        raise ValueError("pas de racine carrée réelle pour un nombre négatif")
    
    if a == 0:
        
        return 0.0
    
    x = float(a)
    
    tours = 0
    
    while True:
        
        suivant = 0.5 * (x + a / x)
        
        tours = tours + 1
        
        if abs(suivant - x) <= tolerance * abs(suivant):
            
            return suivant
        
        x = suivant

print(heron(2))
print(math.sqrt(2))
print(abs(heron(2) - math.sqrt(2)) < 1e-12)



def vers_binaire(n):
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        r = n % 2
        res = str(r) + res
        n = n // 2
    return res

print(vers_binaire(37))
print(vers_binaire(0))


import sys

eps = 1.0
while 1.0 + eps / 2 != 1.0:
    
eps = eps / 2

print(eps)
print(sys.float_info.epsilon)
print(eps == 2 ** -52)
