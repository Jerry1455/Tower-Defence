import pygame as pg
import constantes as c


class Torre (pg.sprite.Sprite):
    def __init__(self, px, image):
        pg.sprite.Sprite.__init__(self)
        
        # temporario (colocar em um json depois)
        self.range = 90
        self.cadencia = 1500
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.target = None
        
        self.image = image
        self.x = px[0] - 16
        self.y = px[1] - 16
        self.rect = self.image.get_rect()
        self.rect.topleft = (px[0] - 16, px[1] - 16)
        self.clicado = False
        self.turretType = ""


    def setTurretType(self, turretType):
        self.turretType = turretType
        return self

    def draw(self, screen):
        screen.blit(self.image, self.rect)
