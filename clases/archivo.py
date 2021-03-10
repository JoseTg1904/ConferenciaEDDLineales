#Librerias para hacer uso de los archivos
import os

''' 
Metodo que genera un archivo de salida en la carpeta graficos del proyecto

os.getcwd() es una funcion que devuelve el directorio actual de ejecucucion del
programa esto para poder hacer uso de la carpeta graficos y guardar ahi los archivos
de salida 

El archivo de salida es de extension .dot debido a que este es el lenguaje que
se utiliza para graficar haciendo uso del la libreria de Graphviz, tambien
se puede utilizar .txt '''

def crearGrafico(dot, nombre):
    path = os.getcwd() + "/graficos/" + nombre + ".dot"
    
    # Abriendo el archivo en modo de escritura
    file = open(path, "w")
    file.write(dot)
    file.close()