# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 18:09:54 2017

@author: fran
"""
import random


def jugarAhorcado(numeroIntentos):
    
    palabra = palabraAleatoria();
    palabraEncriptada = encriptarPalabra(palabra);
    letrasJugadas = ""
    intentos = 0
    finalizado = False
    
    print("Bienvenido al juego del ahorcado")
    #mientras el juego no haya finalizado
    while (finalizado == False):
        #pedimos datos al usuario
        print("Letras jugadas: " + letrasJugadas)
        print("palabra: " + palabraEncriptada)
        letraJugada = raw_input("Introduce una letra: ")
    
        #mientras la letra jugada no sea un caracter
        while(letraJugada.isalpha() == False or len(letraJugada) != 1):
            letraJugada = raw_input("Solo se acepta un caracter. Introduce una letra: ")
        
        #mientras la letra no haya sido jugada antes
        while(letraJugada in letrasJugadas):
            letraJugada = raw_input("Ya has jugado este caracter. Introduce otra letra: ")
        
        #Añadimos la letra al string LetrasJugadas e incrementamos la variable intentos
        letrasJugadas = letrasJugadas + letraJugada
        intentos = intentos + 1
        
        #convertimos la palabra encriptada a lista para modificarla si se ha acertado
        listaPalabraEncriptada = list(palabraEncriptada)
        for indice in range(0, len(palabra)):
            if(letraJugada == palabra[indice]):
                if(palabra[indice] not in listaPalabraEncriptada):
                    intentos  = intentos - 1
                    
                listaPalabraEncriptada[indice] = palabra[indice]
       
        #convertimos la lista a string        
        palabraEncriptada = "".join(listaPalabraEncriptada)            
        
        #si el usuario ha ganado
        if(palabra == palabraEncriptada):
            print("Enhorabuena, has ganado, la palabra es: " + palabra)
            finalizado = True;
        else:
            #si el usuario ha perdido
            if(numeroIntentos == intentos):
                print("Has perdido, la palabra era " + palabra)
                finalizado = True;
            
                   
                
                
def palabraAleatoria():
    palabras = ["avion", "helicoptero", "caravana"]
    return palabras[random.randrange(3)]

def encriptarPalabra(palabra):
    palabraEncriptada = ""
    for caracter in palabra:
        palabraEncriptada = palabraEncriptada + "-";
        
    return palabraEncriptada    
        
             
            