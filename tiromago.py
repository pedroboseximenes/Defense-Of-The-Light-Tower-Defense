from PPlay.animation import *
from PPlay.sprite import *

def raiomagoscorpion(lista_scorpion,janela,lista_raio_mago,lista_torre_mago_real,timemago,money):
    raiomago = Animation("imagens/raioTorre.png", 4)
    raiomago.set_sequence_time(0, 3, 80, True)
    if timemago >= 4.89:
        for i in lista_torre_mago_real:
            if verificararea(i,lista_torre_mago_real,lista_scorpion):
                raiomago.x,raiomago.y = [i.x-35, i.y+15]
                lista_raio_mago.append(raiomago)
        timemago = 0
    else:
        timemago += janela.delta_time()
    movimentodotiro(lista_raio_mago, lista_scorpion, janela)
    money = colisaoraiomob(lista_raio_mago, lista_scorpion, money)
    return lista_raio_mago, timemago , money


def raiomagoogro(lista_ogro,janela,lista_raio_mago,lista_torre_mago_real,timemago2,money):
    raiomago = Animation("imagens/raioTorre.png", 4)
    raiomago.set_sequence_time(0, 3, 80, True)
    if timemago2 >= 4.89:
        for i in lista_torre_mago_real:
            if verificararea(i, lista_torre_mago_real, lista_ogro):
                raiomago.x, raiomago.y = [i.x-35, i.y+15]
                lista_raio_mago.append(raiomago)
        timemago2 = 0
    else:
        timemago2 += janela.delta_time()
    movimentodotiro(lista_raio_mago, lista_ogro, janela)
    money = colisaoraiomob(lista_raio_mago, lista_ogro, money)
    return lista_raio_mago, timemago2, money


def raiomagobesouro(lista_besouro,janela,lista_raio_mago,lista_torre_mago_real,timemago3,money):
    raiomago = Animation("imagens/raioTorre.png", 4)
    raiomago.set_sequence_time(0, 3, 80, True)
    if timemago3 >= 4.89:
        for i in lista_torre_mago_real:
            if verificararea(i, lista_torre_mago_real, lista_besouro):
                raiomago.x, raiomago.y = [i.x-35, i.y+15]
                lista_raio_mago.append(raiomago)
        timemago3 = 0
    else:
        timemago3 += janela.delta_time()
    movimentodotiro(lista_raio_mago, lista_besouro, janela)
    money = colisaoraiomob(lista_raio_mago, lista_besouro, money)
    return lista_raio_mago, timemago3, money

""""
def desenhartiro(listatiro):
    for j in listatiro:
        j.draw()
"""
def verificararea(i,listatorrereal,lista_scorpion):
    """
    calcular area em volta da torre e ver se o mob está na area
    :return: True or False
    """
    #for i in listatorrereal:
    for j in lista_scorpion:
        if (i.y - 60 < j.y < i.y + 60) or j.y == i.y:
             return True
    return False

def movimentodotiro(lista_raio_mago,lista_scorpion,janela):
    veldotiroraio = 20
    for i in lista_raio_mago:
        if 0 <= i.x:
            i.x += veldotiroraio * janela.delta_time() * -1
        if i.x >= janela.width - i.width or i.x < 0 or i.y >= janela.height - i.height or i.y < 0:
            lista_raio_mago.remove(i)

def colisaoraiomob(lista_raio_mago,lista_scorpion,money):
    for i in lista_raio_mago:
        for j in lista_scorpion:
            if i.collided(j):
                money += 150
                lista_scorpion.remove(j)
                lista_raio_mago.remove(i)
    return money