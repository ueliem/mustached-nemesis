import pygame, os, sys
from pygame.locals import *

import GAME.ENTITIES.listener
import GAME.ENTITIES.baseentity
import GAME.EVENTMANAGER.eventmanager
import TILEMAP.core

class Player(GAME.ENTITIES.baseentity.BaseEntity):
	def __init__(self, eventmanager, configclass, environment):
		self.tilesheet = None
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
		self.environment = environment
		self.drawSurf = pygame.Surface((24,32), SRCALPHA)
		##########
		self.xpos = 64
		self.ypos = 48

		self.xgrid = 4
		self.ygrid = 5

		self.ableToMove = True
		self.moving = False
		self.direction = self.configclass.DIRECTION_DOWN
		self.is_interacting = False
		self.counter = 0
		self.threshold = 1
		self.tileSoFar = 0
		##########
		self.curRect = Rect(24,0,24,32)
		#self.drawSurf.blit(self.tilesheet, (0,0), self.curRect)
	def update(self, direction, amnt):
		self.update_position()
		self.update_image(direction, amnt)
	def update_image(self, direction, amnt):
		if direction == self.configclass.DIRECTION_UP:
			if amnt == 0:
				self.curRect = Rect(24,0,24,32)
			elif amnt < 5:
				self.curRect = Rect(0,0,24,32)
			elif amnt < 10:
				self.curRect = Rect(24,0,24,32)
			elif amnt < 14:
				self.curRect = Rect(48,0,24,32)
			else:
				self.curRect = Rect(24,0,24,32)

		elif direction == self.configclass.DIRECTION_DOWN:
			if amnt == 0:
				self.curRect = Rect(24,64,24,32)
			elif amnt < 5:
				self.curRect = Rect(0,64,24,32)
			elif amnt < 10:
				self.curRect = Rect(24,64,24,32)
			elif amnt < 14:
				self.curRect = Rect(48,64,24,32)
			else:
				self.curRect = Rect(24,64,24,32)

		elif direction == self.configclass.DIRECTION_LEFT:
			if amnt == 0:
				self.curRect = Rect(24,96,24,32)
			elif amnt < 5:
				self.curRect = Rect(0,96,24,32)
			elif amnt < 10:
				self.curRect = Rect(24,96,24,32)
			elif amnt < 14:
				self.curRect = Rect(48,96,24,32)
			else:
				self.curRect = Rect(24,96,24,32)

		elif direction == self.configclass.DIRECTION_RIGHT:
			if amnt == 0:
				self.curRect = Rect(24,32,24,32)
			elif amnt < 5:
				self.curRect = Rect(0,32,24,32)
			elif amnt < 10:
				self.curRect = Rect(24,32,24,32)
			elif amnt < 14:
				self.curRect = Rect(48,32,24,32)
			else:
				self.curRect = Rect(24,32,24,32)
		self.drawSurf = pygame.Surface((24,32), SRCALPHA)
		self.drawSurf.blit(self.tilesheet, (0,0), self.curRect)

	def update_position(self):
		if self.moving:
			if self.counter >= self.threshold:
				if self.direction == self.configclass.DIRECTION_UP:
					self.ypos -= 1
				elif self.direction == self.configclass.DIRECTION_DOWN:
					self.ypos += 1
				elif self.direction == self.configclass.DIRECTION_LEFT:
					self.xpos -= 1
				elif self.direction == self.configclass.DIRECTION_RIGHT:
					self.xpos += 1
				self.tileSoFar += 1
		
				self.counter = 0

				if self.tileSoFar == 16:
					keys = pygame.key.get_pressed()
					if self.direction == self.configclass.DIRECTION_UP:
						self.ygrid -= 1
					elif self.direction == self.configclass.DIRECTION_DOWN:
						self.ygrid += 1
					elif self.direction == self.configclass.DIRECTION_LEFT:
						self.xgrid -= 1
					elif self.direction == self.configclass.DIRECTION_RIGHT:
						self.xgrid += 1

					if keys[K_UP] and self.direction == self.configclass.DIRECTION_UP and self.check_can_move(self.direction):
						self.tileSoFar = 0
					elif keys[K_DOWN] and self.direction == self.configclass.DIRECTION_DOWN and self.check_can_move(self.direction):
						self.tileSoFar = 0
					elif keys[K_LEFT] and self.direction == self.configclass.DIRECTION_LEFT and self.check_can_move(self.direction):
						self.tileSoFar = 0
					elif keys[K_RIGHT] and self.direction == self.configclass.DIRECTION_RIGHT and self.check_can_move(self.direction):
						self.tileSoFar = 0
					else:
						self.tileSoFar = 0
						self.moving = False

			else:
				self.counter += 1
		else:
			pass

	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			self.update(self.direction, self.tileSoFar)
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.KeyPressEvent):
			if (not self.moving) and self.ableToMove:
				if event.key == K_UP:
					self.direction = self.configclass.DIRECTION_UP
					if self.check_can_move(self.direction):
						self.moving = True
				elif event.key == K_DOWN:
					self.direction = self.configclass.DIRECTION_DOWN
					if self.check_can_move(self.direction):
						self.moving = True
				elif event.key == K_LEFT:
					self.direction = self.configclass.DIRECTION_LEFT
					if self.check_can_move(self.direction):
						self.moving = True
				elif event.key == K_RIGHT:
					self.direction = self.configclass.DIRECTION_RIGHT
					if self.check_can_move(self.direction):
						self.moving = True
				elif event.key == K_z and self.ableToMove == True and not self.is_interacting:
					e = None
					if self.direction == self.configclass.DIRECTION_UP:
						e = GAME.EVENTMANAGER.eventmanager.InteractionEvent(self, self.xgrid, self.ygrid-1)
					elif self.direction == self.configclass.DIRECTION_DOWN:
						e = GAME.EVENTMANAGER.eventmanager.InteractionEvent(self, self.xgrid, self.ygrid+1)
					elif self.direction == self.configclass.DIRECTION_LEFT:
						e = GAME.EVENTMANAGER.eventmanager.InteractionEvent(self, self.xgrid-1, self.ygrid)
					elif self.direction == self.configclass.DIRECTION_RIGHT:
						e = GAME.EVENTMANAGER.eventmanager.InteractionEvent(self, self.xgrid+1, self.ygrid)
					self.eventmanager.inform(e)
				elif event.key == K_z and self.is_interacting:
					self.is_interacting = False
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.DialogEvent):
			self.ableToMove = False
			self.is_interacting = True
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.EnablePlayerEvent):
			self.ableToMove = True
	def check_can_move(self, direction):
		collisonmap = self.environment.create_collison_map()
		try:
			if direction == self.configclass.DIRECTION_UP:
				if int(collisonmap[self.ygrid-1][self.xgrid]) == 0:
					return True
			elif direction == self.configclass.DIRECTION_DOWN:
				if int(collisonmap[self.ygrid+1][self.xgrid]) == 0:
					return True
			elif direction == self.configclass.DIRECTION_LEFT:
				if int(collisonmap[self.ygrid][self.xgrid-1]) == 0:
					return True
			elif direction == self.configclass.DIRECTION_RIGHT:
				if int(collisonmap[self.ygrid][self.xgrid+1]) == 0:
					return True
		except IndexError:
			return False

	def draw(self, surface, offset):
		#surface.blit(self.drawSurf, ((self.xpos) - 4, self.ypos + 16))
		surface.blit(self.drawSurf, (108,64))
	def load_resources(self, resourcemanager):
		self.tilesheet = resourcemanager.load_image_alpha("CHARSHEETS/playerchar.png")
