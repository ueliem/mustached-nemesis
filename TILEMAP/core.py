import sys, os
import pygame
from pygame.locals import *

"""class Map():
	def __init__(self, mapfile, tilesheet):
		self.mapfile = mapfile
		self.tilesheet = tilesheet
	def render(self):
		pass

"""
class Map:
    def __init__(self, fl, fc, tl):
		self.f = fl
		self.fc = fc
		self.tilesheet = tl
		self.coords = []

		widthheight = self.f[0]
		tmp = widthheight.split("x", 1)
		self.width = int(tmp[0])
		self.height = int(tmp[1])

		self.drawSurf = pygame.Surface((self.width*16, self.height*16))

		for i in range(1, self.height+1):
			line = self.f[i]
			line = line.strip("\n")
			line = line.strip("\r")
			tmplist = line.split(",", self.width)

			self.coords += tmplist
	
		for x in range(self.height):
			for y in range(self.width):
				tmpstr = str(self.coords[y + self.width*x]).strip("(")
				tmpstr = tmpstr.strip(")")
				clist = tmpstr.split(".", 1)
				xdist = 16 * int(clist[0])
				ydist = 16 * int(clist[1])
				tileRect = Rect(xdist, ydist, 16, 16)
				self.drawSurf.blit(self.tilesheet, (16*y, 16*x), tileRect)

		self.collisions = []
		for i in range(self.height):
			line = self.fc[i]
			line = line.strip("\n")
			line = line.strip("\r")
			tmplist = line.split(",", self.width)
			#print tmplist
			self.collisions.append(tmplist)

		#print self.collisions
    def update(self):
		pass
