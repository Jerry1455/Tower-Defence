from views.components.baseComponents.botao import Botao
import pygame as pg
import constantes as c


class BotaoTorre(Botao):
    def __init__(self, px, image):
        super().__init__(px, image)
        self.pos = pg.mouse.get_pos()
        
    def action(self, state, world_state):
        state['botaoCancel'] = True
        return state

    def draw(self, screen, state, world_state):
        # pegar a posição do mouse
        pos = pg.mouse.get_pos()

        # checar se o mouse clickou e outras paradas
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicado == False:
                state = self.action(state, world_state)
        if pg.mouse.get_pressed()[0] == 0:
            self.clicado = False

        screen.blit(self.image, self.rect)
        return state
    
        
