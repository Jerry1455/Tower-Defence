from views.components.baseComponents.botao import Botao
import pygame as pg
import constantes as c
from midia.access import Midia
from importData import ImportData
from models.entities.torre import Torre

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

    def action(self, state, world_state):
        return state

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, event, flag):
        if self.rect.collidepoint(event.pos):
            return True, Torre(
                (flag.x, flag.y),
                pg.image.load(self.data.torres()[
                    self.turretType]['torreSprite']).convert_alpha()).setTurretType(self.turretType)
        return False, None
