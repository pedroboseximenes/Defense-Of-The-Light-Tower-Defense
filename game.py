from torre import *
from tiro import *
from scorpion import *
from besouro import *
from ogro import *
from torremago import *
from tiromago import *
from random import randint
def cliquenatorre(teste,tempo,mouse,clique,money):
    if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
        clique = True

    return clique

def game(janela):
    fundo = GameImage("imagens/FundoFloresta.jpg")
    janela.set_title("Defense of the Light")

    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
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
    """
    torres !!!!!!!!!!!!
    """
    listatorre = []
    torre = Animation("imagens/torrefeita.png", 6)
    torre.set_sequence_time(0, 6, 1000, True)
    listatorrereal = []
    lista_torre_mago = []
    torremago = Sprite("imagens/magic-1.png",1)
    lista_torre_mago_real = []

    botaoarqueiro = GameImage("imagens/ico_8.png")
    botaoarqueiro.x, botaoarqueiro.y = [970,300]
    botaomago = GameImage("imagens/ico_18.png")
    botaomago.x, botaomago.y = [970,400]
    clique = False
    cliquemago = False

    roundgame = 1

    tiroarco = Sprite("imagens/37.png", 1)
    listatiro = []

    lista_raio_mago = []

    lista_scorpion = []
    lista_besouro = []
    lista_ogro = []

    contadordebesouro = 0
    contadordeogro = 0
    contadordescorpion = 0


    timeogro = 0
    timescorpion = 0

    """
    TEMPO UTILIZADO P FLECHA SER CRIADA, ABAIXO:
    """
    timeogrotorre = 0
    time2 = 0
    time3 = 0
    """
    TEMPO UTILIZADO P RAIO SER CRIADO, ABAIXO:
    """
    timemago2 = 0
    timemago = 0
    timemago3 = 0


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
        if (mouse.is_over_object(botaomago) and mouse.is_button_pressed(1) and tempo >= 0.75 and cliquemago == False and money >= 200):
            cliquemago = True
            money -= 200
        """
        vendo se tem vida ainda
        """
        if vida <= 0 or roundgame == 5:
            break
        if contadordescorpion == (3 * roundgame) and contadordeogro == (4 * roundgame) and contadordebesouro == (3 *roundgame):
            roundgame += 1
            contadordescorpion = 0
            contadordeogro = 0
            contadordebesouro = 0

        listatorrreal, clique = movimentotorre(listatorre, mouse, tempo, clique,botaoarqueiro ,torre,listatorrereal)
        lista_torre_mago_real, cliquemago = movimentotorremago(lista_torre_mago_real,cliquemago,mouse,lista_torre_mago, torremago)

        lista_scorpion, timescorpion, contadordescorpion = scorpionanimation(janela, lista_scorpion, timescorpion,contadordescorpion, roundgame)
        vida = scorpionmovimento(lista_scorpion,janela,vida)
        listatiro, time2, money = tirotorrescorpion(torre, lista_scorpion, listatorrereal, listatiro, janela, time2 ,tiroarco, money)
        ##mago
        lista_raio_mago,timemago, money = raiomagoscorpion(lista_scorpion,janela,lista_raio_mago,lista_torre_mago_real,timemago2,money)
        colisaotorrescorpion(listatorrereal, lista_scorpion)
        colisaotorrescorpion(lista_torre_mago_real, lista_scorpion)

        lista_besouro, timebesouro, contadordebesouro = besouroanimation(janela, lista_besouro, timebesouro,contadordebesouro, roundgame)
        vida = besouromovimento(lista_besouro, janela, vida)
        listatiro, time2, money = tirotorrebesouro(torre, lista_besouro, listatorrereal, listatiro, janela, time2, tiroarco,money)
        lista_raio_mago,timemago3, money = raiomagobesouro(lista_besouro, janela, lista_raio_mago, lista_torre_mago_real, timemago3, money)
        colisaotorrebesouro(listatorrereal, lista_besouro)
        colisaotorrebesouro(lista_torre_mago_real, lista_besouro)

        lista_ogro, timeogro, contadordeogro = ogroanimation(janela, lista_ogro, timeogro, contadordeogro, roundgame)
        vida = ogromovimento(lista_ogro, janela, vida)
        listatiro, timeogrotorre, money = tirotorreogro(torre, lista_ogro, listatorrereal, listatiro, janela, timeogrotorre, tiroarco, money)
        lista_raio_mago, timemago2, money = raiomagoogro(lista_ogro,janela,lista_raio_mago,lista_torre_mago_real,timemago2,money)
        colisaotorreogro(listatorrereal, lista_ogro)
        colisaotorreogro(lista_torre_mago_real, lista_ogro)

        # desenhos:
        fundo.draw()
        for i in listatorrereal:
            i.draw()
            i.update()
        for i in listatorre:
            i.draw()
            listatorre.remove(i)
            i.update()
        for i in lista_torre_mago_real:
            i.draw()
        for i in lista_torre_mago:
            i.draw()
            lista_torre_mago.remove(i)

        for j in listatiro:
            j.draw()
        for i in lista_raio_mago:
            i.draw()
            i.update()

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
        botaomago.draw()
        janela.draw_text(str(money), 990, 70, 50, (1, 0, 0), "Boulder", False, False)
        estrela.draw()
        janela.draw_text(str(vida), 1000, 10, 50, (1, 0, 0), "Boulder", False, False)
        coracao.draw()
        janela.draw_text(str(roundgame), janela.width/2, 10, 50, (1, 0, 0), "Boulder", False, False)
        janela.update()