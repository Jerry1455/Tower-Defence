import pygame as pg
import constantes as c
import constantes.paletaDeCores as pdc


class Torre (pg.sprite.Sprite):
    def __init__(self, px, image):
        pg.sprite.Sprite.__init__(self)
        
        # temporario (colocar em um json depois)
        self.range = 90
        self.cadencia = 1500
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.target = None
        
        self.x = px[0] 
        self.y = px[1] 
        
        # Criar circulo 
        self.rangeImage = pg.Surface((self.range *2, self.range * 2))
        self.rangeImage.fill(pdc.cinza)
        self.rangeImage.set_colorkey(pdc.cinza)
        pg.draw.circle(self.rangeImage, pdc.cinzaC, (self.range,self.range), self.range)
        self.rangeImage.set_alpha(100)
        self.range_rect = self.rangeImage.get_rect()
        self.range_rect.center = (self.x , self.y)
        
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.clicado = False
        self.turretType = ""

    def setTurretType(self, turretType):
        self.turretType = turretType
        return self

    def draw(self, screen):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)
        self.pos = pg.mouse.get_pos()
        if self.rect.collidepoint(self.pos):
            screen.blit(self.rangeImage, self.range_rect)
