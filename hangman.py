from hangman_interfaz import *
import os
import random

PALABRAS_DEFAULT = ["caracol","telefono","radio","boxeo","avion","lagrima","computadora"]
CANT_VIDAS = 6
VACIO = "_"

def validar_letra(str):
    return ((len(str) == 1) and (str.isalpha()))

def pedir_letra(letras_usadas):
    letra = input("Ingrese una letra: \n")
    while not validar_letra(letra):
        letra = input("DIJE UNA LETRA: \n")
    while letra in letras_usadas:
        letra = input("Ya ingresaste esa letran ingresá otra: \n")
    letras_usadas.append(letra)
    return letra[0]

def crear_lista_(str):
    list = []
    for x in range(len(str)):
        list.append(VACIO)
    return list

def insertar_letra(lista_letras, palabra, letra):
    i = 0
    for caracter in palabra:
        if caracter == letra:
            lista_letras[i] = str(letra)
        i+=1
    return 0

def main():

    vidas = CANT_VIDAS
    letras_usadas = []
    imprimir_bienvenida()

    palabra = PALABRAS_DEFAULT[random.randint(0, len(PALABRAS_DEFAULT)-1)]
    lista_letras = crear_lista_(palabra)
    imprimir_pantalla(lista_letras,vidas)

    while ((vidas > 0) and (VACIO in lista_letras)):

        letra = pedir_letra(letras_usadas) #letra es un caracter

        if letra in palabra:
            insertar_letra(lista_letras, palabra, letra)
        else:
            vidas -= 1
        os.system('clear')
        imprimir_pantalla(lista_letras, vidas)

    imprimir_fin(vidas,palabra)

    return 0

main ()
