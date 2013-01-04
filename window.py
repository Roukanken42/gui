import pygame, gui

BTN_CLOSE_GRAPHIC = {gui.button.STATE_NORMAL : pygame.image.load("C:/Python32/MyLibs/gui/resources/close_button_normal.png"),
                     gui.button.STATE_PRESSED: pygame.image.load("C:/Python32/MyLibs/gui/resources/close_button_pressed.png")
                     }

class Window (gui.Base) :
    def __init__ (self, size, parent = None, layer = 1000):
        gui.Base.__init__(self, parent, layer)

        self.title  = "New window"
        self._size   = size

        self._gui_items = pygame.sprite.LayeredUpdates()
        self.d_rect = pygame.rect.Rect (1, 20, self.size[0] + 1, self.size[1]+20)
        self.rect   = pygame.rect.Rect (0,  0, self.size[0] + 2, self.size[1]+21)
        self.rect.topleft = (20, 50)
        self.font = pygame.font.Font("Vera.ttf", 12)
        self.fontrect = pygame.rect.Rect(10, 4, 42, 47)

        
        self.display = pygame.surface.Surface(self.size)
        self.image   = pygame.surface.Surface(self.rect.size)
        self.display.fill((255, 255, 255))
        self.image.fill ((170, 170, 170))

        self.BtnClose = gui.button.Button (parent = self, layer = 1)
        self.BtnClose.graphic = BTN_CLOSE_GRAPHIC
        self.BtnClose.rect = pygame.rect.Rect((0, 0), (16, 16))
        self.BtnClose.topright = self.size[0]-2, 2
        self.BtnClose.caption = ""

        @gui.membermethod(self.BtnClose)
        def onMouseButtonUp (btn, event):
            for comp in self._gui_items.sprites():
                comp.kill()
            self.kill()
            self.closed = True

        self.BtnMove = gui.button.Button (parent = self, layer = 0)
        self.BtnMove.rect = pygame.rect.Rect(0, 0, self.rect.size[0], self.rect.size[1]-self.size[1])
        self.BtnMove.visible = False

        @gui.membermethod (self.BtnMove)
        def onMouseButtonDown(self, event):
            self.drag_begin = event.pos

        @gui.membermethod (self.BtnMove)
        def onDrag (btn, event):
            x = self.rect.topleft[0] + event.pos[0] - btn.drag_begin [0]
            y = self.rect.topleft[1] + event.pos[1] - btn.drag_begin [1]
            self.rect.topleft = x, y
        
    def _onMouseButtonUp (self, event, layer) :
        if not layer == -1 : return -1

        eventpos = event.pos
        event.pos = event.pos[0]-self.rect.topleft[0], event.pos[1]-self.rect.topleft[1] 
        gui.event.handleEvent (event, self)

        event.pos = eventpos
        if self.rect.collidepoint(eventpos): return self.layer
        return -1

    def _onMouseButtonDown (self, event, layer) :
        if not layer == -1 : return -1

        eventpos = event.pos
        event.pos = event.pos[0]-self.rect.topleft[0], event.pos[1]-self.rect.topleft[1] 
        gui.event.handleEvent (event, self)

        event.pos = eventpos
        if self.rect.collidepoint(eventpos): return self.layer
        return -1

    def _onMouseMotion (self, event, layer) :
        if not layer == -1 : return -1

        eventpos = event.pos
        event.pos = event.pos[0]-self.rect.topleft[0], event.pos[1]-self.rect.topleft[1] 
        gui.event.handleEvent (event, self)

        event.pos = eventpos
        if self.rect.collidepoint(eventpos): return self.layer
        return -1
        
    def update (self, *args, **kwargs):
        self.image.fill ((170, 170, 170))
        self.image.blit (self.display, self.d_rect)
        self.__title = self.font.render (self.title, False, (0, 0, 0))
        self.fontrect.size = self.__title.get_rect().size
        self.image.blit (self.__title, self.fontrect)

        self._gui_items.update (*args, **kwargs)
        self._gui_items.draw (self.image)
        
    @property
    def size(self):
        return self._size

    def blit (self, source, dest, area=None, special_flags = 0):
        self.display.blit(source, dest, area, special_flags)
