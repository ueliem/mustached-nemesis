import pygame
from pygame.locals import *

import GAME.EVENTMANAGER.eventmanager
import GAME.ENTITIES.listener
import GAME.ENTITIES.player
import GAME.ENTITIES.testnpc
import GAME.ENVIRONMENT.environment
import TILEMAP.core

class BaseState(GAME.ENTITIES.listener.BaseListener):
	def __init__(self):
		self.name = None
		self.drawSurf = pygame.Surface((480,320))
	def start(self):
		pass
	def run(self):
		pass
	def pause(self):
		pass
	def listen(self, event):
		pass

class SplashScreenState(BaseState):
	def __init__(self, window, resourcemanager, eventmanager, configclass):
		#super(SplashScreenState, self).__init__()
		self.name = None
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.window = window
		self.resourcemanager = resourcemanager
		self.configclass = configclass
		self.drawSurf = pygame.Surface((window.width,window.height))
		self.image = self.resourcemanager.load_image("MISC/titlescreen.png")
		self.drawSurf.blit(self.image, (0,0))
		self.draw_to_self()
		self.draw_to_screen()
	def start(self):
		pass
	def run(self):
		pass
	def pause(self):
		pass

	def update(self):
		pass
	def draw_to_self(self):
		self.drawSurf.fill((0,0,0))
		self.drawSurf.blit(self.image, (0,0))
	def draw_to_screen(self):
		self.window.screen.blit(self.drawSurf, (0,0))
		self.window.refresh()
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			#print "received"
			pygame.event.pump()
			for entry in pygame.event.get():
				if entry.type == QUIT:
					sys.exit()
				elif entry.type == KEYDOWN:
					#if entry.key == K_UP:
					pass
				else:
					pass

class OverworldState(BaseState):
	def __init__(self, window, resourcemanager, eventmanager, configclass):
		self.name = "OVERWORLD STATE"
		pygame.display.set_caption(self.name)
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.window = window
		self.resourcemanager = resourcemanager
		self.configclass = configclass
		self.drawSurf = pygame.Surface((window.width,window.height))

		self.scrollx = 0.0
		self.scrolly = 0.0
		#self.ableToMove = True
		#self.moving = False
		#self.direction = self.configclass.DIRECTION_DOWN

		#self.counter = 0
		#self.threshold = 1
		#self.tileSoFar = 0

		self.map = TILEMAP.core.Map(self.resourcemanager.load_file("MAPF/map1.txt"), self.resourcemanager.load_file("MAPC/map1c.txt"), self.resourcemanager.load_image("TILESHEETS/map1.png"))
		#self.drawSurf.blit(self.map.drawSurf, (self.scrollx,self.scrolly))
		self.environment = GAME.ENVIRONMENT.environment.Environment(self.eventmanager, self.configclass, self.map)
		self.player = GAME.ENTITIES.player.Player(self.resourcemanager.load_image_alpha("CHARSHEETS/playerchar.png"), self.eventmanager, self.configclass, self.environment)
		#self.drawSurf.blit(self.player.drawSurf, (108,64))
		self.testperson = GAME.ENTITIES.testnpc.TestNPC(self.resourcemanager.load_image_alpha("CHARSHEETS/playerchar.png"), self.eventmanager, self.configclass, self.environment)
		#################
		
		self.environment.add_entity(self.player)
		self.environment.add_entity(self.testperson)
		#################
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			#print "received"
			#self.update()
			self.draw()
			self.window.screen.blit(self.drawSurf, (0,0))
			self.window.refresh()

	def draw(self):
		self.scrollx = self.player.xpos
		self.scrolly = self.player.ypos
		#self.drawSurf.blit(self.map.drawSurf, (0,0))#(self.scrollx,self.scrolly))
		#self.player.update(self.direction, self.tileSoFar)
		#self.drawSurf.blit(self.player.drawSurf, ((self.player.xpos) - 4, self.player.ypos + 16))#(108,64))#(-1 * self.player.xpos, -1 * self.player.ypos))#(108,64))
		#self.drawSurf.blit(self.testperson.drawSurf, ((self.testperson.xpos) - 4, self.testperson.ypos + 16))#(108,64))#(-1 * self.player.xpos, -1 * self.player.ypos))#(108,64))
		self.environment.draw(self.drawSurf)



