import gui, pygame

class Edit (gui.Base):
    def __init__ (self, layer = 100):
        gui.Base.__init__(self, layer = layer)

        self._text = ""
        
