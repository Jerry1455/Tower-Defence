import pygame as pg

class Botao ():
    def __init__(self, x y, imagem):
        self.imagem = imagem
        self.rect = self.image.get_rect ()
        self.rect.topleft = (x,y)
        
        def draw (self, surface):
            # pegar a posição do mouse
            pos = pg.mouse.get_pos()
            
            # checar se o mouse clickou e outras paradas
            if self.rect.collidepoit (pos):
                if.pg.mouse.get_pressed()[0] == 1 