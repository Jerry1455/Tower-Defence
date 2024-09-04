import pygame as pg
import constantes.paletaDeCores as pdc
import constantes as c
from midia.access import Midia


class Torre (pg.sprite.Sprite):
    def __init__(self, px, image, shotImage):
        pg.sprite.Sprite.__init__(self)
        self.animation = []
        self.shotAnimation = []
        self.setShotAnimation (shotImage)
        self.animationCooldown = 0
        self.setAnimation(image)
        self.actualFrame = 0
        self.midia = Midia()
        self.image = self.midia.img_pistola

        # temporario (colocar em um json depois)
        self.range = 90
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.coldownTimeDefault = 30
        self.x = px[0]
        self.y = px[1]
        self.coldownTime = self.coldownTimeDefault
        self._target = None
        self.target = None
        self.upgradeMenu = False
        
        self.price = 10
        # Criar circulo
        self.rangeImage = pg.Surface((self.range * 2, self.range * 2))
        self.rangeImage.fill(pdc.cinza)
        self.rangeImage.set_colorkey(pdc.cinza)
        pg.draw.circle(self.rangeImage, pdc.cinzaC,
                       (self.range, self.range), self.range)
        self.rangeImage.set_alpha(100)
        self.range_collide = self.rangeImage.get_rect()
        self.range_collide.center = (self.x, self.y)

        self.clicado = False
        self.turretType = ""
        self.coldowAnimation = 10

    def setTurretType(self, turretType):
        self.turretType = turretType
        return self

    def setShotAnimation(self, image):
        if image.get_height() > c.TAMANHO_QUADRADO:
            self.shotFrames = round(image.get_height() / c.TAMANHO_QUADRADO)
            for i in range(0, self.shotFrames):
                frame = pg.transform.scale_by(image.subsurface(
                    0, i * c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO), c.MULTI)
                self.shotAnimation.append(frame)
                self.image = frame
            self.shotFrames = len(self.shotAnimation)

        return image

    def setAnimation(self, image):
        if image.get_height() > c.TAMANHO_QUADRADO:
            self.frames = round(image.get_height() / c.TAMANHO_QUADRADO)
            for i in range(0, self.frames):
                frame = pg.transform.scale_by(image.subsurface(
                    0, i * c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO), c.MULTI)
                self.animation.append(frame)
                self.image = frame
            self.frames = len(self.animation)

        return image

    def animate(self):
        self.actualFrame += 1
        if self.target != None:
            if self.actualFrame >= self.frames:
                self.actualFrame = 0
        else:
            if self.actualFrame >= self.shotFrames:
                self.actualFrame = 0

    def draw(self, screen):
        if self.target != None:
            if len(self.shotAnimation) <= self.actualFrame:
                self.actualFrame = 0
            self.image = self.shotAnimation[self.actualFrame]
            self.rect = self.animation[self.actualFrame].get_rect()
        else:
            self.image = self.animation[self.actualFrame]
            self.rect = self.animation[self.actualFrame].get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)

        self.pos = pg.mouse.get_pos()

        if self.rect.collidepoint(self.pos):
            screen.blit(self.rangeImage, self.range_collide)

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target):
        if self._target is None:
            self.coldownTime = self.coldownTimeDefault
        self._target = target

    def shotTarget(self):
        if self.target is not None:
            if self.coldownTime < 1:
                self.target.vida -= 1
                self.coldownTime = self.coldownTimeDefault
                return self.target
            else:
                self.coldownTime -= 1
                return self.target

        return self.target
