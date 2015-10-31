#!/usr/bin/env python
# -*- coding: utf-8 -*-

HEIGHT			= 400
WIDTH			= 320
NAME			= "Snake Against the Machine!"

SPRITE_WIDTH 	= 10
SPRITE_HEIGHT	= 10

SPRITES = {
	'#': {
		'image': 'img/block.png',
		'angle': 0,
		'transparent': False
	},
	'2': {
		'image': 'img/food.png',
		'angle': 0,
		'transparent': True
	},
	'snake': {
		'image': 'img/snake.png',
		'angle': 0,
		'transparent': True
	},
	'head-right': {
		'image': 'img/snake-head.png',
		'angle': 0,
		'transparent': True
	},
	'head-left': {
		'image': 'img/snake-head.png',
		'angle': 180,
		'transparent': True
	},
	'head-down': {
		'image': 'img/snake-head.png',
		'angle': 270,
		'transparent': True
	},
	'head-up': {
		'image': 'img/snake-head.png',
		'angle': 90,
		'transparent': True
	},
	'tail-left': {
		'image': 'img/snake-tail.png',
		'angle': 180,
		'transparent': True
	},
	'tail-right': {
		'image': 'img/snake-tail.png',
		'angle': 0,
		'transparent': True
	},
	'tail-down': {
		'image': 'img/snake-tail.png',
		'angle': 270,
		'transparent': True
	},
	'tail-up': {
		'image': 'img/snake-tail.png',
		'angle': 90,
		'transparent': True
	},
	'body-up-down': {
		'image': 'img/snake-body.png',
		'angle': 90,
		'transparent': True
	},
	'body-down-up': {
		'image': 'img/snake-body.png',
		'angle': 90,
		'transparent': True
	},
	'body-left-right': {
		'image': 'img/snake-body.png',
		'angle': 0,
		'transparent': True
	},
	'body-right-left': {
		'image': 'img/snake-body.png',
		'angle': 0,
		'transparent': True
	},
	'body-right-up': {
		'image': 'img/snake-l.png',
		'angle': 0,
		'transparent': True
	},
	'body-up-right': {
		'image': 'img/snake-l.png',
		'angle': 0,
		'transparent': True
	},
	'body-left-down': {
		'image': 'img/snake-l.png',
		'angle': 180,
		'transparent': True
	},
	'body-down-left': {
		'image': 'img/snake-l.png',
		'angle': 180,
		'transparent': True
	},
	'body-up-left': {
		'image': 'img/snake-l.png',
		'angle': 90,
		'transparent': True
	},
	'body-left-up': {
		'image': 'img/snake-l.png',
		'angle': 90,
		'transparent': True
	},
	'body-right-down': {
		'image': 'img/snake-l.png',
		'angle': 270,
		'transparent': True
	},
	'body-down-right': {
		'image': 'img/snake-l.png',
		'angle': 270,
		'transparent': True
	}
}

BACKGROUNDS = {
	'ice' : 'img/ice.png',
	'stars' : 'img/stars.png'
}
