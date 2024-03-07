"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
 """
import math

def areaPoligono():
    n = 0
    lados = []
    while n != -1:
        try:
            n = int(input("Ingrese los lados del poligono, -1 para finalizar: "))
            if n != -1 and n > 0:
                lados.append(n)
            if n < -1:
                print("Por favor, no introduzca valores negativos.")
            if n == -1 and len(lados) < 3:
                print("Por favor, introduzca al menos 3 poligonos.")
                n = 0
            if len(lados) == 4:
                n = -1
        except ValueError:
            print("Tipo de dato no valido.")
            
    print("Datos cargados con exitos!")
    print("Procesando informacion...")
    
    if len(lados) == 3:
        #Utilizamos la formula de Heron
        #Primero calculamos S
        s = sum(lados)/2
        formula = s * (s-lados[0]) * (s-lados[1]) * (s-lados[2])
        resultado = 0
        if formula > 0:
            resultado = math.sqrt(formula)
            resultado = round(resultado,3)
        if resultado <= 0:
            resultado = "Inexistente"
            print(f"El triángulo con lados de longitud {lados[0]}, {lados[1]} y {lados[2]} no puede existir en un plano euclidiano. Esto se debe a que, según la desigualdad triangular, la suma de las longitudes de cualquier par de lados de un triángulo debe ser siempre mayor que la longitud del tercer lado.")
        print(f"El resultado del area es de: {resultado}")
    elif len(lados) == 4:
        lados.sort()
        #Caso de que sea un rectangulo
        if lados[0] == lados[1] and lados[0] == lados[2] and lados[0] == lados[3]:
            print(f"El area del cuadrado es de:",lados[0]*lados[1])
        elif lados[0] == lados[1] and lados[2] == lados[3]:
            print(f"El area del rectangulo es de:",lados[0]*lados[2])
        else:
            print("Los poligonos ingresados no forman un triangulo, ni un cuadrado, ni un rectangulo.")
            
    

areaPoligono()
        
        