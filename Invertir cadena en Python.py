"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

def invertirCadenas(text):
    text = list(text)
    invertido = []
    restar = 1
    for i in range(len(text)):
        invertido.append(text[len(text)-restar])
        restar = restar + 1
    invertido = "".join(invertido)
    return invertido

print(invertirCadenas("Hola me llamo lucas"))