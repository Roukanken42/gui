import gui, pygame, collections, abc

class Movable:

    def __init__ (self, rect):
        self._rect = rect

    
    
##  Shortcuts for positioning and moving (aka. rect modifying)
    rect = gui.Shortcut ("_rect")
    
    bottomleft  = gui.Shortcut ("_rect.bottomleft")
    topleft     = gui.Shortcut ("_rect.topleft")
    bottomright = gui.Shortcut ("_rect.bottomright")
    topright    = gui.Shortcut ("_rect.topright")

    midbottom = gui.Shortcut ("_rect.midbottom")
    midtop    = gui.Shortcut ("_rect.midtop")
    midleft   = gui.Shortcut ("_rect.midleft")
    midright  = gui.Shortcut ("_rect.midright")

    centerx = gui.Shortcut ("_rect.centerx")
    centery = gui.Shortcut ("_rect.centery")
    height  = gui.Shortcut ("_rect.height")
    width   = gui.Shortcut ("_rect.width")
    
    bottom = gui.Shortcut ("_rect.bottom")
    left   = gui.Shortcut ("_rect.left")
    right  = gui.Shortcut ("_rect.right")
    top    = gui.Shortcut ("_rect.top")
    center = gui.Shortcut ("_rect.center")
    size   = gui.Shortcut ("_rect.size")

    move = gui.Shortcut ("_rect.move")
    
