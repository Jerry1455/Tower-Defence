from views.components.baseComponents.botao import Botao
import pygame as pg
import constantes as c
from midia.access import Midia

class BotaoTorreta(Botao):
    def __init__(self, px, image):
        super().__init__(px, image)
        self.pos = pg.mouse.get_pos()
        self.grupoBandeira = pg.sprite.Group()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def action(self, state, world_state):
        return state

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, event, flag):
       print ("A torre sera colocada em: {} {} ".format(flag.x, flag.y))
