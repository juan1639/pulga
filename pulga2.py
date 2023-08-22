import pygame
import random

#---------------------------------------------------------------
# Clases:
#			Pulga 		(No sprite)
#			Plataforma 	(Sprite)
#			FlappyBird	(Sprite)
#			Bicho 		(Sprite)
#			Textos		(Sprite)
#			Decorativos (Sprite)
#--------------------------------------------------------------					
class Pulga():
	def __init__(self, game, x, y, TX, TY, escala):
		self.game = game 


class Plataforma(pygame.sprite.Sprite):
	def __init__(self, game, x, y, ancho, velX_rnd, TX, TY, escala):
		super().__init__()
		self.game = game 

