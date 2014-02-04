import sys, os
import pygame
from pygame.locals import *
import threading
import GAME.ENTITIES.listener
import GAME.EVENTMANAGER.eventmanager

class GameClock(GAME.ENTITIES.listener.BaseListener, threading.Thread):
    def __init__(self, eventmanager):
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.TICKSIZE = 20
		self.running = True
		self.time = pygame.time.get_ticks()
    def run(self):
		while self.running:
			curTime = pygame.time.get_ticks()
			if curTime - self.time > self.TICKSIZE:
				self.time = curTime
				ev = GAME.EVENTMANAGER.eventmanager.TickEvent()
				self.eventmanager.inform(ev)
				#print "yay"
    def stop(self):
		self.running = false
	#def queue_event(self):
	#	pass
