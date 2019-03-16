# Hangman interfaz

HANGMAN = " _\n| |\n| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __\n| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n| | | | (_| | | | | (_| | | | | | | (_| | | | |\n|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n\t\t    __/ /\n\t\t   |___/"
GAMEOVER = "\n ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗\n██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗\n██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝\n██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗\n╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║\n ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝"
WIN="\n██╗    ██╗██╗███╗   ██╗\n██║    ██║██║████╗  ██║\n██║ █╗ ██║██║██╔██╗ ██║\n██║███╗██║██║██║╚██╗██║\n╚███╔███╔╝██║██║ ╚████║\n ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝"
GRAFICO_0 = "   _______\n |/      |\n |\n |      \n |              {}\n |\n |\n_|___"
GRAFICO_1 = "   _______\n |/      |\n |      (_)\n |      \n |              {}\n |\n |\n_|___"
GRAFICO_2 = "   _______\n |/      |\n |      (_)\n |       |\n |       |      {}\n |\n |\n_|___"
GRAFICO_3 = "   _______\n |/      |\n |      (_)\n |      \|\n |       |      {}\n |\n |\n_|___"
GRAFICO_4 = "   _______\n |/      |\n |      (_)\n |      \|/\n |       |      {}\n |\n |\n_|___"
GRAFICO_5 = "   _______\n |/      |\n |      (_)\n |      \|/\n |       |      {}\n |      /\n |\n_|___"
GRAFICO_6 = "   _______\n |/      |\n |      (_)\n |      \|/\n |       |      {}\n |      / \ \n |\n_|___"

lista_graficos = [GRAFICO_6,GRAFICO_5,GRAFICO_4,GRAFICO_3,GRAFICO_2,GRAFICO_1,GRAFICO_0]
def imprimir_bienvenida():
    print(HANGMAN)

def crear_cadena(lista_letras):
    palabra = ""
    for letra in lista_letras:
        palabra = palabra + letra + " "
    return palabra

def imprimir_fin(vidas):
    if vidas == 0:
        print(GAMEOVER)
    else:
        print(WIN)

def imprimir_pantalla(lista_letras, vidas):
    palabra = crear_cadena(lista_letras)
    print(lista_graficos[vidas].format(palabra))
