# -*- encoding: utf-8 -*-
import pygame, sys
import config

def load_image(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message

	image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color)

	return image

def print_sprite(code):
	img = load_image(config.SPRITES[code]['image'], config.SPRITES[code]['transparent'])
	if config.SPRITES[code]['angle'] != 0:
		img = pygame.transform.rotate(img, config.SPRITES[code]['angle'])

	return img
