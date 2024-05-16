import pygame as pg
import constantes as c

class Torre (pg.sprite.Sprite):
    def __init__(self, image, QuadX, QuadY):
        pg.sprite.Sprite.__init__(self)
        self.QuadX = QuadX
        self.QuadY = QuadY
        self.x = (self.QuadX + 0.5) * c.TAMANHO_QUADRADO
        self.y = (self.QuadY + 0.5) * c.TAMANHO_QUADRADO
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        