import gui, pygame

class Screen(gui.Base):
    def __init__ (self, size):
        self.layer = 0
        pygame.init()

        self.image = pygame.display.set_mode (size)
        self.rect = size
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.fill ( (255, 255, 255) )

        gui.def_surf = self
        self._gui_items = pygame.sprite.LayeredUpdates()
        
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
        pass

    def update (self, *args, **kwargs):
        self._gui_items.update(*args, **kwargs)
        
##  Drawing shortcuts
    blit   = gui.Shortcut ("image.blit")
    fill   = gui.Shortcut ("image.fill")
    copy   = gui.Shortcut ("image.copy")
    scroll = gui.Shortcut ("image.scroll")
    lock   = gui.Shortcut ("image.lock")
    unlock = gui.Shortcut ("image.unlock")

    set_at = gui.Shortcut ("image.set_at")
    get_at = gui.Shortcut ("image.get_at")
    
    subsurface = gui.Shortcut ("image.subsurface")
    getsurface = gui.Shortcut ("image")
    

