import pygame as pg

class Midia:
    def __init__(self):
        pgim = pg.image.load

        self.img_mapa = pgim('midia/levels/level-0.png').convert_alpha()

        # imagens Inimigos
        self.img_zombie_norm = pgim('midia/imagens/inimigos/zombieNormal.png').convert_alpha()
        self.img_zombie_fort = pgim('midia/imagens/inimigos/zombieForte.png').convert_alpha()
        self.img_zombie_arm = pgim('midia/imagens/inimigos/zombieArm.png').convert_alpha()
        self.img_zombie_rato = pgim('midia/imagens/inimigos/zombieRato.png').convert_alpha()

        # imagenns Torres
        self.img_torre = pgim('midia/imagens/torres/dmgTorreStand.png').convert_alpha()
        

        # Imagens botões
        self.img_cancel_btn = pgim ('midia/imagens/botao/cancelBtn.png').convert_alpha()
        self.img_bandeira_btn = pgim ('midia/imagens/botao/bandeira.png').convert_alpha()
        self.img_iconeDMG_btn = pgim ('midia/imagens/botao/iconeDmg.png').convert_alpha()
        self.img_iconeMGC_btn = pgim ('midia/imagens/botao/iconeMgc.png').convert_alpha()
        self.img_iconeAREA_btn = pgim ('midia/imagens/botao/iconeArea.png').convert_alpha()