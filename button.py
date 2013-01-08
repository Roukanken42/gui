import gui, pygame, collections, abc

STATE_NORMAL   = 0
STATE_DISABLED = 1
STATE_PRESSED  = 2

DEFAULT_GRAPHIC = {STATE_NORMAL   : pygame.surface.Surface((500, 500)),
                   STATE_DISABLED : pygame.surface.Surface((500, 500)),
                   STATE_PRESSED  : pygame.surface.Surface((500, 500))
                   }

DEFAULT_GRAPHIC[STATE_NORMAL  ].fill((255, 0,   0))
DEFAULT_GRAPHIC[STATE_DISABLED].fill((150, 50, 50))
DEFAULT_GRAPHIC[STATE_PRESSED ].fill((255, 100, 0))


class Button (gui.Base, gui.template.Movable):

    def __init__ (self, parent = None, layer = 100):
        """Button constructor"""
        gui.Base.__init__(self, parent, layer = layer)
        gui.template.Movable.__init__(self, pygame.rect.Rect(0, 0, 150, 50))

        self._caption = type(self).__name__
        self.graphic = DEFAULT_GRAPHIC
        
        self._font = pygame.font.Font("Vera.ttf", 12)

        self._visible = True
        self._pressed = False
        self._enabled = True

        self.changed = True

        self.update_img()
        
    def update_img (self):
        """Internal function for drawing Button"""
        self.changed = False
        
        self.image = pygame.surface.Surface(self.rect.size)
        self.image.blit(self.graphic[self.getState()].copy(), self.image.get_rect())

        text = self.font.render(self.caption, True, (0, 0, 0))              #TODO >> color
        textrect = text.get_rect()
        textrect.center = self.image.get_rect().center
        
        self.image.blit(text, textrect)
        if not self.visible:
            self.image.fill ((255, 255, 255))
            self.image.set_colorkey ((255, 255, 255))

    def update (self, *args, **kwargs):
        """Update and Draw hook"""
        if (self.changed): self.update_img()
    
    def getState (self) :
        if not self.enabled: return STATE_DISABLED
        if self.pressed: return STATE_PRESSED
        return STATE_NORMAL
    
    def _onMouseButtonDown (self, event, toplayer):
        if not toplayer == -1: return -1
        if not self.rect.collidepoint(event.pos): return -1
        if not event.button == 1 : return self.layer
        if not self.enabled : return self.layer 
        
        self.pressed = True        
        self.onMouseButtonDown(event)
        return self.layer

    def onMouseButtonDown (self, event):
        pass
       
    def _onMouseButtonUp  (self, event, toplayer):
        if not self.pressed : return -1
        if not event.button == 1 : return self.layer
        
        self.pressed = False
        if not self.rect.collidepoint(event.pos): return self.layer
        if not self.enabled : return self.layer
        
        self.onMouseButtonUp(event)

        return self.layer
    
    def onMouseButtonUp (self, event):
        pass    


    def _onMouseMotion (self, event, toplayer):
        if self.pressed: self.onDrag (event)


    def onDrag (self, event):
        pass
    
##  Shorcuts for updating
    caption = gui.Shortcut ("_caption")
    visible = gui.Shortcut ("_visible")
    pressed = gui.Shortcut ("_pressed")
    enabled = gui.Shortcut ("_enabled")
    font    = gui.Shortcut ("_font")
