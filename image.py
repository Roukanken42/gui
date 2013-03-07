import gui, pygame

class Image (gui.Base, gui.template.Movable):
    def __init__ (self, layer = 20, parent = None, size = (100, 100)):
        gui.Base.__init__ (self, parent = parent, layer = layer)
        self.rect = pygame.rect.Rect((20, 20), size)
        self.image = pygame.surface.Surface(self.rect.size)

        self.visible = True
        self.drag = False

    def draw (self):
        pass

    @property
    def size (self):
        return size

    @size.setter
    def size (self, new):
        temp = pygame.surface.Surface(new)
        temp.blit(self.image, (0, 0))
        self.image = temp
        self.rect.size = new

    def _onMouseButtonDown (self, event, toplayer):
        if not toplayer == -1: return -1
        if not self.rect.collidepoint(event.pos): return -1
        if not self.visible: return -1
        
        self.drag = True

        eventpos = event.pos
        event.pos = (event.pos[0] - self.left, event.pos[1] - self.top)

        self.drag_begin = event.pos
        self.onMouseButtonDown (event)

        event.pos = eventpos

        return self.layer

    def onMouseButtonDown (self, event):
        pass

    def _onMouseButtonUp (self, event, toplayer):
        self.drag = False
        
        if not toplayer == -1: return -1
        if not self.rect.collidepoint(event.pos): return -1
        if not self.visible: return -1

        eventpos = event.pos
        event.pos = (event.pos[0] - self.left, event.pos[1] - self.top)
       
        self.onMouseButtonUp (event)

        event.pos = eventpos

        self.drag_begin = (0, 0)
        return self.layer

    def onMouseButtonUp (self, event):
        pass

    
    def _onMouseMotion (self, event, toplayer):
        eventpos = event.pos
        event.pos = (event.pos[0] - self.left, event.pos[1] - self.top)
        
        if self.drag: self.onDrag (event)

        if not toplayer == -1: return -1
        if not self.rect.collidepoint(event.pos): return -1
        if not self.visible: return -1

        self.onMouseMotion(event)

        event.pos = eventpos
        
    def onDrag (self, event):
        pass

    def onMouseMotion (self, event):
        pass
            
    blit   = gui.Shortcut ("image.blit")
    fill   = gui.Shortcut ("image.fill")
    scroll = gui.Shortcut ("image.scroll")
    lock   = gui.Shortcut ("image.lock")
    unlock = gui.Shortcut ("image.unlock")

    set_at = gui.Shortcut ("image.set_at")
    get_at = gui.Shortcut ("image.get_at")

    visible = gui.Shortcut ("_visible")
    

    
        
