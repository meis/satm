#!/usr/bin/env python
# -*- coding: utf-8 -*-

HEIGHT			= 400
WIDTH			= 320
NAME			= "Snake Against the Machine!"

SPRITE_WIDTH 	= 10
SPRITE_HEIGHT	= 10

SPRITES = {
	'#': {
		'image': 'block.png',
		'angle': 0,
		'transparent': False
	},
	'2': {
		'image': 'food.png',
		'angle': 0,
		'transparent': True
	},
	'snake': {
		'image': 'snake.png',
		'angle': 0,
		'transparent': True
	},
	'head-right': {
		'image': 'snake-head.png',
		'angle': 0,
		'transparent': True
	},
	'head-left': {
		'image': 'snake-head.png',
		'angle': 180,
		'transparent': True
	},
	'head-down': {
		'image': 'snake-head.png',
		'angle': 270,
		'transparent': True
	},
	'head-up': {
		'image': 'snake-head.png',
		'angle': 90,
		'transparent': True
	},
	'tail-left': {
		'image': 'snake-tail.png',
		'angle': 180,
		'transparent': True
	},
	'tail-right': {
		'image': 'snake-tail.png',
		'angle': 0,
		'transparent': True
	},
	'tail-down': {
		'image': 'snake-tail.png',
		'angle': 270,
		'transparent': True
	},
	'tail-up': {
		'image': 'snake-tail.png',
		'angle': 90,
		'transparent': True
	},
	'body-up-down': {
		'image': 'snake-body.png',
		'angle': 90,
		'transparent': True
	},
	'body-down-up': {
		'image': 'snake-body.png',
		'angle': 90,
		'transparent': True
	},
	'body-left-right': {
		'image': 'snake-body.png',
		'angle': 0,
		'transparent': True
	},
	'body-right-left': {
		'image': 'snake-body.png',
		'angle': 0,
		'transparent': True
	},
	'body-right-up': {
		'image': 'snake-l.png',
		'angle': 0,
		'transparent': True
	},
	'body-up-right': {
		'image': 'snake-l.png',
		'angle': 0,
		'transparent': True
	},
	'body-left-down': {
		'image': 'snake-l.png',
		'angle': 180,
		'transparent': True
	},
	'body-down-left': {
		'image': 'snake-l.png',
		'angle': 180,
		'transparent': True
	},
	'body-up-left': {
		'image': 'snake-l.png',
		'angle': 90,
		'transparent': True
	},
	'body-left-up': {
		'image': 'snake-l.png',
		'angle': 90,
		'transparent': True
	},
	'body-right-down': {
		'image': 'snake-l.png',
		'angle': 270,
		'transparent': True
	},
	'body-down-right': {
		'image': 'snake-l.png',
		'angle': 270,
		'transparent': True
	}

}

BACKGROUNDS = {
	'ice' : 'ice.png',
	'stars' : 'stars.png'
}
