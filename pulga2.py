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

		self.lista_imagenes = []

		for i in range(6):
			nombrePng = 'tile{}.png'.format(i + 1)
			image_rect = self.game.obtenerGrafico(nombrePng, escala)
			self.lista_imagenes.append(image_rect[0])

		escalaX = escala[0]
		escalaY = escala[1]

		self.image = pygame.Surface((ancho * escalaX, escalaY))
		self.image.set_colorkey((0, 0, 0))

		if velX_rnd == 0:
			for i in range(ancho):
				if i == 0 and ancho < self.game.COLUMNAS:
					self.image.blit(self.lista_imagenes[1], (i * escalaX, 0))

				elif i == ancho - 1 and ancho < self.game.COLUMNAS:
					self.image.blit(self.lista_imagenes[2], (i * escalaX, 0))

				else:
					self.image.blit(self.lista_imagenes[0], (i * escalaX, 0))

		else:
			for i in range(ancho):
				self.image.blit(self.lista_imagenes[5], (i * escalaX, 0))

		self.rect = self.image.get_rect()
		self.rect.topleft = (x * TX, y * TY)

		self.ancho = ancho
		self.velX = velX_rnd


	def update(self):
		self.rect.y += self.game.scroll
		self.rect.x += self.velX

		if (self.rect.right > self.game.RESOLUCION[0] and self.velX > 0) or (self.rect.x < 0 and self.velX < 0):
			self.velX = -self.velX

		# if self.ancho == self.game.COLUMNAS:
		# 	self.game.pulga.plataformaMETA = self.rect.y 

		if self.rect.top > self.game.RESOLUCION[1]:
			self.kill()







