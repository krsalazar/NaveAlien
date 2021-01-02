import pygame, sys, time, nave

#Base que utilizaran todas las escenas del juego
class Escena:
    def __init__(self):
        self.proximaEscena = False
        self.jugando = True

    def leer_eventos(self, eventos):
        #Lee los eventos para interactuar con los objetos
        pass

    def actualizar(self):
        #Actualiza los objetos en la pantalla
        pass

    def dibujar(self, pantalla):
        #Dibuja los objetos en la pantalla
        pass

    def cambiar_escena(self, escena):
        #Cambia la escena del juego
        self.proximaEscena = escena
