import pygame, os, sys
from pygame.locals import *

import GAME.ENTITIES.listener

class DialogManager(GAME.ENTITIES.listener.BaseListener):
	def __init__(self):
		pass
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			pass
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.DialogEvent):
			pass
		elif isinstance(event, GAME.EVENTMANAGER.eventmanager.KeyPressEvent):
			pass
