import gui, pygame

class Label (gui.Base, gui.template.Movable):
    def __init__ (self, layer=100, parent=None):
        gui.Base.__init__ (self, layer=layer, parent=parent)
        gui.template.Movable.__init__ (self, pygame.rect.Rect(0, 0, 10, 12))

        self.text = type(self).__name__
        self.font = pygame.font.Font(gui.resource("Vera.ttf"), 12)
        self.color = (0, 0, 0)
        self.size = self.font.size(self.text)
        self.image = self.font.render(self.text, True, self.color)


    def update (self):
        if self.changed:
            self.size = self.font.size(self.text)
            self.image = self.image = self.font.render(self.text, True, self.color)
        
        

        
##  Update shotcuts
    text    = gui.Shortcut ("_text")
    caption = gui.Shortcut ("_text")
    font    = gui.Shortcut ("_font")
    color   = gui.Shortcut ("_color")
    
