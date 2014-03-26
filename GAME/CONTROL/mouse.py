import sys
import pygame
from pygame.locals import *

import GAME.ENTITIES.listener
import GAME.EVENTMANAGER.eventmanager

class MouseControl:
	def __init__(self, eventmanager, configclass):
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			pygame.event.pump()
			for entry in pygame.event.get():
				if entry.type == QUIT:
					sys.exit()
				elif entry.type == MOUSEBUTTONDOWN:
					e = GAME.EVENTMANAGER.eventmanager.LeftMousePressEvent(entry.pos)
					self.eventmanager.inform(e)
