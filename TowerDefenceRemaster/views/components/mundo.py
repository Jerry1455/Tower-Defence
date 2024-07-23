import pygame as pg
import constantes as c
from views.components.botaoBandeira import BotaoBandeira
from views.components.grupos import Grupos as gp

class Mundo ():
    def __init__(self, imgMapa, surface):
        self.image = imgMapa
        self.enemyWpPx = []
        surface.blit(self.image, (0, 0))
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
        self.enemyWpPx = self.drawWaypoint()
    def drawWaypoint(self):
        enemyWpPx = []
        for x, y in self.enemyWp:
            if x > 0 and y > 0:
                enemyWpPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                 (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))
            elif x > 0:
                enemyWpPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                 (y*c.TAMANHO_QUADRADO)))
            elif y > 0:
                enemyWpPx.append(((x*c.TAMANHO_QUADRADO),
                                 (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))
        return enemyWpPx

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
        self.enemyWpPx = self.drawWaypoint()
    
    def criarBandeira (self):
        for bandeira in self.bandeirasPx:
            bandeira = BotaoBandeira (BotaoBandeira.imgBandeira, self.bandeirasPx[0], self.bandeirasPx[1] )
            gp.grupoBandeira.add(bandeira)
        return gp.grupoBandeira
    
    def coordbandeiras(self):
        bandeiras = [
            (2, 3),
            (10, 8),
            (4, 6),
            (11, 6),
            (8, 6),
            (7, 4),
            (11, 3),
        ]
        bandeirasPx = []
        for x, y in bandeiras:
            if x > 0 and y > 0:
                bandeirasPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                 (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))
            elif x > 0:
                bandeirasPx.append(((x*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2,
                                 (y*c.TAMANHO_QUADRADO)))
            elif y > 0:
                bandeirasPx.append(((x*c.TAMANHO_QUADRADO),
                                 (y*c.TAMANHO_QUADRADO)-c.TAMANHO_QUADRADO/2))
        return bandeirasPx
    
