import pygame as pg
from pygame.math import Vector2
import math

class Inimigo (pg.sprite.Sprite):
    def __init__(self, waypoint, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoint = waypoint
        self.pos = Vector2(self.waypoint[0])
        self.alvo_waypoint = 1
        self.speed = 2
        self.angulo = 0
        self.imagemOriginal = image
        self.image = pg.transform.rotate(self.imagemOriginal, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.move()
        self.rotacionar()

    def move(self):
        # define o próximo alvo
        if self.alvo_waypoint < len(self.waypoint):
            self.alvo = Vector2(self.waypoint[self.alvo_waypoint])
            self.movimento = self.alvo - self.pos
            
        # Inimigo chegou no final do curso
        else:
            self.kill()
        
        # calulcar a distancia do alvo
        dist = self.movimento.length()
        if dist >= self.speed:
            self.pos += self.movimento.normalize() * self.speed
        else:
            if dist != 0 :
                self.pos += self.movimento.normalize() * dist
            self.alvo_waypoint += 1
        
    def rotacionar (self):
        
        # calcular a distancia do proximo waypoint
        dist = self.alvo - self.pos
        
        # usa a distancia para calcular o angulo
        self.angulo = math.degrees(math.atan2(-dist[1], dist[0]))
        
        # rotacionar a imagem e atualizar o retangulo
        self.image = pg.transform.rotate(self.imagemOriginal, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
            

