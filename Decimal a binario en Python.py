"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
 """
import random

def decimalAbinario(decimal):
    binario = []
    while decimal != 0:
        if decimal % 2 == 0:
            binario.append(0)
            decimal = decimal // 2
        else:
            binario.append(1)
            decimal = decimal // 2
    binario.reverse()
    binario = "".join(map(str,binario))
    return binario

#5 casos random para testear
ejemplo = random.randint(5,9999)
print(f"{ejemplo} = {decimalAbinario(ejemplo)}")
ejemplo = random.randint(5,9999)
print(f"{ejemplo} = {decimalAbinario(ejemplo)}")
ejemplo = random.randint(5,9999)
print(f"{ejemplo} = {decimalAbinario(ejemplo)}")
ejemplo = random.randint(5,9999)
print(f"{ejemplo} = {decimalAbinario(ejemplo)}")
ejemplo = random.randint(5,9999)
print(f"{ejemplo} = {decimalAbinario(ejemplo)}")



                