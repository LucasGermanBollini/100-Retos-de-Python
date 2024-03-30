'''/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
 '''

def buscarIguales(a1,a2,v):
    same = []
    notSame = []
    if len(a1) > len(a2):
        mc,mg = a2,a1
    else:
        mc,mg = a1,a2
    print(a1,a2)
    for j in range(len(mg)):
        for i in range(len(mc)):
            if a1[i] == a2[j]:
                if a1[i] not in same:
                    same.append(a[i])
    for i in range(len(mg)):
        if mg[i] not in mc:
            if mg[i] not in notSame:
                notSame.append(mg[i])
    
    return same if v == True else notSame
            
        
    
        
    
            
    
a = [9,10,4,2,4,1]
b = [6,8,4,3,10,9,2,1,3,4,5]
v = True

print(buscarIguales(a,b,v))
                
        
        
    