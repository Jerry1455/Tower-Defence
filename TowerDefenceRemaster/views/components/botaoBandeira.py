from views.components.baseComponents.botao import Botao
import pygame as pg
import constantes as c
from midia.access import Midia
from .botaoTorreta import BotaoTorreta


class BotaoBandeira(Botao):
    def __init__(self, px, image):
        super().__init__(px, image)
        self.pos = pg.mouse.get_pos()
        self.grupoBandeira = pg.sprite.Group()
        self.image = image
        self.midia = Midia()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.menuOpen = False
        self.menuOpenAction = False
        self.menuCloseAction = False
        self.calculateButtonTurret()
        self.buttonTurrets = []
        self.spritesTurrets = [
            self.midia.img_iconeMGC_btn,
            self.midia.img_iconeDMG_btn,
            self.midia.img_iconeAREA_btn
        ]

    def action(self, state, world_state):
        state['botaoBandeira'] = True
        return state

    def draw(self, screen):
        if self.menuOpenAction == True:

            for buttonPx, image in zip(self.buttonTurretPx, self.spritesTurrets):
                print(buttonPx,image)
                self.buttonTurrets.append(BotaoTorreta(buttonPx, image))
                self.menuOpen = True
                self.menuOpenAction = False

        if self.menuCloseAction and self.menuOpen:
            self.buttonTurrets = []
            self.menuOpen = False
            self.menuCloseAction = False

        if self.buttonTurrets != [] and self.menuOpen == True:

            for buttonTurret in self.buttonTurrets:
                buttonTurret.draw(screen)

        screen.blit(self.image, self.rect)

    def update(self, event):
        pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.buttonTurrets != [] and self.menuOpen:
                for turret in self.buttonTurrets:
                    turret.update(event, self)

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if self.rect.collidepoint(event.pos):
                self.menuOpenAction = True
            else:
                self.menuCloseAction = True

    def calculateButtonTurret(self):



        if self.y < 18:
            self.buttonTurretPx = [
                (self.x - 8, self.y+16+16),
                (self.x + 16, self.y+16+16),
                (self.x + 16, self.y+16+16)
            ]
        else:
            self.buttonTurretPx = [
                (self.x - 8, self.y-16),
                (self.x + 8+16, self.y-16),
                (self.x + 8, self.y-16-16)
            ]
