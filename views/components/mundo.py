import pygame as pg
import constantes as c
from constantes import paletaDeCores as pdc
from views.components.botaoBandeira import BotaoBandeira
from midia.access import Midia
from importData import ImportData
from models.entities.inimigo import Inimigo
from models.entities.torre import Torre
from pygame.math import Vector2
from .particula import Particula
import random

class Mundo ():
    def __init__(self, imgMapa, screen):
        self.endgame = False
        self.midia = Midia()
        self.image = imgMapa
        self.font = pg.font.SysFont("britannic", 28)
        self.imgCoracao = self.midia.imgCoracao
        self.coinsObj = []

        # life
        self.life = 1
        self.labelLife = self.font.render(str(self.life), 10, (pdc.cinzaE))

        # coins
        self.coins = 30
        self.labelCoin = self.font.render(str(self.coins), 10, (pdc.cinzaE))

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
        self.levelDifficult = self.data.level()
        self.flagButtonsPos = self.data.map()['bandeiras']
        self.drawCoordbandeiras()
        self.coldownAnimation = 0
        # Inimigo
        self.setRates()
        self.enemyWpPx = []
        self.enemys = []
        self.enemyCount = 0
        self.drawWaypoint()
        self.grupoInimigo = pg.sprite.Group()
        self.addEnemy()

    def setRates(self):
        pg.time.set_timer(c.ENEMYEVENT, self.levelDifficult['enemySpawnTime'])

    def addEnemy(self):
        self.enemyCount += 1
        enemySort = []
        for enemy in self.levelDifficult["enemys"]:
            for i in range(0,enemy['spawnRate']):
                enemySort.append(enemy)
            
        chosenEnemy = enemySort[random.randint(0,len(enemySort)-1)]
        
        inimigo = Inimigo(self.enemyWpPx, pg.image.load(chosenEnemy['spriteSheet']).convert_alpha())
        inimigo.vida = chosenEnemy['vida']
        inimigo.value = chosenEnemy["value"]
        inimigo.speed = chosenEnemy['speed']
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

    def drawWorld(self, screen):
        screen.blit(self.image, (0, 0))
        self.labelLife = self.font.render(str(self.life), 10, (pdc.cinzaE))
        self.labelCoin = self.font.render(str(self.coins), 10, (pdc.cinzaE))

        for enemy in self.enemys:
            if enemy.pos == Vector2(self.enemyWpPx[-1]):
                self.life -= 1
                self.enemys.remove(enemy)

        screen.blit(self.imgCoracao, (c.TELA_LARGURA/2, 0))
        screen.blit(self.labelLife, (c.TELA_ALTURA /
                    2 + 8 + 19*(c.TAMANHO_ICONES), 0))
        screen.blit(self.labelCoin, (c.TELA_ALTURA /
                    2 + 8 + 12*(c.TAMANHO_ICONES), 0))
        
    def draw(self, screen):
        self.coldownAnimation += 1
        self.drawWorld(screen)
        if self.endgame == True:
            s = pg.Surface((1000,750))  # the size of your rect
            s.set_alpha(128)                # alpha level
            s.fill((255,45,25))           # this fills the entire surface
            screen.blit(s, (0,0))
            
            s = pg.Surface((c.TELA_ALTURA/2, c.TELA_LARGURA/12))  # the size of your rect
            s.fill((255,255,255))           # this fills the entire surface
            screen.blit(s, ((c.TELA_LARGURA/12)*4.25,(c.TELA_ALTURA/4)*1.65))
        else:
            for flag in self.flags:
                if (self.coldownAnimation % flag.coldowAnimation) == 0:
                    flag.animate()
                flag.draw(screen)

            self.flagsGroup.draw(screen)

            if self.coldownAnimation > 100:
                self.coldownAnimation = 0
            self.drawWaypoint()
            for enemy in self.enemys:
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
                    if isinstance(enemy, Inimigo):
                        if flag.range_collide.collidepoint(enemy.pos) and flag.target == None:
                            flag.target = enemy
                            targeted = True

                        if flag.range_collide.collidepoint(enemy.pos) and flag.target == enemy:
                            self.enemys[enemyCount] = flag.shotTarget()
                            flag.target = self.enemys[enemyCount]
                            targeted = True
                        if targeted is False:
                            flag.target = None

    def enemyUpdate(self):
        self.grupoInimigo.update()
        self.verifyCollideRangeTurret()
        for i, enemy in enumerate(self.enemys):

            if isinstance(enemy, Particula):
                if enemy.done is True:
                    self.enemys.remove(enemy)
            else:
                if enemy.vida == 1:
                    self.coins += enemy.value
                    self.grupoInimigo.remove(enemy)
                    self.enemys[i] = Particula(enemy.pos, 'coin')

    def update(self, event):
        for flagCount, flag in enumerate(self.flags):
            if self.flags[flagCount] == None:
                self.flags[flagCount] = BotaoBandeira(
                    self.flagButtonsPx[flagCount], self.flagImage)
                self.flagsGroup.add(self.flags[flagCount])
            if isinstance(flag, BotaoBandeira):
                updateToTurret, turret = flag.update(event)
            else:
                updateToTurret = flag.update(event) 
            if updateToTurret and not (self.coins - turret.price < 0):
                self.coins -= turret.price
                self.flagsGroup.remove(self.flags[flagCount])

                self.flags[flagCount] = flag.turret
                updateToTurret = False
        if event.type == c.ENEMYEVENT:
            self.addEnemy()

        if self.life < 0:
            self.endgame = True