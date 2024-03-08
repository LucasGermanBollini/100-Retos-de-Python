"""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
 """

def palindromo(text):
    text = text.lower()
    text = list(text)
    for i in range(len(text)-1,0,-1):
        #Signos de puntuacion, se pueden agregar mas para mejorar el programa
        if "." == text[i] or " " == text[i] or "," == text[i] or "?" == text[i]:
            text.remove(text[i])
    textNueva = text[::-1]
    print(text == textNueva)

palindromo("Ana lleva al oso la avellana")#Es palindromo
palindromo("Anita lava la tina.")#Es palindromo
palindromo("La ruta natural.")#Es palindromo
palindromo("Ana lava llaves.")#No es palindromo
palindromo("La luz del sol es algo hermoso.")#No es palindromo
    