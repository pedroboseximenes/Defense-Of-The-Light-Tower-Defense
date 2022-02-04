from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from game import *
def fases(janela, mouse, teclado):
    fundo = GameImage("imagens/game_background_1.jpg")
    janela.set_title("Defense of the Light")
    mapa1 = GameImage("imagens/num_1.png")
    mapa2= GameImage("imagens/num_.png")
    mapa3 = GameImage("imagens/num_3.png")
    mapa1_play = GameImage("imagens/button_play.png")
    mapa2_play = GameImage("imagens/button_play.png")
    mapa3_play = GameImage("imagens/button_play.png")

    mapa1.x,mapa1.y = [janela.width/2 - mapa1.width/2 - 300,  janela.height/2 - 50]
    mapa2.x,mapa2.y = [janela.width/2 - mapa2.width/2, janela.height/2 - 50]
    mapa3.x, mapa3.y = [janela.width/2 - mapa3.width/2 + 300, janela.height/2 - 50]

    mapa1_play.x, mapa1_play.y = [janela.width/2 - mapa1.width/2 - 360,  janela.height/2 +50]
    mapa2_play.x, mapa2_play.y = [janela.width/2 - mapa2.width/2-59, janela.height/2 + 50]
    mapa3_play.x, mapa3_play.y = [janela.width/2 - mapa3.width/2 + 250, janela.height/2 + 50]
    while True:
        if teclado.key_pressed("ESC"):
            break
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(mapa1_play)):
                fases = 1
                game(janela, fases)
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(mapa2_play)):
                fases = 2
                game(janela, fases)
        if(mouse.is_button_pressed(1)):
            if (mouse.is_over_object(mapa3_play)):
                fases = 3
                game(janela, fases)
        fundo.draw()
        mapa1.draw()
        mapa2.draw()
        mapa3.draw()
        mapa1_play.draw()
        mapa2_play.draw()
        mapa3_play.draw()
        janela.update()
def tutorial(janela,fundo,teclado):
    tutorialarco = Sprite("imagens/7.png",1)
    tutorialarco.x,tutorialarco.y = [10,10]
    texto = "TxO:"
    while True:
        if (teclado.key_pressed("ESC")):
            break
        fundo.draw()
        janela.draw_text(str(texto), janela.width/2, 360, 38, (1, 0, 0), "Boulder", False, False)
        tutorialarco.draw()
        janela.update()
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
    information_button = Sprite("imagens/information.png",1)
    fases_button = Sprite("imagens/button_quick.png",1)

    mouse = Window.get_mouse()
    tempo = 0

    #coords:
    information_button.x, information_button.y = [980,10]
    jogar_button.x, jogar_button.y  = [janela.width/2 - jogar_button.width/2 - 200,  janela.height/2 - 50]
    historia_button.x, historia_button.y = [janela.width/2 - historia_button.width/2, janela.height - 200]
    close_button.x, close_button.y = [30,janela.height - 120]
    fases_button.x,fases_button.y = [janela.width/2 - jogar_button.width/2 + 200,  janela.height/2 - 50]

    logo.x = janela.width/2 - logo.width/2
    logo.y = 7

    while True:
        #mecanicas:
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(fases_button)):
                fases(janela,mouse,teclado)
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(jogar_button)):
                fase = 1
                game(janela,fase)
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(close_button)):
                break
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(historia_button)):
                janela = trailer(janela,teclado)
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(information_button)):
                tutorial(janela,fundo, teclado)
        #desenhos:
        fundo.draw()
        logo.draw()
        jogar_button.draw()
        historia_button.draw()
        close_button.draw()
        #information_button.draw()
        fases_button.draw()
        janela.update()