from views.components.baseComponents.botao import Botao
import pygame as pg
from midia.access import Midia
from .botaoTorreta import BotaoTorreta
import constantes as c


class BotaoBandeira(pg.sprite.Sprite):
    def __init__(self, px, image):
        pg.sprite.Sprite.__init__(self)

        self.pos = pg.mouse.get_pos()
        self.grupoBandeira = pg.sprite.Group()
        self.animation = []
        self.setImage(image)
        self.actualFrame = 0
        self.midia = Midia()
        self.x = px[0]
        self.y = px[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.menuOpen = False
        self.menuOpenAction = False
        self.menuCloseAction = False
        self.calculateButtonTurret()
        self.buttonTurrets = []
        self.spritesTurrets = [
            self.midia.img_iconeDMG_btn,
            self.midia.img_iconeAREA_btn
        ]
        self.turretTypes = [
            'pistola',
            'bomba'
        ]
        self.turret = None
        self.coldowAnimation = 7

    def animate(self):
        self.actualFrame += 1
        if self.actualFrame >= self.frames:
            self.actualFrame = 0

    def setImage(self, image):
        print(image.get_height())
        if image.get_height() > c.TAMANHO_QUADRADO:
            frames = round(image.get_height() / c.TAMANHO_QUADRADO)
            for i in range(0, frames):
                frame = pg.transform.scale_by(image.subsurface(
                    0, i * c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO), c.MULTI)
                self.image = frame
                self.animation.append(frame)
            self.frames = len(self.animation)

    def action(self, state, world_state):
        state['botaoBandeira'] = True
        return state

    def draw(self, screen):
        if self.menuOpenAction == True:

            for buttonPx, image, turretType in zip(self.buttonTurretPx, self.spritesTurrets, self.turretTypes):
                print(buttonPx, image)
                self.buttonTurrets.append(
                    BotaoTorreta(buttonPx, image, turretType))
                self.menuOpen = True
                self.menuOpenAction = False

        if self.menuCloseAction and self.menuOpen:
            self.buttonTurrets = []
            self.menuOpen = False
            self.menuCloseAction = False

        if self.buttonTurrets != [] and self.menuOpen == True:

            for buttonTurret in self.buttonTurrets:
                buttonTurret.draw(screen)

        if self.animation == []:
            screen.blit(self.image, self.rect)
        else:
            self.image = self.animation[self.actualFrame]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            screen.blit(self.image, self.rect)

    def update(self, event):
        pos = pg.mouse.get_pos()
        if self.buttonTurrets != [] and self.menuOpen:
            for turret in self.buttonTurrets:
                resultUpdate, self.turret = turret.update(event, self)
                if resultUpdate:
                    self.grupoBandeira.add(self, self.turret)
                    return resultUpdate, self.turret

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            pos = pg.mouse.get_pos()
            if self.rect.collidepoint(event.pos):
                self.menuOpenAction = True
            else:
                self.menuCloseAction = True
        return False, None

    def calculateButtonTurret(self):

        if self.y < 18:
            self.buttonTurretPx = [
                (self.x - 8*c.MULTI, self.y+41*(c.MULTI)),
                (self.x + 8*c.MULTI, self.y+25*(c.MULTI)),
                (self.x + 8*c.MULTI, self.y+41*(c.MULTI))
            ]
        else:
            self.buttonTurretPx = [
                (self.x - 8*c.MULTI, self.y-25*(c.MULTI)),
                (self.x + 8*c.MULTI, self.y-41*(c.MULTI)),
                (self.x + 8*c.MULTI, self.y-25*(c.MULTI))
            ]
