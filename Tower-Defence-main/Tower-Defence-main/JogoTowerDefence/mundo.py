import pygame as pg


class Mundo ():
    def __init__(self, imagemMapa):
        self.image = imagemMapa

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
    waypoint = [
    (68 , 0),
    (71, 88),
    (485, 77),
    (515, 154),
    (68, 193),
    (72, 302),
    (563, 242),
    (538, 338),
]
