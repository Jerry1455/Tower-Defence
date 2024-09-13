from views.components.baseComponents.botao import Botao
import pygame as pg
import constantes as c
from midia.access import Midia
from importData import ImportData
from models.entities.torre import Torre
import constantes.paletaDeCores as pdc


class BotaoTorreta(Botao):
    def __init__(self, px, image, turretType):
        super().__init__(px, image)
        self.pos = pg.mouse.get_pos()
        self.grupoBandeira = pg.sprite.Group()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.turretType = turretType
        self.data = ImportData()
        self.roudDraw = None
        self.range = 90

        self.rangeImage = pg.Surface((self.range * 2, self.range * 2))
        self.rangeImage.fill(pdc.cinza)
        self.rangeImage.set_colorkey(pdc.cinza)
        pg.draw.circle(self.rangeImage, pdc.cinzaC,
                       (self.range, self.range), self.range)
        self.rangeImage.set_alpha(100)
        self.range_rect = self.rangeImage.get_rect()

    def animate(self):
        self.image.get_height()

    def action(self, state, world_state):
        return state

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.roudDraw:
            screen.blit(self.rangeImage, self.range_rect)

    def update(self, event, flag):
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.range_rect.center = (flag.x, flag.y)
            self.roudDraw = True
        else:
            self.roudDraw = None
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                torre = Torre(
                    (flag.x, flag.y),
                    pg.image.load(self.data.torres()[
                        self.turretType]['torreSprite']).convert_alpha(),
                    pg.image.load(self.data.torres()[self.turretType]['torreSpriteFire']).convert_alpha()).setTurretType(self.turretType)

                torre.price = self.data.torres()[self.turretType]['price']

                torre.damage = self.data.torres()[self.turretType]['damage']

                return True, torre
            return False, None
        return False, None
