import pygame as pg
import constantes as c
from views.components.botaoBandeira import BotaoBandeira
from midia.access import Midia
from importData import ImportData


class Mundo ():
    def __init__(self, imgMapa, screen):
        self.midia = Midia()
        self.image = imgMapa
        self.enemyWpPx = []
        self.flags = []
        self.flagsGroup = pg.sprite.Group()
        self.flagImage = self.midia.img_bandeira_btn
        self.data = ImportData()

        screen.blit(self.image, (0, 0))
        self.enemyWp = [
            (2, 0),
            (2, 2),
            (12, 2),
            (12, 5),
            (3, 5),
            (3, 7),
            (11, 7),
            (11, 9),
        ]
        self.drawWaypoint()
        self.flagButtonsPos = self.data.map()['bandeiras']
        self.drawCoordbandeiras()

    def drawWaypoint(self):
        self.enemyWpPx = []
        for x, y in self.enemyWp:
            if x > 0 and y > 0:
                self.enemyWpPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                       (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))
            elif x > 0:
                self.enemyWpPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                       (y*c.TAMANHO_QUADRADO)))
            elif y > 0:
                self.enemyWpPx.append(((x*c.TAMANHO_QUADRADO),
                                       (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        self.flagsGroup.draw(screen)
        for flag in self.flags:
            flag.draw(screen)
        self.drawWaypoint()

    def drawCoordbandeiras(self):
        self.flagButtonsPx = []
        for x, y in self.flagButtonsPos:
            if x > 0 and y > 0:
                self.flagButtonsPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                           (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))
            elif x > 0:
                self.flagButtonsPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                           (y*c.TAMANHO_QUADRADO)))
            elif y > 0:
                self.flagButtonsPx.append(((x*c.TAMANHO_QUADRADO),
                                           (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))
        self.flags = [BotaoBandeira((x, y), self.flagImage)
                      for x, y in self.flagButtonsPx]
        for flag in self.flags:
            self.flagsGroup.add(flag)

    def update(self, event):
        for flagCount in range(0, len(self.flags)):
            if self.flags[flagCount] == None:
                self.flags[flagCount] = BotaoBandeira(
                    self.flagButtonsPx[flagCount], self.flagImage)
                self.flagsGroup.add(self.flags[flagCount])
            updateToTurret = self.flags[flagCount].update(event)
            if updateToTurret:
                self.flagsGroup.remove(self.flags[flagCount])

                self.flags[flagCount] = self.flags[flagCount].turret
                self.flagsGroup.add(self.flags[flagCount])
                updateToTurret = False
