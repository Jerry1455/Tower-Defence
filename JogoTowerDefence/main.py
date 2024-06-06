import pygame as pg
from inimigos.inimigo import Inimigo
from torres.torre import Torre
from botao import Botao
from mundo import Mundo
import constantes as c
import paletaDeCores as pdc


# iniciar o pygame
pg.init()

pgim = pg.image.load
clock = pg.time.Clock()

# criar a tela do jogo
tela = pg.display.set_mode((c.TELA_LARGURA + c.PAINEL, c.TELA_ALTURA))
pg.display.set_caption("Tower Defence")

#############
# Variáveis #
#############
colocarTorre = False

###################
# carregar imagem #
###################

# imagens mapa
imgMapa = pgim('levels/mapaTeste.png').convert_alpha()

# imagens Inimigos
imgZombieNorm = pgim('arte/imagens/inimigos/ZombieNormal.png').convert_alpha()
imgZombieFort = pgim('arte/imagens/inimigos/ZombieForte.png').convert_alpha()
imgZombieArm = pgim('arte/imagens/inimigos/ZombieArm.png').convert_alpha()
imgZombieRato = pgim('arte/imagens/inimigos/ZombieRato.png').convert_alpha()

# imagenns Torres
imgTorre = pgim('arte/imagens/torres/torre1.png').convert_alpha()

# Imagens botões
imgCancelBtn = pgim ('arte/imagens/botao/cancelBtn.png').convert_alpha()
imgComprarBtn = pgim ('arte/imagens/botao/comprarBtn.png').convert_alpha()

def criarTorre(posMouse):
    mouseQuadX = posMouse[0] // c.TAMANHO_QUADRADO
    mouseQuadY = posMouse[1] // c.TAMANHO_QUADRADO
    torre = Torre(imgTorre, mouseQuadX, mouseQuadY)
    grupoTorre.add(torre)


# criar Mundo
mundo = Mundo(imgMapa)

# criar grupos
grupoInimigo = pg.sprite.Group()
grupoTorre = pg.sprite.Group()

# criar botões

botaoTorre = Botao (c.TELA_LARGURA + 30, 120, imgComprarBtn )
botaoCancel = Botao (c.TELA_LARGURA + 50, 180, imgCancelBtn)

inimigo = Inimigo(mundo.waypoint, imgZombieNorm)
grupoInimigo.add(inimigo)


# loop do jogo
rodar = True
while rodar:

    ################
    # ATUALIZANDO #
    ################

    # atualizar grupo
    grupoInimigo.update()

    ###############
    # DESENHANDO #
    ###############
    # tempo do tick
    clock.tick(c.FPS)

    tela.fill(pdc.bege)

    # desenhar o level
    mundo.draw(tela)

    # desenhar caminho do inimigo
    pg.draw.lines(tela, pdc.cinza, False, mundo.waypoint)

    # desenhar Grupos
    grupoInimigo.draw(tela)
    grupoTorre.draw(tela)

    # desenhar Botoes
    if botaoTorre.draw (tela):
        colocarTorre = True
        
    if colocarTorre == True:
        if botaoCancel.draw (tela):
         colocarTorre = False

    #########################
    # GERENCIANDO EVENTOS  #
    #########################

    # gerenciar eventos
    for event in pg.event.get():
        # fechar jogo
        if event.type == pg.QUIT:
            rodar = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            posMouse = pg.mouse.get_pos()
            # checar se o mouse está na área do jogo
            if posMouse[0] < c.TELA_LARGURA and posMouse[1] < c.TELA_ALTURA:
                criarTorre(posMouse)

    # atualizar a tela
    pg.display.flip()

pg.quit()