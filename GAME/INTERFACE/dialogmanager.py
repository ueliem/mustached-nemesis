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
		pygame.font.init()
		self.font = pygame.font.Font(None, 24)
		self.current_dialog = []
		self.dialog_counter = 0
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			pass
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.DialogEvent):
			self.is_displaying_dialog = True
			self.current_dialog = event.dialogfile
			self.dialog_counter = 0
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.KeyPressEvent):
			#if self.is_displaying_dialog and event.key == K_x:
			#	self.eventmanager.inform(GAME.EVENTMANAGER.eventmanager.EnablePlayerEvent())
			#	self.is_displaying_dialog = False
			if event.key == K_z and self.is_displaying_dialog:
				if self.dialog_counter >= len(self.current_dialog) - 1:
					self.eventmanager.inform(GAME.EVENTMANAGER.eventmanager.EnablePlayerEvent())
					self.is_displaying_dialog = False
					#print "this"
				else:
					self.dialog_counter += 1
	def draw(self, surface):
		if self.is_displaying_dialog and self.current_dialog != None and self.dialog_counter < len(self.current_dialog):
			surface.blit(self.drawSurf, (0,(self.configclass.window_height-self.drawSurf.get_height())) )
    			text = self.font.render(self.current_dialog[self.dialog_counter], 1, (10, 10, 10))
    			surface.blit(text, (0,(self.configclass.window_height-self.drawSurf.get_height())) )
