import pygame, os, sys
from pygame.locals import *
class GameWindow():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width,height), 0, 0)
		pygame.display.set_caption("Starting up...")
		self.background = pygame.Surface((width,height))
		self.background.fill((0,0,0))
		self.screen.blit(self.background, (0,0))	
		pygame.display.flip()
	def change_caption(self, caption):
		pygame.display.set_caption(caption)
	def refresh(self):
		#self.screen.blit(self.background, (0,0))
		pygame.display.flip()
	def trigger_close(self):
		sys.exit()
