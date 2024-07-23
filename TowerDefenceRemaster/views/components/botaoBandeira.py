from views.components.baseComponents.botao import Botao
import pygame as pg
import constantes as c

class BotaoBandeira(Botao):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.pos = pg.mouse.get_pos()
        self.grupoBandeira = pg.sprite.Group()  
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
   ## def drawBandeiras(self, surface):
        
        