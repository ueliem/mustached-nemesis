import pygame
from pygame.locals import *
import os
class ResourceManager():
	def __init__(self):
		self.resourcepath = "GAME/RESOURCES/"
		self.resources = {}
		pass
	def load_image(self, filename):
		image = pygame.image.load(os.path.join(self.resourcepath, filename))
		self.resources[filename] = image
		return image
	def load_image_alpha(self, filename):
		image = pygame.image.load(os.path.join(self.resourcepath, filename)).convert_alpha()
		self.resources[filename] = image
		return image
	def load_file(self, filename):
		f = open(os.path.join(self.resourcepath, filename))
		self.resources[filename] = f
		return f
	def load_file_as_string(self, filename):
		f = open(os.path.join(self.resourcepath, filename))
		stringf = f.readlines()
		self.resources[filename] = stringf
		f.close()
		return stringf
