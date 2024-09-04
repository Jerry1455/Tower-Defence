import pygame as pg
from midia.access import Midia
import constantes as c
from views.components.botaoTorre import BotaoTorre
from views.components.botaoCancel import BotaoCancel


class Menu:
    def __init__(self, screen):
        self.midia = Midia()
        self.screen = screen
        self.state = {'botaoCancel': False,
                      'botaoTorre': True, 'botaoTorre2': True}
        self.components = {'botaoTorre': BotaoTorre((c.TELA_LARGURA + c.OFF_SET, c.OFF_SET), self.midia.img_iconeDMG_btn),
                           'botaoTorre2': BotaoTorre((c.TELA_LARGURA + c.TAMANHO_ICONES+c.OFF_SET, c.OFF_SET), self.midia.img_iconeMGC_btn),
                           'botaoCancel': BotaoCancel((c.TELA_LARGURA + 120, 180), self.midia.img_cancel_btn)}
        self.submenu = {'botaoTorre': [], 'botaoCancel': None}

    def draw(self, world_state):
        for component_name, component in self.components.items():
            if self.state[component_name] is True:
                self.state = component.draw(
                    self.screen, self.state, world_state,)
