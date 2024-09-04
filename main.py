import pygame as pg
from models.entities.torre import Torre
from views.components.baseComponents.botao import Botao
from views.components.mundo import Mundo
import constantes as c
import constantes.paletaDeCores as pdc
from views.components.menu import Menu
from views.components.botaoBandeira import BotaoBandeira
from midia.access import Midia

# iniciar o pygame
pg.init()

pgim = pg.image.load
clock = pg.time.Clock()

# criar a tela do jogo
tela = pg.display.set_mode((c.TELA_LARGURA, c.TELA_ALTURA))
pg.display.set_caption("Tower Defence")


###################
# carregar imagem #
###################
# TODO: Sprite Loader
midia = Midia()
# criar Mundo
mundo = Mundo(midia.img_mapa, tela)
# Criar menu
menu = Menu(tela)

# criar botões

world_state = {}
# loop do jogo
rodar = True
while rodar:

    ################
    # ATUALIZANDO #
    ################

    # atualizar level
    clock.tick(c.FPS)

    tela.fill(pdc.bege)

    # desenhar o level
    mundo.draw(tela)

    # desenhar caminho do inimigo

    menu.draw(world_state)
    #########################
    # GERENCIANDONoneTOS  #
    #########################
    mundo.enemyUpdate()
    # gerenciar eventos
    for event in pg.event.get():

        mundo.update(event)

        if event.type == pg.QUIT:
            rodar = False

    # atualizar a tela
    pg.display.flip()
pg.quit()
