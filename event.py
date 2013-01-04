import pygame, gui

UPDATE = 33


listeners = []
func_names  = {pygame.QUIT            : "_onQuit",
               pygame.MOUSEBUTTONUP   : "_onMouseButtonUp",
               pygame.MOUSEBUTTONDOWN : "_onMouseButtonDown",
               pygame.MOUSEMOTION     : "_onMouseMotion",
               pygame.KEYDOWN         : "_onKeyDown",
               pygame.KEYUP           : "_onKeyUp",
               UPDATE                 : "_onUpdate"
               }

def handleEvent (event, elem):
    toplayer = -1
    for obj in elem._gui_items.sprites()[::-1]:
        temp = notifyObject (obj, event, toplayer)
        if toplayer == -1 : toplayer = temp
        
def notifyObject (obj, event, toplayer):
    try :
        if (event.type == pygame.USEREVENT):
            event = pygame.event.Event(event.ID, event.dict)
        name = func_names[event.type]
    except KeyError:
        return -1

    
    if not hasattr(obj, name): return -1 
    return obj.__getattribute__(name)(event, toplayer)
    
def pull ():
    for event in pygame.event.get():
        notifyObject (gui.def_surf, event, -1)
        handleEvent  (event, gui.def_surf)

