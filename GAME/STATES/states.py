import pygame
from pygame.locals import *

import GAME.EVENTMANAGER.eventmanager
import GAME.ENTITIES.listener
import GAME.ENTITIES.player
import TILEMAP.core

class GameConstants:
	DIRECTION_NONE = 0
	DIRECTION_UP = 1
	DIRECTION_DOWN = 2
	DIRECTION_LEFT = 3
	DIRECTION_RIGHT = 4
	def __init__(self):
		pass

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
		self.ableToMove = True
		self.moving = False
		self.direction = GameConstants.DIRECTION_DOWN

		self.counter = 0
		self.threshold = 1
		self.tileSoFar = 0

		self.map = TILEMAP.core.Map(self.resourcemanager.load_file("MAPF/map1.txt"), self.resourcemanager.load_file("MAPC/map1c.txt"), self.resourcemanager.load_image("TILESHEETS/map1.png"))
		#self.drawSurf.blit(self.map.drawSurf, (self.scrollx,self.scrolly))
		self.player = GAME.ENTITIES.player.Player(self.resourcemanager.load_image_alpha("CHARSHEETS/playerchar.png"), self.configclass)
		#self.drawSurf.blit(self.player.drawSurf, (108,64))

	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			#print "received"
			pygame.event.pump()
			for entry in pygame.event.get():
				if entry.type == QUIT:
					sys.exit()
				elif entry.type == KEYDOWN:
					#print "received"
					if (not self.moving) and self.ableToMove:
					#print "received"
						if entry.key == K_UP:
							self.direction = GameConstants.DIRECTION_UP
							self.moving = True
						elif entry.key == K_DOWN:
							self.direction = GameConstants.DIRECTION_DOWN
							self.moving = True
						elif entry.key == K_LEFT:
							self.direction = GameConstants.DIRECTION_LEFT
							self.moving = True
						elif entry.key == K_RIGHT:
							self.direction = GameConstants.DIRECTION_RIGHT
							self.moving = True
				else:
					pass
			self.update()
			self.draw()
			self.window.screen.blit(self.drawSurf, (0,0))
			self.window.refresh()

	def update(self):
		if self.moving:
			if self.counter >= self.threshold:
				if self.direction == GameConstants.DIRECTION_UP:
					self.scrolly += 1
				elif self.direction == GameConstants.DIRECTION_DOWN:
					self.scrolly -= 1
				elif self.direction == GameConstants.DIRECTION_LEFT:
					self.scrollx += 1
				elif self.direction == GameConstants.DIRECTION_RIGHT:
					self.scrollx -= 1
				self.tileSoFar += 1
		
				self.counter = 0

				if self.tileSoFar == 16:
					keys = pygame.key.get_pressed()
					if keys[K_UP] and self.direction == GameConstants.DIRECTION_UP:
						self.tileSoFar = 0
					elif keys[K_DOWN] and self.direction == GameConstants.DIRECTION_DOWN:
						self.tileSoFar = 0
					elif keys[K_LEFT] and self.direction == GameConstants.DIRECTION_LEFT:
						self.tileSoFar = 0
					elif keys[K_RIGHT] and self.direction == GameConstants.DIRECTION_RIGHT:
						self.tileSoFar = 0
					else:
						#print "stop moving"
						self.tileSoFar = 0
						self.moving = False
				

			else:
				self.counter += 1
		else:
			pass
	def draw(self):
		self.drawSurf.blit(self.map.drawSurf, (self.scrollx,self.scrolly))
		self.player.update(self.direction, self.tileSoFar)
		self.drawSurf.blit(self.player.drawSurf, (108,64))

