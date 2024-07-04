import pygame as pg
import constantes


class EventController:
    def __init__(self):
        self.map_vector = [[x, y] for x in range(0, constantes.TELA_ALTURA, constantes.TAMANHO_QUADRADO)
                           for y in range(0, constantes.TELA_LARGURA, constantes.TAMANHO_QUADRADO)]

        self.map_grid = []
        for y in range(0, constantes.TELA_ALTURA, constantes.TAMANHO_QUADRADO):
            line = []
            for x in range(0, constantes.TELA_LARGURA, constantes.TAMANHO_QUADRADO):
                line.append([x, y])
            self.map_grid.append(line)

        self.map_path =[
                (68, 0),
                (71, 88),
                (485, 77),
                (515, 154),
                (68, 193),
                (72, 302),
                (563, 242),
                (538, 338),
        ]

    def stateUpdate(self):
        pass

    def update(self, eventQueue):
        for event in eventQueue:
            if event in self.registredEvents:
        self.registredEvents[event]()

    def openTowerMenu(self, event):
    # Verificar quadrado clicado
        # Abrir menu no lugar selecionado
