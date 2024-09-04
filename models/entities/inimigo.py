import pygame as pg
from pygame.math import Vector2
import math
import constantes as c


class Inimigo (pg.sprite.Sprite):
    def __init__(self, enemyWpPx, image):
        pg.sprite.Sprite.__init__(self)
        self._vida = 5
        self.vida = 5
        self.size = 1.25
        self.value = 100
        self.animation = []
        self.enemyWpPx = enemyWpPx
        self.pos = Vector2(self.enemyWpPx[0])
        self.alvo_enemyWpPx = 0
        self.morto = False
        self.speed = 2
        self.angulo = 0
        self.actualFrame = 0
        self.setAnimation(image)
        self.image = self.animation[self.actualFrame]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.fliped = True
        self.updateFrame = 0

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
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

    def setAnimation(self, image):
        if image.get_height() > c.TAMANHO_QUADRADO:
            self.frames = round(image.get_height() / c.TAMANHO_QUADRADO)
            for i in range(0, self.frames):
                print(0, i * c.TAMANHO_QUADRADO,
                      c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO)
                frame = pg.transform.scale_by(image.subsurface(
                    0, i * c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO, c.TAMANHO_QUADRADO), self.size)
                self.animation.append(frame)
            for i, frame in enumerate(self.animation):
                self.animation[i] = pg.transform.flip(frame, True, False)
            self.frames = len(self.animation)
        return image

    def rotacionar(self):
        if self.actualFrame >= self.frames:
            self.actualFrame = 0
        self.image = self.animation[self.actualFrame]
        # calcular a distancia do proximo waypoint
        dist = self.alvo - self.pos

        # usa a distancia para calcular o angulo
        self.angulo = math.degrees(math.atan2(-dist[1], dist[0]))

        # rotacionar a imagem e atualizar o retangulo
        if math.cos(math.radians(self.angulo)) == -1 and self.fliped is False:
            for i, frame in enumerate(self.animation):
                self.animation[i] = pg.transform.flip(frame, True, False)
            self.fliped = True

        if math.cos(math.radians(self.angulo)) == 1 and self.fliped is True:
            for i, frame in enumerate(self.animation):
                self.animation[i] = pg.transform.flip(frame, True, False)
            self.fliped = False

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.updateFrame += 1
        if self.updateFrame >= 5:
            self.actualFrame += 1
            self.updateFrame = 0

    def draw(self, screen):

        screen.blit(self.image, self.rect)
