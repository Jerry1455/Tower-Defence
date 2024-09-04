import pygame as pg
from models.entities.inimigo import Inimigo
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

#############
# Variáveis #
#############
colocarTorre = False

###################
# carregar imagem #
###################
# TODO: Sprite Loader
# imagens mapa
imgMapa = pgim('midia/levels/level-0.png').convert_alpha()

# imagens Inimigos
imgZombieNorm = pgim('midia/imagens/inimigos/zombieNormal.png').convert_alpha()
imgZombieFort = pgim('midia/imagens/inimigos/zombieForte.png').convert_alpha()
imgZombieArm = pgim('midia/imagens/inimigos/zombieArm.png').convert_alpha()
imgZombieRato = pgim('midia/imagens/inimigos/zombieRato.png').convert_alpha()

# imagenns Torres
imgTorre = pgim('midia/imagens/torres/torre1.png').convert_alpha()

# Imagens botões
imgCancelBtn =     pgim('midia/imagens/botao/cancelBtn.png').convert_alpha()
img_bandeira_btn = pgim('midia/imagens/botao/bandeira.png').convert_alpha()

'''
def criarTorre(posMouse):
    mouseQuadX = posMouse[0] // c.TAMANHO_QUADRADO
    mouseQuadY = posMouse[1] // c.TAMANHO_QUADRADO
    torre = Torre(imgTorre, mouseQuadX, mouseQuadY)
    grupoTorre.add(torre)
'''

def selecionar(posMouse):
    mouseQdrx = posMouse[0] // c.TAMANHO_QUADRADO
    mouseQdry = posMouse[1] // c.TAMANHO_QUADRADO
    for bandeira in grupoBandeira:
        if (mouseQdrx, mouseQdry) == (bandeira.quadradoX, bandeira.quadradoY):
            return bandeira

def limparSelecao():
    for bandeira in grupoBandeira:
        bandeira.clicado = False

# criar Mundo
mundo = Mundo(imgMapa, tela)
# Criar menu
menu = Menu(tela)

# criar botões
botaoCancel = Botao((c.TELA_LARGURA + 50, 180), imgCancelBtn)

inimigo = Inimigo(mundo.enemyWpPx, imgZombieNorm)
grupoInimigo = pg.sprite.Group()
grupoTorre = pg.sprite.Group()
grupoTeste = pg.sprite.Group()

grupoInimigo.add(inimigo)

world_state = {

}
# loop do jogo
rodar = True
while rodar:
    
    ################
    # ATUALIZANDO #
    ################

    # atualizar level
    grupoInimigo.update()
    clock.tick(c.FPS)
    tela.fill(pdc.bege)

    # desenhar o level
    mundo.draw(tela)
    grupoInimigo.draw(tela)
    grupoTorre.draw(tela)
    
    # desenhar caminho do inimigo
    pg.draw.lines(tela, pdc.cinza, False, mundo.enemyWpPx)
    
    menu.draw(world_state)

    #########################
    # GERENCIANDO EVENTOS  #
    #########################

    # gerenciar eventos
    for event in pg.event.get():
        if event.type !=  pg.MOUSEMOTION: 
            print(event)
        # fechar jogo
        mundo.update(event)
        if event.type == pg.QUIT:
            rodar = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            posMouse = pg.mouse.get_pos()
            # checar se o mouse está na área do jogo
            '''          
  if posMouse[0] < c.TELA_LARGURA and posMouse[1] < c.TELA_ALTURA:
                mundo.criarTorre(posMouse)
                c.bandeiraClicado = None
                limparSelecao()
                if colocarTorre is True:
                    criarTorre(posMouse)
                else:
                    bandeiraClicado = (posMouse)
    '''
    # atualizar a tela
    pg.display.flip()
pg.quit()