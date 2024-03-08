"""
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
 """

def traductorMorse(text):
    text = text.lower()
    text = list(text)
    morseTradu = []
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',' ']
    morse = ['· —', '— · · ·', '— · — ·', '— · ·', '·', '· · — ·', '— — ·', '· · · ·', '· ·', '· — — —', '— · —', '· — · ·', '— —', '— ·', '— — —', '· — — ·', '— — · —', '· — ·', '· · ·', '—', '· · —', '· · · —', '· — —', '— · · —', '— · — —', '— — · ·', '— — — — —', '· — — — —', '· · — — —', '· · · — —', '· · · · —', '· · · · ·', '— · · · ·', '— — · · ·', '— — — · ·', '— — — — ·',' ']
    for i in range(len(text)):
        for j in range(len(alfabeto)):
            if alfabeto[j] == text[i]:
                morseTradu.append(morse[j])
    morseTradu = " ".join(morseTradu)
    print(morseTradu)
    
traductorMorse("SOS")
traductorMorse("Hoy fue un gran dia, el sol estaba radiante y la gente muy contenta")
    
    
    
    
    
    
    
    