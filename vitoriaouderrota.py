import moviepy.editor
from PPlay.window import *
from PPlay.gameimage import *
from game import *



def perdeu(janela, mouse):
    fundo = GameImage("imagens/game_background_1.jpg")
    janela.set_title("Defense of the Light")
    perder = GameImage("imagens/header_failed.png")
    perder.x, perder.y = [janela.width / 2 - perder.width / 2, janela.height / 2 - perder.height / 2]
    restart = GameImage("imagens/button_restart.png")
    restart.x, restart.y = [10, 600]

    mapa1_play = GameImage("imagens/button_play.png")
    mapa1_play.x, mapa1_play.y = [700, 600]
    while True:
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(restart)):
                 break
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(mapa1_play)):
                break
        fundo.draw()
        perder.draw()
        restart.draw()
        mapa1_play.draw()
        janela.update()


def ganhar(janela,mouse):
    fundo = GameImage("imagens/game_background_1.jpg")
    janela.set_title("Defense of the Light")
    ganhou = GameImage("imagens/header_win.png")
    ganhou.x, ganhou.y = [janela.width / 2 - ganhou.width / 2, janela.height / 2 - ganhou.height / 2]
    restart = GameImage("imagens/button_restart.png")
    restart.x, restart.y = [10, 600]
    while True:
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(restart)):
                break
        fundo.draw()
        ganhou.draw()
        restart.draw()
        janela.update()