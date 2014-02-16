import pygame, os, sys
from pygame.locals import *

import GAME.ENTITIES.listener
import GAME.ENTITIES.baseentity
import TILEMAP.core

class TestNPC(GAME.ENTITIES.baseentity.BaseEntity):
	def __init__(self, eventmanager, configclass, environment):
		self.tilesheet = None
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
		self.environment = environment
		self.dialogfile = None
		self.drawSurf = pygame.Surface((24,32), SRCALPHA)
		##########
		self.xpos = 32
		self.ypos = 48

		self.xgrid = 2
		self.ygrid = 5

		self.ableToMove = True
		self.moving = False
		self.direction = self.configclass.DIRECTION_DOWN

		self.counter = 0
		self.threshold = 1
		self.tileSoFar = 0
		##########
		self.curRect = Rect(24,0,24,32)
		#self.drawSurf.blit(self.tilesheet, (0,0), self.curRect)
	def update(self, direction, amnt):
		#self.update_position()
		#self.update_image(direction, amnt)
		pass
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

	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			self.update_image(self.direction, 0)
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.InteractionEvent):
			if event.targetxgrid == self.xgrid and event.targetygrid == self.ygrid:
				e = GAME.EVENTMANAGER.eventmanager.DialogEvent(event.initiator, self, self.dialogfile)
				self.eventmanager.inform(e)
	def draw(self, surface, offset):
		surface.blit(self.drawSurf, ((self.xpos) - 4 + offset[0], self.ypos + 16 + offset[1]))
	def load_resources(self, resourcemanager):
		self.tilesheet = resourcemanager.load_image_alpha("CHARSHEETS/playerchar.png")
		self.dialogfile = resourcemanager.load_file_as_string("LANGUAGES/en/testdialog.txt")
