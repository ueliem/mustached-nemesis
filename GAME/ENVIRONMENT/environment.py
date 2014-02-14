import GAME.ENTITIES.listener

class Environment(GAME.ENTITIES.listener.BaseListener):
	def __init__(self, eventmanager, configclass, gamemap):
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
		self.gamemap = gamemap
		self.collisionmap = []
		self.entities = []
	def listen(self, event):
		if isinstance(event, GAME.EVENTMANAGER.eventmanager.TickEvent):
			#self.create_collison_map()
			#print "#####"
			pass

	def create_collison_map(self):
		intermediatemap = []
		#add collisions of all entities
		#print len(self.entities)

		for y in range(self.gamemap.height):
			tmp = []
			for x in range(self.gamemap.width):
				if (self.gamemap.collisions[y][x] == "1"):
					tmp.append("1")
				elif (self.gamemap.collisions[y][x] == "0"):
					tmp.append("0")
			intermediatemap.append(tmp)
		#print intermediatemap
		for i in range(len(self.entities)):
			intermediatemap[self.entities[i].ygrid][self.entities[i].xgrid] = 1
		#print intermediatemap
		return intermediatemap

	def add_entity(self, e):
		self.entities.append(e)
	def draw(self, surface, offset):
		self.entities.sort(key=lambda x: x.ygrid, reverse=False)
		surface.blit(self.gamemap.drawSurf, offset)#(0,0))#self.gamemap.draw()
		for i in range(len(self.entities)):
			self.entities[i].draw(surface, offset)
