import pygame as pg

class Botao ():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect ()
        self.rect.topleft = (x, y)
        self.clicado = False
        
    def draw (self, surface):
        acao = False
        # pegar a posição do mouse
        pos = pg.mouse.get_pos()
            
        # checar se o mouse clickou e outras paradas
        if self.rect.collidepoint (pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicado == False:
                acao = True
                self.clicado = True
        if pg.mouse.get_pressed ()[0] == 0 :
            self.clicado = False


        surface.blit(self.image, self.rect)

        return acao