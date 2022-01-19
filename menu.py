from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from game import *

janela = Window(1080, 800)
fundo = GameImage("imagens/game_background_1.jpg")
janela.set_title("Defense of the Light")


jogar_button = Sprite("imagens/button_play.png", 1)

mouse = Window.get_mouse()
tempo = 0

#coords:
jogar_button.x = janela.width/2 - jogar_button.width/2
jogar_button.y = janela.height/2 - jogar_button.height/2

while True:
    #mecanicas:
    if (mouse.is_button_pressed(1)):
        if (mouse.is_over_object(jogar_button)):
            game(janela)
    #desenhos:
    fundo.draw()
    jogar_button.draw()
    janela.update()