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
