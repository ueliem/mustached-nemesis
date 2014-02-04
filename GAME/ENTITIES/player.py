import pygame, os, sys
from pygame.locals import *

class Player:
	def __init__(self, tl, configclass):
		self.tilesheet = tl
		self.configclass = configclass
		self.drawSurf = pygame.Surface((24,32), SRCALPHA)
		self.moving = False
		self.curRect = Rect(24,0,24,32)
		self.drawSurf.blit(self.tilesheet, (0,0), self.curRect)
	def update(self, direction, amnt):
		self.update_image(direction, amnt)
		self.update_position()
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
