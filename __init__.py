import gui.event, pygame, sys, collections, types, os

def_surf = None
path = os.path.dirname(gui.__file__)

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
import gui.screen
import gui.button
import gui.window
