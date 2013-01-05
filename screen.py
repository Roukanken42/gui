import gui, pygame

class Screen(gui.Base):
    def __init__ (self, size):
        self.layer = 0
        pygame.init()

        self.image = pygame.display.set_mode (size)
        self.rect = size
        self.fps = 30
        self.clock = pygame.time.Clock()

        gui.def_surf = self
        self._gui_items = pygame.sprite.LayeredUpdates()
    
    def __hash__ (self):
        return hash(id(self))
        
    def _onMouseButtonUp (self, event, layer):
        if not layer == -1: return -1
        self.onMouseButtonUp (event)

    def onMouseButtonUp (self, event):
        pass
    
    def _onQuit (self, event, layer):
        if (self.onQuit(event)) :
            pygame.quit()
            sys.exit()

    def onQuit (self, event) :
        return True

    def __str__ (self):
        return repr (self)

    def __repr__ (self) :
        return "<Screen object>"

    def draw (self):
        self._gui_items.draw(self.image)

        pygame.display.update()
        self.clock.tick(self.fps)


    def _onUpdate (self, event, toplayer):
        self.onUpdate(event)
        return -1
        
    def onUpdate (self, event):
        self.fill((255, 255, 255))

    def update (self, *args, **kwargs):
        self._gui_items.update(*args, **kwargs)
        
##  Drawing shortcuts
    blit   = gui.Shortcut ("image.blit")
    fill   = gui.Shortcut ("image.fill")

