import pygame as pg
from pygame.math import Vector2
import math
import constantes as c


class Inimigo (pg.sprite.Sprite):
    def __init__(self, enemyWpPx, image):
        pg.sprite.Sprite.__init__(self)
        self._vida = 5
        self.vida = 5
        self.enemyWpPx = enemyWpPx
        self.pos = Vector2(self.enemyWpPx[0])
        self.alvo_enemyWpPx = 0
        self.morto = False
        self.speed = 2
        self.angulo = 0
        self.imagemOriginal = image
        self.image = pg.transform.flip(self.imagemOriginal, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.fliped = True

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self,vida):
        if vida < 1:
            self.morto = True
        else:
            self._vida = vida

    def update(self):
        self.move()
        self.rotacionar()

    def move(self):
        # define o próximo alvo
        if self.alvo_enemyWpPx < len(self.enemyWpPx):
            self.alvo = Vector2(self.enemyWpPx[self.alvo_enemyWpPx])
            self.movimento = self.alvo - self.pos

        # Inimigo chegou no final do curso
        else:
            self.kill()

        # calulcar a distancia do alvo
        dist = self.movimento.length()
        if dist >= self.speed:
            self.pos += self.movimento.normalize() * self.speed
        else:
            if dist != 0:
                self.pos += self.movimento.normalize() * dist
            self.alvo_enemyWpPx += 1

    def rotacionar(self):

        # calcular a distancia do proximo waypoint
        dist = self.alvo - self.pos

        # usa a distancia para calcular o angulo
        self.angulo = math.degrees(math.atan2(-dist[1], dist[0]))

        # rotacionar a imagem e atualizar o retangulo
        if math.cos(math.radians(self.angulo)) == -1 and self.fliped is False:
            self.image = pg.transform.flip(self.image, True, False)
            self.fliped = True

        if math.cos(math.radians(self.angulo)) == 1 and self.fliped is True:
            self.image = pg.transform.flip(self.image, True, False)
            self.fliped = False

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def draw(self, screen):
        
        screen.blit(self.image, self.rect)