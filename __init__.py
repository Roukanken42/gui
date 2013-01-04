import gui.event, pygame, sys, collections, types

def_surf = None

def _get (obj, name):
    if len(name) == 1: return getattr(obj, name[0])
    return _get(getattr(obj, name[0]), name[1:])

def _set (obj, name, value):
    if len(name) == 1:
        setattr(obj, name[0], value)
        return
    
    _set(getattr(obj, name[0]), name[1:], value)


class Shortcut:
    def __init__ (self, name):
        self.name = name.split(".")

    def __get__ (self, obj, objtype=None):
        return _get (obj, self.name)

    def __set__ (self, obj, value):
        _set(obj, self.name, value)
        obj.changed = True



def membermethod (obj):
    def add (func):
        boundmethod = types.MethodType(func, obj)
        obj.__setattr__(func.__name__, boundmethod)
        
        return func    
    return add

class Base (pygame.sprite.Sprite):
    def __init__ (self, parent = None, layer = 100):
        self.layer = layer
        self.parent = parent

        if self.parent is None:
            self.parent = def_surf

        #gui.event.regListen(self)
        pygame.sprite.Sprite.__init__(self)
        self.parent._gui_items.add (self, layer= self.layer)

    def delete (self):
        gui.event.delListen(self)

    def changeattr (self, **kwargs):
        for name, value in kwargs.items():
            if (hasattr(self, name)):
                setattr (self, name, value)
    
import gui.button
import gui.window

def update (*args, **kwargs) :
    x = pygame.event.Event(pygame.USEREVENT, ID = gui.event.UPDATE)
    pygame.event.post (x)
    gui.event.pull()
    def_surf.update(*args, **kwargs)
    def_surf.draw()
    


def loop ():
    while(True):
        update()






class Screen(gui.Base):
    def __init__ (self, size):
        global def_surf
        self.layer = 0
        pygame.init()

        self.image = pygame.display.set_mode (size)
        self.rect = size
        self.fps = 30
        self.clock = pygame.time.Clock()

        def_surf = self
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
