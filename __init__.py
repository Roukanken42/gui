import gui.event, pygame, sys, collections, types, os

def_surf = None
path = os.path.dirname(gui.__file__)


def resource (filename):
    return os.path.join (path, "resources", filename)


def _set (obj, name, value):
    if len(name) == 1:
        setattr(obj, name[0], value)
        return
    
    _set(getattr(obj, name[0]), name[1:], value)


class Shortcut:
    def __init__ (self, name):
        self.name = name.split(".")

    def __get__ (self, obj, objtype=None):
        for name in self.name:
            obj = getattr(obj, name)

        return obj

    def __set__ (self, obj, value):
        for i, name in enumerate(self.name):
            if (i == len(self.name) -1): break
            
            obj = getattr(obj, name)

        setattr(obj, self.name[-1], value)

class Base (pygame.sprite.DirtySprite):
    def __init__ (self, parent = None, layer = 100):
        self.layer = layer
        self.parent = parent

        if self.parent is None:
            self.parent = def_surf

        #gui.event.regListen(self)
        pygame.sprite.Sprite.__init__(self)
        self.parent._gui_items.add (self, layer= self.layer)

    def changeattr (self, **kwargs):
        for name, value in kwargs.items():
            if (hasattr(self, name)):
                setattr (self, name, value)

    def event (self, func): 
        boundmethod = types.MethodType(func, self)
        self.__setattr__(func.__name__, boundmethod)



def update (*args, **kwargs) :
    x = pygame.event.Event(pygame.USEREVENT, ID = gui.event.UPDATE)
    pygame.event.post (x)
    gui.event.pull()
    def_surf.update(*args, **kwargs)
    def_surf.draw()
    


def loop ():
    while(True):
        update()
        
import gui.template
import gui.image
import gui.label
import gui.screen
import gui.button
import gui.window
import gui.choice
