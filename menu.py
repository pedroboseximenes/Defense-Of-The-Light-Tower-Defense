from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from game import *
from trailer import *
def trailer(janela,teclado):
    if (teclado.key_pressed("ESC")):
        menu()
    video = moviepy.editor.VideoFileClip("imagens/test2.mp4")
    video = video.volumex(1.8)
    video.preview()
    janela = Window(1080, 800)
    return janela

def menu():
    janela = Window(1080, 800)
    fundo = GameImage("imagens/game_background_1.jpg")
    janela.set_title("Defense of the Light")

    teclado = Window.get_keyboard()

    logo = GameImage("imagens/testelogo.png")

    jogar_button = Sprite("imagens/button_start.png", 1)
    historia_button = Sprite("imagens/button_play.png",1)
    close_button = Sprite("imagens/button_close.png",1)

    mouse = Window.get_mouse()
    tempo = 0

    #coords:
    jogar_button.x, jogar_button.y  = [janela.width/2 - jogar_button.width/2,  janela.height/2 - 50]
    historia_button.x, historia_button.y = [janela.width/2 - historia_button.width/2, janela.height - 200]
    close_button.x, close_button.y = [30,janela.height - 120]

    logo.x = janela.width/2 - logo.width/2
    logo.y = 7

    while True:
        #mecanicas:
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(jogar_button)):
                game(janela)
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(close_button)):
                break
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(historia_button)):
                janela = trailer(janela,teclado)
        #desenhos:
        fundo.draw()
        logo.draw()
        jogar_button.draw()
        historia_button.draw()
        close_button.draw()
        janela.update()