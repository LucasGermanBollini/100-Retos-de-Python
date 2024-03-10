"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""
#Un número de n dígitos es un número de Armstrong si es igual a la suma de las n-ésimas potencias de sus dígitos.
#Por ejemplo: 8208 = 8^4 + 2^4 + 0^4 + 8^4

def numeroDeAmstrong(n):
    sumatoria = 0
    long = str(n)
    for i in range(len(long)):
        numero = int(long[i]) ** len(long)
        sumatoria = sumatoria + numero
    return sumatoria == n
    
print(numeroDeAmstrong(8208)) #Verdadero
print(numeroDeAmstrong(2015)) #Falso
print(numeroDeAmstrong(4210818)) #Verdadero
print(numeroDeAmstrong(115132219018763992565095597973971522401)) #Verdadero
print(numeroDeAmstrong(115132219018763992565095597973971522402)) #Falso

        
        
    
        