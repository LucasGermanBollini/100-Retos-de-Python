"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

def numPrimos(n):
    error = True
    for i in range(2,9):
        if n % i == 0 or n == 1:
            error = False
    if n == 2 or n == 3 or n == 5 or n == 7:
        error = True
    return error

for j in range(1,101):
    if numPrimos(j) == True:
        print(j)
    