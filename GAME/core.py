import pygame, os, sys
from pygame.locals import *

#####################################
import GAME.STATES.states
import GAME.RESOURCES.resourcemanager
import GAME.EVENTMANAGER.eventmanager
import GAME.window
import GAME.gameclock
import GAME.ENTITIES.listener
#####################################

class Game():
	def __init__(self, configclass):
		self.configclass = configclass
		self.TICKSIZE = 20
		pygame.init()#move this to main?
		self.eventmanager = GAME.EVENTMANAGER.eventmanager.EventManager()
		self.window = GAME.window.GameWindow(self.configclass.window_width, self.configclass.window_height)
		self.splashscreen = GAME.STATES.states.BattleState(self.window, GAME.RESOURCES.resourcemanager.ResourceManager(), self.eventmanager, self.configclass)
		self.gameclock = GAME.gameclock.GameClock(self.eventmanager)
		self.running = True
	def start(self):
		self.run()
	def run(self):
		self.gameclock.run()
	def stop(self):
		self.running = false
