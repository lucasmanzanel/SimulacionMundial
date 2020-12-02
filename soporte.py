from clases import *
import pickle
import random
from os.path import exists


def cargar_entre(desde, hasta, mensaje = "Ingrese un valor: "):
    opcion = int(input("\x1b[1;32m"+mensaje+"\x1b[0;m"))
    while opcion < desde or opcion > hasta:
        print("\x1b[1;31m"+"Error, el valor debe ser mayor a "+str(desde)+" y menor a "+str(hasta))
        opcion = int(input("\x1b[1;32m"+mensaje+"\x1b[0;m"))
    return opcion


def nombrar_confederacion(numero_confederacion):
    tupla_confederaciones = "0.UEFA", "1.CONMEBOL", "2.CONCACAF", "3.CAF", "4.AFC", "5.OFC"
    confederacion = tupla_confederaciones[numero_confederacion]
    return confederacion


def convertir_registro(vector_linea):
    confederacion = nombrar_confederacion(int(vector_linea[0]))
    pais = vector_linea[1]
    puntos = int(vector_linea[2])
    titulos = int(vector_linea[3])
    seleccion = Seleccion(pais, confederacion, puntos, titulos)
    return seleccion


def agregar_ordenado(vector, registro):
    n = len(vector)
    posicion = n
    izquierda, derecha = 0, n - 1

    while izquierda <= derecha:
        c = (izquierda + derecha) // 2

        if registro.puntos == vector[c].puntos:
            posicion = c
            break

        elif registro.puntos > vector[c].puntos:
            derecha = c - 1
        else:
            izquierda = c + 1

    if izquierda > derecha:
        posicion = izquierda

    vector[posicion : posicion] = [registro]


def cargar_vector(vector_selecciones):
    nombre_archivo = "paises.csv"
    if exists(nombre_archivo):
        archivo = open("paises.csv", "rt", encoding="utf-8")
        for linea in archivo:
            if linea[-1] == "\n":
                linea = linea[:-1]

            vector_linea = linea.split(",")
            seleccion = convertir_registro(vector_linea)
            agregar_ordenado(vector_selecciones, seleccion)
        archivo.close()


def buscar_mayor(vector_selecciones):
    vector_mayores = []
    mayor = 0
    for seleccion in vector_selecciones:
        if seleccion.titulos > mayor:
            mayor = seleccion.titulos
            vector_mayores = [seleccion]
        elif mayor is seleccion.titulos:
            vector_mayores.append(seleccion)
    return vector_mayores


def contar_campeones(vector_selecciones):
    vector_conteo = [0] * 6
    for seleccion in vector_selecciones:
        if seleccion.titulos > 0:
            indice = int(seleccion.confederacion[0])
            vector_conteo[indice] += 1
    return vector_conteo


def nombrar_archivo(x):
    nombre_archivo = "clasificacion "+str(x)+".dat"
    return nombre_archivo


def generar_vector(vector_selecciones, x):
    vector_confederacion = []
    contador = 0
    tupla_confederaciones = "0.UEFA", "1.CONMEBOL", "2.CONCACAF", "3.CAF", "4.AFC", "5.OFC"
    dato = tupla_confederaciones[x]
    for seleccion in vector_selecciones:
        if seleccion.confederacion == dato:
            agregar_ordenado(vector_confederacion, seleccion)
    return vector_confederacion


def generar_archivo(vector_confederacion, nombre_archivo):
    archivo = open(nombre_archivo, "wb")
    for seleccion in vector_confederacion:
        pais = Paises_Confederacion(seleccion.pais, seleccion.puntos, seleccion.titulos)
        pickle.dump(pais, archivo)
    archivo.close()


def validar_anfitrion(vector_selecciones):
    anfitrion = ""
    while anfitrion != str(-1):
        anfitrion = input("\x1b[1;32m"+"Ingrese el nombre del pais anfitrion (o -1 para salir de la opcion): "+"\x1b[0;m")
        if anfitrion == str(-1):
            return -1
        for i in range(len(vector_selecciones)):
            if vector_selecciones[i].pais.lower() == anfitrion.lower():
                return i
        print("\x1b[1;31m"+"Error, pais no encontrado"+"\x1b[0;m")


def busqueda_lineal(x, vector):
    for i in range(len(vector)):
        if vector[i] == x:
            return i
    return -1


def lista_participantes(vector_selecciones, vector_participantes, anfitrion):
    vector_participantes.append(vector_selecciones[anfitrion].pais)

    n = 36
    if anfitrion > n:
        n = 35

    for i in range(n):
        if i != anfitrion:
            vector_participantes.append(vector_selecciones[i].pais)


def completar_fixture(fixture, vector_participantes):
    fixture[0] = vector_participantes[0:8]
    del vector_participantes[0:8]
    for f in range(1, 4):
        for c in range(8):
            participante = random.choice(vector_participantes)
            fixture[f][c] = participante
            posicion = busqueda_lineal(participante, vector_participantes)
            del vector_participantes[posicion]


def generar_fixture(anfitrion, vector_selecciones):
    vector_participantes = []
    lista_participantes(vector_selecciones, vector_participantes, anfitrion)
    fixture = [[0] * 8 for i in range(4)]
    completar_fixture(fixture, vector_participantes)

    return fixture


def buscar_fixture(fixture, pais):
    filas, columnas = len(fixture), len(fixture[0])
    for f in range(filas):
        for c in range(columnas):
            if fixture[f][c].lower() == pais.lower():
                return c
    return -1
