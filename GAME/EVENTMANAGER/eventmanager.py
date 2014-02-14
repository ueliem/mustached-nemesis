class Event:
    def __init__(self):
		self.text = "Event"

"""class PersistantEvent(Event):
	def __init__(self):
		self.text = "Persistant Event"
"""

class TickEvent(Event):
    def __init__(self):
		self.text = "Tick"

class KeyPressEvent(Event):
    def __init__(self, key):
		self.text = "KeyPress"
		self.key = key

class InteractionEvent(Event):
    def __init__(self, initiator, targetxgrid, targetygrid):
		self.text = "Interaction Event"
		self.initiator = initiator
		self.targetxgrid = targetxgrid
		self.targetygrid = targetygrid

class DialogEvent(Event):
    def __init__(self, talker, talkedto, dialogfile):
		self.text = "Dialog Event"
		self.talker = talker
		self.talkedto = talkedto
		self.dialogfile = dialogfile
	
class EnablePlayerEvent(Event):
	def __init__(self):
		self.text = "Enable Player Event"

class EventManager:
    def __init__(self):
		self.listeners = []
    def addListener(self, listener):
		self.listeners.append(listener)
		print "added listener"
    def removeListener(self, listener):
		self.listeners.remove([listener])
		print "removed listener"
    def inform(self, event):
		for listener in self.listeners:
	    		listener.listen(event)
