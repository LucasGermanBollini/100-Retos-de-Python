"""
/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
 """

def divisoresYmultiplos(a,b):
    encontrado = False
    multiplosA = []
    multiplosB = []
    MCD = "No Existe"
    MCM = "No Existe"
    #Maximo comun divisor
    for i in range(9,0,-1):
        if encontrado != True:
            if a%i==0 and b%i==0:
                MCD = i
                encontrado = True
    encontrado = False
    #Minimo comun multiplo
    for i in range(9):
        multiplosA.append(a*i)
        multiplosB.append(b*i)
    for i in range(8,0,-1):
        if multiplosA[i] in multiplosB:
            MCM = multiplosA[i]
    return f"El minimo comun multiplo es: {MCM} \nEl maximo comun divisor es: {MCD}"

print(divisoresYmultiplos(6,8))
                    
        