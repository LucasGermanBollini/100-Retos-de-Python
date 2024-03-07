from PIL import Image
import requests
from io import BytesIO



def obtenerRelacionAspecto(url):
    print("Procesando...")
    respuesta = requests.get(url)
    imagen_bytes = BytesIO(respuesta.content)
    imagen = Image.open(imagen_bytes)
    ancho,alto = imagen.size
    formula = ancho / alto
    multiplicador = 1
    for i in range(1,10):
        relacion = i * formula
        relacionRedonda = round(relacion,1)
        if relacion - relacionRedonda < 0.1:
            multiplicador = i
    formula = formula * multiplicador
    formula = int(formula)
    mcd = 1
    terminar = 0
    mcdEncontrado = 1
    for i in range(2,10):
        if terminar == 0:
            if formula % i == 0 and multiplicador % i == 0:
                mcdEncontrado = i
                terminar = 1
           
    
    
    print(f"La relacion de aspecto de la imagen es de: {int(formula/mcdEncontrado)}:{int(1*multiplicador/mcdEncontrado)}")

#Colocar URL de la imagen entre comillas, algunas imagenes como las de IMGUR no las acepta
obtenerRelacionAspecto("https://www.blogdelfotografo.com/wp-content/uploads/2021/05/3-2-imagen-esquema.webp")