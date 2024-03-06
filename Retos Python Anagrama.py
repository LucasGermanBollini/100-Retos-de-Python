"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def anagrama(palabra1,palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    respuesta = False
    errorEncontrado = 0
    if palabra1 == palabra2:
        respuesta = False
    else:
        if len(palabra1) == len(palabra2):
            for i in range(len(palabra1)):
                if palabra1[i] in palabra2:
                    respuesta = True
                    palabra2.remove(palabra1[i])
                else:
                    errorEncontrado = 1
        if errorEncontrado == 1:
            respuesta = False
    return respuesta

print(anagrama("dnfxg","sdngf"))
print(anagrama("dnfxg", "sdngf"))  
print(anagrama("listen", "silent"))  
print(anagrama("triangle", "integral")) 
print(anagrama("hello", "world"))  
print(anagrama("Astronomer", "Moon starer"))  
print(anagrama("debit card", "bad credit"))  
print(anagrama("abc", "def")) 
print(anagrama("rail safety", "fairy tales")) 
print(anagrama("12345", "54321")) 
print(anagrama("python", "java"))  
print(anagrama("The Morse Code!", "Here come dots"))       
            
#Otra forma de hacerlo utilizando sort()

def anagrama(palabra1,palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    if palabra1 == palabra2:
        return False
    palabra1.sort()
    palabra2.sort()
    return palabra1 == palabra2

print()
print("Prueba del segundo codigo empieza aca: ")
print()
print(anagrama("dnfxg","sdngf"))
print(anagrama("dnfxg", "sdngf"))  
print(anagrama("listen", "silent"))  
print(anagrama("triangle", "integral")) 
print(anagrama("hello", "world"))  
print(anagrama("Astronomer", "Moon starer"))  
print(anagrama("debit card", "bad credit"))  
print(anagrama("abc", "def")) 
print(anagrama("rail safety", "fairy tales")) 
print(anagrama("12345", "54321")) 
print(anagrama("python", "java"))  
print(anagrama("The Morse Code!", "Here come dots"))       
            
