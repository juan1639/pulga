import pygame
import sys
import random

from pulga2 import *

# ----------------------------------------------------------------
# Codigo Principal (main.py) ... Aqui se aloja la clase Game
# 
# Funciones:
# 			instancias()
#			reInstancias()
#			obtenerGrafico()
#			dibujaScroll()
#
#			buclePrincipal()
#							update()
#							draw()
#							check_event()			
# ----------------------------------------------------------------
class Game:
	def __init__(self):
		pygame.init()

		self.rojo = (209, 36, 5)
		self.verde = (50, 205, 54)
		self.amarillo = (240, 130, 14)
		self.azulOsc = (9, 20, 70)
		self.fondoGRIS = (80, 80, 80)
		self.fondoCIELOAzul = (92, 197, 222)
		self.blancoNUBE = (249, 249, 249)

		self.RESOLUCION = (800, 700)
		self.FPS = 50

		self.TX = 50
		self.TY = 50
		self.FILAS = int(self.RESOLUCION[1] / self.TY)
		self.COLUMNAS = int(self.RESOLUCION[0] / self.TX)

		self.GRAVEDAD = 1
		self.MAX_PLATAFORMAS = 7
		self.PLATAFORMAS_LEVEL_UP = 70
		self.contadorPlataformas = 0
		self.anchoPlataf_nivel = [(2, 7), (2, 6), (2, 5), (2, 5),
									(2, 5), (2, 4), (2, 4), (2, 4)]

		self.programaEjecutandose = True
		self.presentacion = True
		self.enJuego = False
		self.gameOver = False
		self.nivelSuperado = False

		self.pantalla = pygame.display.set_mode(self.RESOLUCION)
		self.reloj = pygame.time.Clock()

		self.scrollImg1 = pygame.image.load('./assets/img/scrollBg1.png').convert()
		self.scrollImg2 = pygame.image.load('./assets/img/scrollBg2.png').convert()

		self.SCROLL_THRESH = 200
		self.scroll = 0
		self.bgScroll = 0

		self.sonido_salto = pygame.mixer.Sound("./assets/sound/jumpbros.ogg")
		self.sonido_salto.set_volume(0.3)
		self.sonido_gameOver = pygame.mixer.Sound('./assets/sound/gameoveretro.ogg')
		self.sonido_gameOver.set_volume(0.7)
		self.sonido_pacIntermision = pygame.mixer.Sound('./assets/sound/pacmanintermision.ogg')
		self.sonido_pacIntermision.set_volume(0.7)

		pygame.mixer.music.load("./assets/sound/mario_tuberias.ogg")
		pygame.mixer.music.set_volume(0.4)
		pygame.mixer.music.play(loops=2)

		self.lista_spritesAdibujar = pygame.sprite.Group()
		self.lista_plataformas = pygame.sprite.Group()

		self.instancias()


	def instancias(self):
		self.puntos = 0
		self.nivel = 1
		self.vidas = 3


	def reInstanciasPlataformas(self):
		# Reinstancias Plataformas ------------------------------
		pass


	def obtenerGrafico(self, nombrePng, escala):
		img = pygame.image.load('./assets/img/' + nombrePng).convert()
		image = pygame.transform.scale(img, escala)
		image.set_colorkey((255, 255, 255))
		rect = image.get_rect()
		image_rect = (image, rect)

		return image_rect


	def dibujaScroll(self):
		pass


	def update(self):
		pygame.display.set_caption(str(int(self.reloj.get_fps())))
		
		pygame.display.flip()
		self.reloj.tick(self.FPS)


	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

				elif event.key == pygame.K_RETURN and self.presentacion:
					self.presentacion = False
					self.enJuego = True
					pygame.mixer.music.stop()


	def buclePrincipal(self):
		while self.programaEjecutandose:
			self.check_event()
			self.update()


if __name__ == '__main__':
    game = Game()
    game.buclePrincipal()


			
