import pygame as pg
import constantes as c
from views.components.botaoBandeira import BotaoBandeira
from midia.access import Midia
from importData import ImportData
from models.entities.inimigo import Inimigo
from models.entities.torre import Torre


class Mundo ():
    def __init__(self, imgMapa, screen):
        self.midia = Midia()
        self.image = imgMapa

        # Flags
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
        self.coldownAnimation = 0
        # Inimigo
        self.setDifficult()
        self.enemyWpPx = []
        self.enemys = []
        self.enemyCount = 0
        self.drawWaypoint()
        self.grupoInimigo = pg.sprite.Group()
        self.addEnemy()

    def setDifficult(self):
        pg.time.set_timer(c.ENEMYEVENT, 20000)

    def addEnemy(self):
        print(len(self.enemys))
        self.enemyCount += 1
        inimigo = Inimigo(self.enemyWpPx, self.midia.img_zombie_norm)
        self.enemys.append(inimigo)
        self.grupoInimigo.add(inimigo)

    def drawWaypoint(self):
        self.enemyWpPx = []
        for x, y in self.enemyWp:
            if x > 0 and y > 0:
                self.enemyWpPx.append(((x*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO,
                                       (y*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO))
            elif x > 0:
                self.enemyWpPx.append(((x*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO,
                                       (y*c.TAMANHO_QUADRADO*c.MULTI)))
            elif y > 0:
                self.enemyWpPx.append(((x*c.TAMANHO_QUADRADO*c.MULTI),
                                       (y*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO))

    def draw(self, screen):
        self.coldownAnimation += 1
        screen.blit(self.image, (0, 0))
        for flag in self.flags:
            if (self.coldownAnimation % flag.coldowAnimation) == 0:
                flag.animate()
            flag.draw(screen)
            
        self.flagsGroup.draw(screen)

        if self.coldownAnimation > 100:
            self.coldownAnimation = 0
        self.drawWaypoint()
        for enemy in self.enemys:
            if enemy.morto is not True:
                enemy.draw(screen)

    def drawCoordbandeiras(self):
        self.flagButtonsPx = []
        for x, y in self.flagButtonsPos:
            if x > 0 and y > 0:
                self.flagButtonsPx.append(((x*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO,
                                           (y*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO))
            elif x > 0:
                self.flagButtonsPx.append(((x*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO,
                                           (y*c.TAMANHO_QUADRADO*c.MULTI)))
            elif y > 0:
                self.flagButtonsPx.append(((x*c.TAMANHO_QUADRADO*c.MULTI),
                                           (y*c.TAMANHO_QUADRADO*c.MULTI)-c.TAMANHO_QUADRADO))
        self.flags = [BotaoBandeira((x, y), self.flagImage)
                      for x, y in self.flagButtonsPx]
        for flag in self.flags:
            self.flagsGroup.add(flag)

    def verifyCollideRangeTurret(self):
        for flagCount, flag in enumerate(self.flags):
            targeted = False
            if isinstance(flag, Torre):
                for enemyCount, enemy in enumerate(self.enemys):

                    if flag.range_collide.collidepoint(enemy.pos) and flag.target == None:
                        flag.target = enemy
                        targeted = True
                        print("achei")

                    if flag.range_collide.collidepoint(enemy.pos) and flag.target == enemy:
                        self.enemys[enemyCount] = flag.shotTarget()
                        flag.target = self.enemys[enemyCount]
                        targeted = True
                if targeted == False:
                    flag.target = None

    def enemyUpdate(self):
        self.grupoInimigo.update()
        self.verifyCollideRangeTurret()
        for i, enemy in enumerate(self.enemys):

            if enemy.vida == 1:
                self.enemys.remove(enemy)
                self.grupoInimigo.remove(enemy)

    def update(self, event):
        for flagCount, flag in enumerate(self.flags):
            if self.flags[flagCount] == None:
                self.flags[flagCount] = BotaoBandeira(
                    self.flagButtonsPx[flagCount], self.flagImage)
                self.flagsGroup.add(self.flags[flagCount])
            updateToTurret = flag.update(event)
            if updateToTurret:
                self.flagsGroup.remove(self.flags[flagCount])

                self.flags[flagCount] = flag.turret
                updateToTurret = False
        if event.type == c.ENEMYEVENT:
            self.addEnemy()
