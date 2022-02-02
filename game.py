from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.collision import *
from torre import *
from tiro import *
from scorpion import *
from besouro import *
from ogro import *
from random import randint
"""
tirei o scorpion.py e coloquei no game.py na função abaixo
"""
def cliquenatorre(teste,tempo,mouse,clique,money):
    if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
        clique = True

    return clique

def game(janela):
    fundo = GameImage("imagens/FundoFloresta.jpg")
    janela.set_title("Defense of the Light")

    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
    listatorre = []
    tempo = 0
    """
    dinheiro e vida:
    """
    money = 200
    estrela = GameImage("imagens/star.png")
    estrela.x, estrela.y = [920, 70]
    vida = 40
    coracao = Sprite("imagens/heart.png", 1)
    coracao.x, coracao.y = [920, 10]

    botaoarqueiro = GameImage("imagens/ico_8.png")
    botaoarqueiro.x, botaoarqueiro.y = [970,300]
    clique = False

    torre = Animation("imagens/torrefeita.png",6)
    torre.set_sequence_time(0, 6, 1000, True)

    tiroarco = Sprite("imagens/37.png", 1)
    listatiro = []
    vida_scorpion = 100
    lista_scorpion = []
    listatorrereal = []

    lista_besouro = []
    lista_ogro = []

    contadordebesouro = 0
    contadordeogro = 0
    contadordescorpion = 0


    timeogro = 0
    timeogrotorre = 0

    time = 0
    time2 = 0
    time3 = 0
    timebesouro = 0

    while True:
        tempo += janela.delta_time()
        # mecanicas:
        if (teclado.key_pressed("ESC")):
            break
        """
        vendo se ta sendo click e se te money
        """
        if (mouse.is_over_object(botaoarqueiro) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
            clique = True
            money -= 100
        ""
        """
        vendo se tem vida ainda
        """
        if vida <= 0:
            break

        listatorrreal, clique = movimentotorre(listatorre, mouse, tempo, clique,botaoarqueiro ,torre,listatorrereal)

        lista_scorpion, time, contadordescorpion = scorpionanimation(janela, lista_scorpion, time,contadordescorpion)
        vida = scorpionmovimento(lista_scorpion,janela,vida)
        listatiro, time2, money = tirotorre(torre, lista_scorpion, listatorrereal, listatiro, janela, time2 ,tiroarco, money)
        colisaotorrescorpion(listatorrereal, lista_scorpion)

        lista_besouro, timebesouro, contadordebesouro = besouroanimation(janela, lista_besouro, timebesouro,contadordebesouro)
        vida = besouromovimento(lista_besouro, janela, vida)
        listatiro, time2, money = tirotorrebesouro(torre, lista_besouro, listatorrereal, listatiro, janela, time2, tiroarco,money)
        colisaotorrebesouro(listatorrereal, lista_besouro)

        lista_ogro, timeogro, contadordeogro = ogroanimation(janela, lista_ogro, timeogro, contadordeogro)
        vida = ogromovimento(lista_ogro, janela, vida)
        listatiro, timeogrotorre, money = tirotorreogro(torre, lista_ogro, listatorrereal, listatiro, vida_scorpion, janela, timeogrotorre, tiroarco, money)
        colisaotorreogro(listatorrereal, lista_ogro)

        # desenhos:
        fundo.draw()
        for i in listatorrereal:
            i.draw()
            i.update()
        for i in listatorre:
            i.draw()
            listatorre.remove(i)
            i.update()

        for j in listatiro:
            j.draw()

        for i in lista_ogro:
            i.draw()
            i.update()
        for i in lista_scorpion:
            i.draw()
            i.update()
        for i in lista_besouro:
            i.draw()
            i.update()
        botaoarqueiro.draw()
        janela.draw_text(str(money), 990, 70, 50, (1, 0, 0), "Boulder", False, False)
        estrela.draw()
        janela.draw_text(str(vida), 1000, 10, 50, (1, 0, 0), "Boulder", False, False)
        coracao.draw()
        janela.update()