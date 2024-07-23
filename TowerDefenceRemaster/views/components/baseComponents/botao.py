import pygame as pg
import constantes as c


class Botao (pg.sprite.Sprite):
    def __init__(self, px, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.x = px[0]
        self.y = px[1]
        self.rect = self.image.get_rect()
        self.rect.topleft = (px[0], px[1])
        self.clicado = False
