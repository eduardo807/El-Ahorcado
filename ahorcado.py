# -*- coding: utf-8 -*-

import random

IMAGENES_AHORCADO = ['''

    +---+
    |   |
        |
        |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        |
    ========= ''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
    =========''', '''
    
    +---+
    |   |
   [O   |
   /|\  |
   / \  |
        |
        |
    =========''', '''
    
    +---+
    |   |
   [O]  |
   /|\  |
   / \  |
        |
        |
    =========''']

palabras = {'Colores':'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(), 
            'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentagono hexagono heptagono octogono'.split(),
            'Frutas':'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(),
            'Animales':'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

def obtenerPalabraAlAzar(diccionarioDePalabras):
    claveDePalabras = random.choice(list(diccionarioDePalabras.keys()))
    indiceDePalabra = random.randint(0,len(diccionarioDePalabras[claveDePalabras]) - 1)
    return [diccionarioDePalabras[claveDePalabras][indiceDePalabra], claveDePalabras]

def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('letras Incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print (letra, end=' ')
    print()

    espaciosVacios = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]
            
    for letra in espaciosVacios:
        print(letra, end=' ')
    print()
    
def obtenerIntento(letrasProbadas):

    while True:
        print('Adivina una letra')
        intento = input()
        intento = intento.lower() 
        if len(intento) !=1:
            print('Por favor introduce una letra')
        elif intento in letrasProbadas:
            print('Yas has probado esa letra, elige otra')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor introduzca una letra')
        else:
            return intento

def jugarDeNuevo():
    print('Quieres jugar de nuevo?')
    return input().lower().startswith('s')

print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta, claveSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    print('La palabra secreta pertenece al conjunto: ' + claveSecreta)
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La Palabra Secreta Es "' + palabraSecreta + '"!¡HAS GANADO!')
            juegoTerminado = True
            
    else:
        letrasIncorrectas = letrasIncorrectas + intento
        
        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta +'"')
            juegoTerminado = True
            
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta, claveSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
