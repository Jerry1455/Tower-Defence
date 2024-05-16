import pygame as pg
from inimigo import Inimigo
from torre import Torre
from mundo import Mundo
import constantes as c
import paletaDeCores as pdc


# iniciar o pygame
pg.init()

pgim = pg.image.load
clock = pg.time.Clock()

# criar a tela do jogo
tela = pg.display.set_mode((c.TELA_LARGURA, c.TELA_ALTURA))
pg.display.set_caption("Tower Defence")


# carregar imagem
imagemMapa = pgim('levels/mapaTeste.png').convert_alpha()
imagemInimigo = pgim('arte/imagens/inimigos/inimigo1.png').convert_alpha()
imagemTorre = pgim ('arte/imagens/torres/torre1.png').convert_alpha()

def criarTorre(posMouse):
    mouseQuadX = posMouse [0] // c.TAMANHO_QUADRADO
    mouseQuadY = posMouse [1] // c.TAMANHO_QUADRADO
    torre = Torre (imagemTorre, mouseQuadX, mouseQuadY)
    grupoTorre.add(torre)
# criar Mundo
mundo = Mundo(imagemMapa)

# criar grupos
grupoInimigo = pg.sprite.Group()
grupoTorre = pg.sprite.Group()

inimigo = Inimigo(mundo.waypoint, imagemInimigo)
grupoInimigo.add(inimigo)


# loop do jogo
rodar = True
while rodar:

    # tempo do tick
    clock.tick(c.FPS)

    tela.fill(pdc.bege)

    # desenhar o level
    mundo.draw(tela)

    # desenhar caminho do inimigo
    pg.draw.lines(tela, pdc.cinza, False, mundo.waypoint)

    # atualizar grupo
    grupoInimigo.update()

    # desenhar Grupos
    grupoInimigo.draw(tela)
    grupoTorre.draw(tela)

    # gerenciar eventos
    for event in pg.event.get():
        # fechar jogo
        if event.type == pg.QUIT:
            rodar = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            posMouse = pg.mouse.get_pos()
            # checar se o mouse está na área do jogo
            if posMouse [0] < c.TELA_LARGURA and posMouse [1] < c.TELA_ALTURA:
                criarTorre(posMouse)
                

    # atualizar a tela
    pg.display.flip()

pg.quit()
