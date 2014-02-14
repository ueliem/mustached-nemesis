import GAME.ENTITIES.listener

class BaseEntity(GAME.ENTITIES.listener.BaseListener):
	def __init__(self, tl, eventmanager, configclass, gamemap):
		self.tilesheet = tl
		self.eventmanager = eventmanager
		self.eventmanager.addListener(self)
		self.configclass = configclass
		self.gamemap = gamemap
		self.drawSurf = pygame.Surface((24,32), SRCALPHA)
		self.xgrid = None
		self.ygrid = None
	def listen(self, event):
		pass
	def draw(self, surface, offset):
		pass
