import pygame as pg
from models.entities.torre import Torre
from views.components.baseComponents.botao import Botao
from views.components.mundo import Mundo
import constantes as c
import constantes.paletaDeCores as pdc
from views.components.menu import Menu
from views.components.botaoBandeira import BotaoBandeira

# iniciar o pygame
pg.init()

pgim = pg.image.load
clock = pg.time.Clock()

# criar a tela do jogo
tela = pg.display.set_mode((c.TELA_LARGURA + c.PAINEL, c.TELA_ALTURA))
pg.display.set_caption("Tower Defence")


###################
# carregar imagem #
###################
# TODO: Sprite Loader
# imagens mapa
imgMapa = pgim('midia/levels/level-0.png').convert_alpha()

imgCancelBtn = pgim('midia/imagens/botao/cancelBtn.png').convert_alpha()
img_bandeira_btn = pgim('midia/imagens/botao/bandeira.png').convert_alpha()

# criar Mundo
mundo = Mundo(imgMapa, tela)
# Criar menu
menu = Menu(tela)

# criar botões
botaoCancel = Botao((c.TELA_LARGURA + 50, 180), imgCancelBtn)
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
    mundo.grupoInimigo.update()
    # gerenciar eventos
    for event in pg.event.get():

        mundo.update(event)

        if event.type == pg.QUIT:
            rodar = False

    # atualizar a tela
    pg.display.flip()
pg.quit()
