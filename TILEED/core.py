import pygame, os, sys
from pygame.locals import *

#####################################
import GAME.STATES.states
import GAME.RESOURCES.resourcemanager
import GAME.EVENTMANAGER.eventmanager
import GAME.window
import GAME.gameclock
import GAME.ENTITIES.listener
import GAME.ENTITIES.baseentity
#####################################
import GAME.CONTROL.keyboard
import GAME.CONTROL.mouse
import TILEMAP.core
#####################################

class Editor():
	def __init__(self, window, resourcemanager, eventmanager, configclass):
		self.name = "TILE EDITOR"
		pygame.display.set_caption(self.name)
		self.window = window
		self.resourcemanager = resourcemanager
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
		self.keyboardcontrol = GAME.CONTROL.keyboard.KeyboardControl(self.eventmanager, self.configclass)
		self.mousecontrol = GAME.CONTROL.mouse.MouseControl(self.eventmanager, self.configclass)
		self.drawSurf = pygame.Surface((window.width,window.height))
		self.map = TILEMAP.core.Map(self.resourcemanager.load_file_as_string("MAPF/map1.txt"), self.resourcemanager.load_file_as_string("MAPC/map1c.txt"), self.resourcemanager.load_image("TILESHEETS/map1.png"))
		self.pallette = TilePallette(self.eventmanager, self.configclass)
		self.pallette.load_resources(self.resourcemanager)
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			self.draw()
			self.window.screen.blit(self.drawSurf, (0,0))
			self.window.refresh()
		#elif isinstance(event, GAME.EVENTMANAGER.eventmanager.LeftMousePressEvent):
		#	print "Click" #MAKE THIS CHOOSE A SPOT ON SCREEN
	def draw(self):
		self.drawSurf.fill((0,0,0))
		self.pallette.draw(self.drawSurf, (0,0))
		#self.map.draw(self.drawSurf, (0,0))
		#self.drawSurf.blit(self.map.drawSurf, (0,0))

class TilePallette(GAME.ENTITIES.baseentity.BaseEntity):
	def __init__(self, eventmanager, configclass):
		self.tilesheet = None
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
		#self.gamemap = gamemap
		self.drawSurf = pygame.Surface((24,32), SRCALPHA)
		self.xgrid = None
		self.ygrid = None
		self.cur_selected = None
	def listen(self, event):
		pass
	def load_resources(self, resourcemanager):
		self.tilesheet = resourcemanager.load_image("TILESHEETS/map1.png")
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.LeftMousePressEvent):
			self.cur_selected = Rect((event.pos[0] / self.configclass.tilesize)*self.configclass.tilesize, (event.pos[1] / self.configclass.tilesize)*self.configclass.tilesize, self.configclass.tilesize, self.configclass.tilesize)
			#print self.cur_selected
	def draw(self, surface, offset):
		surface.blit(self.tilesheet, (0,0))
		#print "drawing1"
		if self.cur_selected != None:
			#print "drawing2"
			pygame.draw.rect(surface, (255,255,255), self.cur_selected, 0)

class MapDisplay():
	def __init__(self):
		self.map = None
	def load_map(mapdata):
		pass
	def render_map_region(x, y, width, height):
		pass



class TileEditor():
	def __init__(self, configclass):
		self.configclass = configclass
		self.TICKSIZE = 20
		pygame.init()#move this to main?
		self.eventmanager = GAME.EVENTMANAGER.eventmanager.EventManager()
		self.keyboardcontrol = GAME.CONTROL.keyboard.KeyboardControl(self.eventmanager, self.configclass)
		#self.window = GAME.window.GameWindow(self.configclass.window_width, self.configclass.window_height)
		self.window = GAME.window.GameWindow(800, 512)
		self.editor = Editor(self.window, GAME.RESOURCES.resourcemanager.ResourceManager(), self.eventmanager, self.configclass)
		self.mapdisplay = MapDisplay()
		self.gameclock = GAME.gameclock.GameClock(self.eventmanager)
		self.running = True
	def start(self):
		self.run()
	def run(self):
		self.gameclock.run()
	def stop(self):
		self.running = False
