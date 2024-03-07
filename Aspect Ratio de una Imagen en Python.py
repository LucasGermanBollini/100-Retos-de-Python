"""
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
"""

from PIL import Image
import requests
from io import BytesIO

#Esta primera version del codigo descarga una imagen y divide su alto y ancho para sacar la relacion de aspecto.
def obtenerRelacionAspectoSencillo(url):
    print("Procesando...")
    respuesta = requests.get(url)
    imagen_bytes = BytesIO(respuesta.content)
    imagen = Image.open(imagen_bytes)
    ancho,alto = imagen.size
    formula = ancho / alto
           
    print(f"La relacion de aspecto de la imagen es de: {round(formula,2)}:1")

obtenerRelacionAspectoSencillo("https://previews.123rf.com/images/patterndesign/patterndesign1706/patterndesign170601028/80050485-resumen-de-fondo-de-imagen-16-9-relaci%C3%B3n-de-aspecto-en-el-estilo-de-arte-de-p%C3%ADxeles.jpg")

#Esta otra funcion es una version mas "pro", muestra la relacion de la imagen a un valor redondeado y estandar como lo conocemos ej: 16:9 o 4:3
#Podria hacerse mas facil utilizando distintas bibliotecas para redondear fracciones, en si el resultado es el mismo, pero a la vista es mas agradebla esta otra version

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

#Colocar URL de la imagen entre comillas, algunas imagenes como las de IMGUR no las acepta, pero cualquier otra si, mismo sacadas de google suelen funcionar siempre.
obtenerRelacionAspecto("https://previews.123rf.com/images/patterndesign/patterndesign1706/patterndesign170601028/80050485-resumen-de-fondo-de-imagen-16-9-relaci%C3%B3n-de-aspecto-en-el-estilo-de-arte-de-p%C3%ADxeles.jpg")
