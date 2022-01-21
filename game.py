from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.collision import *
from torre import *
from tiro import *
global money
"""
tirei o scorpion.py e coloquei no game.py na função abaixo
"""
def cliquenatorre(teste,tempo,mouse,clique,money):
    if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
        clique = True

    return clique

def scorpionanimation(janela,lista_scorpion,time):
    if time >= 5:
        for i in range(1):
            if len(lista_scorpion) >= 5:
                break
            scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
            scorpion.x = 10
            scorpion.y = 373
            scorpion.set_sequence_time(0, 19, 50, True)
            lista_scorpion.append(scorpion)
        time = 0
    else:
        time += janela.delta_time()
    return lista_scorpion, time

def scorpionmovimento(lista_scorpion,janela):
    for scorpion in lista_scorpion:

        velMonstro = 80
        if scorpion.x >= 0:
            if scorpion.x < janela.height:
                scorpion.x += velMonstro * janela.delta_time()
        if scorpion.x > 690:
            scorpion.y += velMonstro * janela.delta_time()



def game(janela):
    fundo = GameImage("imagens/FUNDO AREIA COMPLETO.jpg")
    janela.set_title("Defense of the Light")

    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
    lista = []
    tempo = 0
    """
    dinheiro:
    """
    money = 200

    teste = GameImage("imagens/ico_8.png")
    teste.x, teste.y = [50,10]
    coracao = GameImage("../Defense Of The Light 2/imagens/heart.png")
    coracao.x,coracao.y = [500,10]
    clique = False
    torre = Sprite("imagens/torrefeita.png",1)
    tiroarco = Sprite("imagens/arqueiro tower/37.png", 1)
    listatiro = []
    vida_scorpion = 100
    lista_scorpion = []
    listatorrereal = []


    time = 0
    time2 = 0

    while True:
        tempo += janela.delta_time()
        lista_scorpion, time = scorpionanimation(janela, lista_scorpion,time)
        # mecanicas:
        if (teclado.key_pressed("ESC")):
            break
        """
        vendo se ta sendo click e se te money
        """
        if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
            clique = True
            money -= 100
        ""
        clique = movimentotorre(lista, mouse, tempo, clique, teste,torre,listatorrereal)
        scorpionmovimento(lista_scorpion,janela)
        listatiro, time2, money = tirotorre(torre, lista_scorpion, listatorrereal, listatiro, vida_scorpion, janela, time2 ,tiroarco, money)

        # desenhos:
        fundo.draw()
        for i in listatorrereal:
            i.draw()
        for i in lista:
            i.draw()
        for j in listatiro:
            j.draw()
        for i in lista_scorpion:
            i.draw()
            i.update()
        janela.draw_text(str(money), janela.width/2, 10, 27, (255, 0, 0), "Boulder", False, False)
        teste.draw()

        janela.update()