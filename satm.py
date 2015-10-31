# -*- encoding: utf-8 -*-

import pygame
import sys
import src.scene, src.menu_scene, src.pause_scene, src.stage_scene, config

from pygame.locals import *

class Director:

	def __init__(self, height, width, name):
		self.scene 		= None
		self.quit_flag 	= False
		self.clock 		= pygame.time.Clock()
		self.width 		= width
		self.height 	= height
		self.name 		= name
		self.screen 	= pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.name)

	def loop(self):
		while not self.quit_flag:
			#time = self.clock.tick(60)
			keys = pygame.key.get_pressed()
			# Quit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.scene.quit()

			# detecta eventos
			self.scene.event(keys)

			# actualiza la escena
			self.scene.update()

			# dibuja la pantalla
			self.scene.draw(self.screen)
			pygame.display.flip()

	def change_scene(self, scene):
		self.scene = scene

	def quit(self):
		self.quit_flag = True


def main():
	game = Director(config.HEIGHT, config.WIDTH, config.NAME)
	main_menu = src.stage_scene.StageScene(game, '2')
	game.change_scene(main_menu)
	game.loop()


if __name__ == '__main__':
	pygame.init()
	main()
