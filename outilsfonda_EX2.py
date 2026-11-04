from math import*
def diviseurs(n):
    liste = []
    for i in range(1, n + 1):
        if n % i == 0:
            liste.append(i)
    return liste

print(diviseurs(28))

def pgcd_naif(a, b):
    resultat = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            resultat = i
    return resultat

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
print(pgcd_naif(1071, 462))
print(pgcd(1071, 462))


import time

def mesurer():
    nombres = [10007, 100003, 1000003]

    for n in nombres:
        debut = time.time()
        pgcd_naif(n, 1)
        fin = time.time()
        print(n, fin - debut)

        debut = time.time()
        pgcd(n, 1)
        fin = time.time()
        print(n, fin - debut)

mesurer()

import time

def crible(n):
    premiers = [True] * n
    premiers[0] = False
    premiers[1] = False

    for i in range(2, n):
        if premiers[i]:
            for j in range(i * 2, n, i):
                premiers[j] = False

    compteur = 0
    for p in premiers:
        if p:
            compteur = compteur + 1

    return compteur

debut = time.time()
print(crible(100000))
print(time.time() - debut)

def facteurs(n):
    liste = []
    i = 2

    while n > 1:
        if n % i == 0:
            liste.append(i)
            n = n // i
        else:
            i = i + 1

    return liste

print(facteurs(360))

import time

def fib_recursif(n):
    if n <= 1:
        return n
    return fib_recursif(n-1) + fib_recursif(n-2)

def mesurer():
    for n in [20, 25, 30]:
        debut = time.time()
        fib_recursif(n)
        print(n, time.time() - debut)

mesurer()


def compte():
    compteur = {}
    fib_recursif(30, compteur)

    print(compteur[1])
    print(sum(compteur.values()))

compte()


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a

print(fibonacci(25))
print(fibonacci(10000))
print(len(str(fibonacci(10000))))



def euclide_etendu(a, b):
    if b == 0:
        return (a, 1, 0)

    g, u, v = euclide_etendu(b, a % b)

    return (g, v, u - (a // b) * v)

print(euclide_etendu(1071, 462))


