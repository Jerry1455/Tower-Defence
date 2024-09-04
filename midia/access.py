import pygame as pg
import constantes as c

class Midia:
    def __init__(self):
        pgim = pg.image.load

        self.img_mapa = pgim('midia/levels/level-0.png').convert_alpha()

        # imagens Inimigos
        self.img_zombie_norm = pgim('midia/imagens/inimigos/zombieNormal/spriteSheet.png').convert_alpha()
        self.img_zombie_fort = pgim('midia/imagens/inimigos/zombieForte.png').convert_alpha()
        self.img_zombie_arm = pgim('midia/imagens/inimigos/zombieArm.png').convert_alpha()
        self.img_zombie_rato = pgim('midia/imagens/inimigos/zombieRato.png').convert_alpha()

        # imagenns Torres
        self.img_torre = pgim('midia/imagens/torres/dmgTorreStand.png').convert_alpha()
        self.img_pistola = pgim("midia/imagens/torres/pistola/1/pistola.png").convert_alpha()
        
        
        # Imagens botões
        self.img_cancel_btn = pgim ('midia/imagens/botao/cancelBtn.png').convert_alpha()
        self.img_bandeira_btn = pgim ('midia/imagens/botao/bandeira/spriteSheet.png').convert_alpha()
        self.img_iconeDMG_btn = pgim ('midia/imagens/botao/iconeDmg.png').convert_alpha()
        self.img_iconeMGC_btn = pgim ('midia/imagens/botao/iconeMgc.png').convert_alpha()
        self.img_iconeAREA_btn = pgim ('midia/imagens/botao/iconeArea.png').convert_alpha()
        self.imgCoracao = pgim("midia/imagens/botao/coracao.png").convert_alpha()
        
        #definir o tamanho das imagens
        self.img_mapa = pg.transform.scale_by(self.img_mapa,c.MULTI)
        self.img_pistola = pg.transform.scale_by(self.img_pistola,c.MULTI)
        ##self.img_zombie_norm = pg.transform.scale_by( self.img_zombie_norm,(1+c.MULTI/13))
        self.img_zombie_fort = pg.transform.scale_by(self.img_zombie_fort,(1+c.MULTI/13))
        self.img_zombie_arm = pg.transform.scale_by( self.img_zombie_arm,(1+c.MULTI/13))
        self.img_zombie_rato = pg.transform.scale_by( self.img_zombie_rato,(1+c.MULTI/13))
        self.img_torre = pg.transform.scale_by(self.img_torre ,c.MULTI)
        self.img_cancel_btn = pg.transform.scale_by(self.img_cancel_btn,c.MULTI)
        self.img_iconeDMG_btn = pg.transform.scale_by(self.img_iconeDMG_btn,c.MULTI)
        self.img_iconeMGC_btn = pg.transform.scale_by(self.img_iconeMGC_btn ,c.MULTI)
        self.img_iconeAREA_btn = pg.transform.scale_by(self.img_iconeAREA_btn ,c.MULTI)
        self.imgCoracao = pg.transform.scale_by(self.imgCoracao ,c.MULTI)
