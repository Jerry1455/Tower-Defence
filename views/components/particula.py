import pygame as pg
import constantes as c
from importData import ImportData


class Particula ():
    def __init__(self, pos, type_article):
        self.animation = []
        self.pos = pos
        pgim = pg.image.load
        self.frame = 0
        self.vida = 10
        self.size = 1
        self.data = ImportData()
        self.image = self.data.partcileType(type_article)
        self.image = pgim(self.image).convert_alpha()
        self.setAnimation(self.image)
        self.rect = self.animation[0].get_rect()
        self.rect.center = self.pos
        self.done = False
        self.turn = 0
        self.repeat = 100

    def draw(self, screen):
        screen.blit(self.animation[self.frame], self.rect)
        self.frame += 1
        if self.frame >= self.frames:
            self.turn += 1
            self.frame = 0
            if self.turn >= self.repeat:
                self.done = True

    def setAnimation(self, image):
        if image.get_height() > c.TAMANHO_ICONES:
            self.frames = round(image.get_height() / c.TAMANHO_ICONES)
            for i in range(0, self.frames):
                print(0, i * c.TAMANHO_ICONES,
                      c.TAMANHO_ICONES, c.TAMANHO_ICONES)
                frame = pg.transform.scale_by(image.subsurface(
                    0, i * c.TAMANHO_ICONES, c.TAMANHO_ICONES, c.TAMANHO_ICONES), self.size)
                self.animation.append(frame)
            for i, frame in enumerate(self.animation):
                self.animation[i] = pg.transform.flip(frame, True, False)
            self.frames = len(self.animation)
        return image
