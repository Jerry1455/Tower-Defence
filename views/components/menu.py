import pygame as pg
from midia.access import Midia
import constantes as c


class Menu:
    def __init__(self, screen):
        self.midia = Midia()
        self.screen = screen

        self.submenu = {'botaoTorre': [], 'botaoCancel': None}

    def draw(self, world_state):
        pass