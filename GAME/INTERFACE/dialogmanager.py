import pygame, os, sys
from pygame.locals import *

import GAME.ENTITIES.listener
import GAME.EVENTMANAGER.eventmanager

class DialogManager(GAME.ENTITIES.listener.BaseListener):
	def __init__(self, eventmanager, configclass):
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
		self.is_displaying_dialog = False
		self.drawSurf = pygame.Surface((self.configclass.window_width,40))
		self.drawSurf.fill((255,255,255))
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			pass
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.DialogEvent):
			self.is_displaying_dialog = True
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.KeyPressEvent):
			if self.is_displaying_dialog and event.key == K_x:
				self.eventmanager.inform(GAME.EVENTMANAGER.eventmanager.EnablePlayerEvent())
				self.is_displaying_dialog = False
	def draw(self, surface):
		if self.is_displaying_dialog:
			surface.blit(self.drawSurf, (0,(self.configclass.window_height-self.drawSurf.get_height())) )
