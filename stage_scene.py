# -*- encoding: utf-8 -*-
import scene
import utils
import config
import stages
import pygame
from pygame.locals import *
import random

'''
TODO:
* Fer que el grid es correspongui a coordenades X,Y
* Dues o més food seguides

'''

class StageScene(scene.Scene):		

	def __init__(self, director, stage_id):
		scene.Scene.__init__(self, director)		
		
		self.game_area = GameArea(self, [0,80], stage_id)	
		self.notify_area = NotifyArea(self, [0,0], stage_id)
		self.paused = False	
		self.counter = {
			'score' : 0
		}

	def update(self):
		if self.paused == False:
			self.game_area.update()

	def event(self, keys):

		if keys[K_SPACE]:
			self.pause()
		if keys[K_ESCAPE]:
			self.quit()

		self.game_area.event(keys)

	def draw(self, screen):
		if self.paused:
			pass
		else:
			self.game_area.draw(screen)
			self.notify_area.draw(screen)

	def pause(self):
		if self.paused:
			self.paused = False
		else:
			self.paused = True

	def quit(self):
		self.director.quit()
	
					
class NotifyArea():

	def __init__(self, stage, start_pos, stage_id):
		self.stage = stage
		self.start_pos = start_pos

	def draw(self, screen):
		background_image = utils.load_image("notify_area.png")
		screen.blit(background_image, (self.start_pos[0], self.start_pos[1]))
		
		font = pygame.font.SysFont("Courier New",18)
		ren = font.render("Score: " + str(self.stage.counter['score']), 1, (255,255,255))
		screen.blit(ren, [10, 10])

	
class GameArea():

	def __init__(self, stage, start_pos, stage_id):		
		self.stage = stage

		self.grid = stages.STAGES[stage_id]['grid']		

		self.max_y = len(stages.STAGES[stage_id]['grid'])
		self.max_x = len(stages.STAGES[stage_id]['grid'][0])

		self.food = stages.STAGES[stage_id]['food']

		self.background_type = stages.STAGES[stage_id]['background-type']
		self.start_pos = start_pos		
		self.stage_id = stage_id
		self.sprite_width = config.SPRITE_WIDTH
		self.sprite_height = config.SPRITE_HEIGHT

		self.num_ticks = 10
		self.ticks = 0

		self.snake = Snake(self)

	def get_start_pos(self):
		return self.start_pos

	def get_stage_id(self):
		return self.stage_id

	def update(self):
		if self.ticks == self.num_ticks:
			self.snake.update()
			self.ticks = 0
		else:
			self.ticks = self.ticks + 1

	def event(self, keys):

		if keys[K_DOWN]:
			self.snake.add_direction("down")

		if keys[K_UP]:
			self.snake.add_direction("up")

		if keys[K_RIGHT]:
			self.snake.add_direction("right")

		if keys[K_LEFT]:
			self.snake.add_direction("left")

	def draw(self, screen):
		self.draw_background(screen)		
		self.draw_food(screen)	
		self.snake.draw(screen)

	def draw_sprite(self, screen, sprite, position):
		screen.blit(utils.print_sprite(sprite), (self.start_pos[0] + position[0] * self.sprite_width , self.start_pos[1] + position[1] * self.sprite_height))

	def draw_background(self, screen):
		
		background_image = utils.load_image(config.BACKGROUNDS[self.background_type])
		screen.blit(background_image, (self.start_pos[0], self.start_pos[1]))	

		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == '#':
					self.draw_sprite(screen, "#", [j, i])	

	def is_block(self, position):
		is_block = False
		if self.grid[position[1]][position[0]] == "#":
			is_block = True
		return is_block

	def is_food(self, position):
		return self.food.count([position[0], position[1]]) > 0

	def is_free(self, position):
		if self.is_block(position):
			return False
		elif self.is_food(position):
			return False
		elif self.snake.is_in(position):
			return False
		return True

	def get_rand_free_pos(self):
		free_positions = []
		for i in range(0, self.max_x):
			for j in range(0, self.max_y):
				if self.is_free([i, j]):
					free_positions.append([i,j])

		return random.choice(free_positions)

	def draw_food(self, screen):
		for i in range(0,len(self.food)): 	
			self.draw_sprite(screen, "2", self.food[i])

	def add_food(self, position):
		self.food.append(position)

	def eat_food(self, position):

		if self.food.count([position[0], position[1]]) > 0:
			self.food.remove([position[0], position[1]])

			if True:
				self.add_food(self.get_rand_free_pos())

			self.stage.counter['score'] = self.stage.counter['score'] + 1

			return True
		return False

