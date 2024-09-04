import pygame as pg

class Grupos (pg.sprite.Sprite):
    def __init__ (self, grupoInimigo, grupoTorre, grupoBadeira):
        grupoInimigo = pg.sprite.Group()
        grupoTorre = pg.sprite.Group()
        grupoBandeira = pg.sprite.Group()
    
    def grupoInimigo (self):
        grupoInimigo = pg.sprite.Group()