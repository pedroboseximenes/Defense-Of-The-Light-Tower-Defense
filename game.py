from torre import *
from tiro import *
from scorpion import *
from besouro import *
from ogro import *
from torremago import *
from tiromago import *
from torredefesa import *
from torredefesamecanica import *
from vitoriaouderrota import *
from random import randint


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

def cliquenatorre(teste,tempo,mouse,clique,money):
    if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
        clique = True

    return clique

def game(janela,fase):
    if fase == 1:
        fundo = GameImage("imagens/FundoFloresta.jpg")
        janela.set_title("Defense of the Light")
    elif fase == 2:
        fundo = GameImage("imagens/FundoDeserto.jpg")
        janela.set_title("Defense of the Light")
    elif fase == 3:
        fundo = GameImage("imagens/FundoNeve.jpg")
        janela.set_title("Defense of the Light")

    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
    tempo = 0
    """
    dinheiro e vida:
    """
    money = 500
    estrela = GameImage("imagens/star.png")
    estrela.x, estrela.y = [920, 70]
    vida = 10 * fase
    coracao = Sprite("imagens/heart.png", 1)
    coracao.x, coracao.y = [920, 10]
    """
    preço das torres embaixo delas
    """
    precoarqueiro = GameImage("imagens/crystal_1(1).png")
    precoarqueiro.x, precoarqueiro.y = [955,360]
    precomago = GameImage("imagens/crystal_1(1).png")
    precomago.x, precomago.y = [955,460]
    precodefesa = GameImage("imagens/crystal_1(1).png")
    precodefesa.x, precodefesa.y = [955,260]
    valoraqueiro = 100
    valormago = 200
    valordefesa = 500


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
    lista_torre_defesa = []
    torredefesa = Sprite("imagens/7.png",1)
    lista_torre_defesa_real = []
    listavidastorresdefesa = []

    botaoarqueiro = GameImage("imagens/ico_8.png")
    botaoarqueiro.x, botaoarqueiro.y = [970,300]
    botaomago = GameImage("imagens/ico_18.png")
    botaomago.x, botaomago.y = [970,400]
    botaodefesa = GameImage("imagens/ico_2.png")
    botaodefesa.x, botaodefesa.y = [970, 200]


    clique = False
    cliquemago = False
    cliquedefesa = False

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
    contadorscorpionmorto = 0
    contadorogromorto = 0
    contadorbesouromorto = 0


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
        if (mouse.is_over_object(botaodefesa) and mouse.is_button_pressed(1) and tempo >= 0.75 and cliquedefesa == False and money >= 200):
            cliquedefesa = True
            money -= 500
        """
        vendo se tem vida ainda
        """
        if vida <= 0:
            perdeu(janela, mouse)
            break
        if roundgame == 3:
            ganhar(janela,mouse)
            break
        if contadorscorpionmorto == (2 + roundgame) and contadorbesouromorto == (2+roundgame) and contadorogromorto == (3+roundgame):
            roundgame += 1
            contadordescorpion = 0
            contadordeogro = 0
            contadordebesouro = 0
            contadorbesouromorto = 0
            contadorogromorto = 0
            contadorscorpionmorto = 0

        listatorrreal, clique = movimentotorre(listatorre, mouse, tempo, clique,botaoarqueiro ,torre,listatorrereal)
        lista_torre_defesa_real, cliquedefesa, listavidastorresdefesa = movimentotorredefesa(lista_torre_defesa_real,cliquedefesa,mouse,lista_torre_defesa, torredefesa, listavidastorresdefesa)
        lista_torre_mago_real, cliquemago = movimentotorremago(lista_torre_mago_real,cliquemago,mouse,lista_torre_mago, torremago)

        lista_scorpion, timescorpion, contadordescorpion = scorpionanimation(janela, lista_scorpion, timescorpion,contadordescorpion, roundgame,fase)
        vida = scorpionmovimento(lista_scorpion,janela,vida)
        listatiro, time2, money, contadorscorpionmorto = tirotorrescorpion(torre, lista_scorpion, listatorrereal, listatiro, janela, time2 ,tiroarco, money, contadorscorpionmorto)
        ##mago
        lista_raio_mago,timemago, money, contadorscorpionmorto = raiomagoscorpion(lista_scorpion,janela,lista_raio_mago,lista_torre_mago_real,timemago2,money, contadorscorpionmorto)
        contadorscorpionmorto =colisaotorrescorpion(listatorrereal, lista_scorpion, contadorscorpionmorto)
        contadorscorpionmorto = colisaotorrescorpion(lista_torre_mago_real, lista_scorpion, contadorscorpionmorto)
        listavidastorresdefesa, money, contadorscorpionmorto = colisaotorredefesascorpion(lista_torre_defesa_real, lista_scorpion, listavidastorresdefesa, money, contadorscorpionmorto)

        lista_besouro, timebesouro, contadordebesouro = besouroanimation(janela, lista_besouro, timebesouro,contadordebesouro, roundgame, fase)
        vida = besouromovimento(lista_besouro, janela, vida)
        listatiro, time2, money, contadorbesouromorto = tirotorrebesouro(torre, lista_besouro, listatorrereal, listatiro, janela, time2, tiroarco,money, contadorbesouromorto)
        lista_raio_mago,timemago3, money, contadorbesouromorto = raiomagobesouro(lista_besouro, janela, lista_raio_mago, lista_torre_mago_real, timemago3, money, contadorbesouromorto)
        contadorbesouromorto = colisaotorrebesouro(listatorrereal, lista_besouro, contadorbesouromorto)
        contadorbesouromorto = colisaotorrebesouro(lista_torre_mago_real, lista_besouro, contadorbesouromorto)
        listavidastorresdefesa, money, contadorbesouromorto = colisaotorredefesabesouro(lista_torre_defesa_real, lista_besouro, listavidastorresdefesa, money, contadorbesouromorto)


        lista_ogro, timeogro, contadordeogro = ogroanimation(janela, lista_ogro, timeogro, contadordeogro, roundgame,fase)
        vida = ogromovimento(lista_ogro, janela, vida)
        listatiro, timeogrotorre, money, contadorogromorto = tirotorreogro(torre, lista_ogro, listatorrereal, listatiro, janela, timeogrotorre, tiroarco, money, contadorogromorto)
        lista_raio_mago, timemago2, money, contadorogromorto = raiomagoogro(lista_ogro,janela,lista_raio_mago,lista_torre_mago_real,timemago2,money, contadorogromorto)
        contadorogromorto = colisaotorreogro(listatorrereal, lista_ogro, contadorogromorto)
        contadorogromorto = colisaotorreogro(lista_torre_mago_real, lista_ogro, contadorogromorto)
        listavidastorresdefesa, money, contadorogromorto = colisaotorredefesaogro(lista_torre_defesa_real, lista_ogro, listavidastorresdefesa, money, contadorogromorto)

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
        for i in lista_torre_defesa:
            i.draw()
            lista_torre_defesa.remove(i)
        for i in lista_torre_defesa_real:
            i.draw()

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
        botaodefesa.draw()
        precoarqueiro.draw()
        precomago.draw()
        precodefesa.draw()

        janela.draw_text(str(money), 990, 70, 50, (1, 0, 0), "Boulder", False, False)
        estrela.draw()
        janela.draw_text(str(vida), 1000, 10, 50, (1, 0, 0), "Boulder", False, False)
        coracao.draw()
        janela.draw_text(str(roundgame), janela.width/2, 10, 50, (1, 0, 0), "Boulder", False, False)

        janela.draw_text(str(valoraqueiro), 975, 360, 25, (1, 0, 0), "Boulder", False, False)
        janela.draw_text(str(valormago), 975, 460, 25, (1, 0, 0), "Boulder", False, False)
        janela.draw_text(str(valordefesa), 975, 260, 25, (1, 0, 0), "Boulder", False, False)
        janela.update()