class Snake():
	
	def __init__(self, game_area):
		self.eating = False
		self.game_area = game_area
		stage_id = game_area.get_stage_id()
		self.list = stages.STAGES[stage_id]['snake']
		self.direction = stages.STAGES[stage_id]['direction']
		self.next_direction = self.direction
		
	def draw(self, screen):

		# Print snake's head.
		head_part = "head-" + self.direction
		self.game_area.draw_sprite(screen, head_part , [self.list[0][0], self.list[0][1]])

				
		# Print snake's body.

		for i in range(1,(len(self.list))):
			if i == len(self.list) - 1:			
				body_part = "tail-"
			else:
				body_part = "body-"

			if self.list[i-1][0] - self.list[i][0] == 1:
				body_part = body_part + "right"			
			elif self.list[i-1][0] - self.list[i][0] > 1:
				body_part = body_part + "left"
			elif self.list[i-1][0] - self.list[i][0] == -1:
				body_part = body_part + "left"
			elif self.list[i-1][0] - self.list[i][0] < -1:
				body_part = body_part + "right"
			elif self.list[i-1][1] -self.list[i][1] == 1:
				body_part = body_part + "down"
			elif self.list[i-1][1] -self.list[i][1] > 1:
				body_part = body_part + "up"
			elif self.list[i-1][1] -self.list[i][1] == -1:
				body_part = body_part + "up"
			else:
				body_part = body_part + "down"
			
			if i != len(self.list) - 1:	

				if self.list[i][0] - self.list[i+1][0] == 1:
					body_part = body_part + "-left"
				elif self.list[i][0] - self.list[i+1][0] > 1:
					body_part = body_part + "-right"
				elif self.list[i][0] - self.list[i+1][0] == -1:
					body_part = body_part + "-right"
				elif self.list[i][0] - self.list[i+1][0] < -1:
					body_part = body_part + "-left"
				elif self.list[i][1] -self.list[i+1][1] == 1:
					body_part = body_part + "-up"
				elif self.list[i][1] -self.list[i+1][1] > 1:
					body_part = body_part + "-down"
				elif self.list[i][1] -self.list[i+1][1] == -1:
					body_part = body_part + "-down"
				else:				
					body_part = body_part + "-up"

			self.game_area.draw_sprite(screen, body_part , [self.list[i][0], self.list[i][1]])

	def add_direction(self, direction):
		self.next_direction = direction

	def is_in(self, position):
		return self.list.count([position[0], position[1]]) > 0

	def update(self):
		new_x = self.list[0][0]
		new_y = self.list[0][1]

		if (self.next_direction == "up") & (self.direction != "down"):
			self.direction = "up"
		elif (self.next_direction == "down") & (self.direction != "up"):
			self.direction = "down"
		elif (self.next_direction == "left") & (self.direction != "right"):
			self.direction = "left"
		elif (self.next_direction == "right") & (self.direction != "left"):
			self.direction = "right"
		
		if self.direction == "up":
			new_y = new_y - 1
		elif self.direction == "down":
			new_y = new_y + 1
		elif self.direction == "left":
			new_x = new_x - 1
		else:
			new_x = new_x + 1

		new_x = new_x % self.game_area.max_x
		new_y = new_y % self.game_area.max_y

		self.list.insert(0, [new_x, new_y])

		if self.eating != True:
			self.list = self.list[0:len(self.list)-1]
		else:			
			self.eating = False
		
		# Snake vs Snake.
		if self.list.count([new_x, new_y]) > 1:
			print "Snake vs Snake"
			sys.exit(0)

		if self.game_area.is_block([new_x, new_y]):
			self.game_area.exit()
		if self.game_area.eat_food([new_x, new_y]):
			self.eating = True
	
