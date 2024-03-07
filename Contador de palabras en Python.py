"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
 """


def contadorPalabras(text):
    text = text.lower()
    text = text.split(" ")
    text.sort()
    listadoPalabras = []
    contador = 1
    detenerse = 0
    for i in range(len(text)):
        if text[i] not in listadoPalabras:
            if i != 0:
                listadoPalabras.append(contador)
                contador = 1
            listadoPalabras.append(text[i])
        else:
            contador = contador + 1
            
    #Este apartado es solo para calcular las veces que aparece la ultima palabra en el texto
    contador = 1
    j = len(text)
    while detenerse != 1:
        if text[j-1] == text[j-2]:
            contador = contador + 1
            j = j - 1
        else:
            detenerse = 1
    listadoPalabras.append(contador)
        
    while listadoPalabras != []:
        print(f"La palabra '{listadoPalabras[0]}' aparece {listadoPalabras[1]} vez/veces dentro del texto.")
        del listadoPalabras[1]
        del listadoPalabras[0]
        
        
        
        
        
        
contadorPalabras("La cantidad que existe de estrellas en el mundo es practicamente infinita, pero lo que poca gente sabe es que este texto no sirve leerlo por completo ya que no tiene sentido")