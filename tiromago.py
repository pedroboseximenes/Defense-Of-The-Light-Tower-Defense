from PPlay.animation import *
from PPlay.sprite import *
from PPlay.collision import *


def raiomagoscorpion(lista_scorpion,janela,lista_raio_mago,lista_torre_mago_real,timemago,money, contadorscorpionmorto, upgradetorremago):
    raiomago = Animation("imagens/raioTorre.png", 4)
    raiomago.set_sequence_time(0, 3, 80, True)
    for j in range(len(upgradetorremago)):
        if timemago >= 4.89 - (upgradetorremago[j] * 0.22):
            for i in lista_torre_mago_real:
                if verificararea(i,lista_torre_mago_real,lista_scorpion):
                    raiomago.x,raiomago.y = [i.x-35, i.y+15]
                    lista_raio_mago.append(raiomago)
            timemago = 0
    else:
        timemago += janela.delta_time()
    movimentodotiro(lista_raio_mago, lista_scorpion, janela, upgradetorremago)
    money, contadorscorpionmorto = colisaoraiomob(lista_raio_mago, lista_scorpion, money, contadorscorpionmorto)
    return lista_raio_mago, timemago , money, contadorscorpionmorto


def raiomagoogro(lista_ogro,janela,lista_raio_mago,lista_torre_mago_real,timemago2,money, contadorogromorto, lista_vida_ogros, upgradetorremago):
    raiomago = Animation("imagens/raioTorre.png", 4)
    raiomago.set_sequence_time(0, 3, 80, True)
    for j in range(len(upgradetorremago)):
        if timemago2 >= 4.89 - (upgradetorremago[j] * 0.22):
            for i in lista_torre_mago_real:
                if verificararea(i, lista_torre_mago_real, lista_ogro):
                    raiomago.x, raiomago.y = [i.x-35, i.y+15]
                    lista_raio_mago.append(raiomago)
            timemago2 = 0
    else:
        timemago2 += janela.delta_time()
    movimentodotiro(lista_raio_mago, lista_ogro, janela, upgradetorremago)
    money, contadorogromorto, lista_vida_ogros = colisaomagoogro(lista_raio_mago,lista_ogro,money, contadorogromorto, lista_vida_ogros)
    return lista_raio_mago, timemago2, money, contadorogromorto, lista_vida_ogros


def raiomagobesouro(lista_besouro,janela,lista_raio_mago,lista_torre_mago_real,timemago3,money, contadorbesouromorto, upgradetorremago):
    raiomago = Animation("imagens/raioTorre.png", 4)
    raiomago.set_sequence_time(0, 3, 80, True)
    for j in range(len(upgradetorremago)):
        if timemago3 >= 4.89 - (upgradetorremago[j] * 0.22):
            for i in lista_torre_mago_real:
               if verificararea(i, lista_torre_mago_real, lista_besouro):
                    raiomago.x, raiomago.y = [i.x-35, i.y+15]
                    lista_raio_mago.append(raiomago)
            timemago3 = 0
    else:
        timemago3 += janela.delta_time()
    movimentodotiro(lista_raio_mago, lista_besouro, janela, upgradetorremago)
    money, contadorbesouromorto = colisaoraiomob(lista_raio_mago, lista_besouro, money, contadorbesouromorto)
    return lista_raio_mago, timemago3, money, contadorbesouromorto


def raiomagoarthemis(arthemis,janela,lista_raio_mago,lista_torre_mago_real,time3,money, vidaarthemis, upgradetorremago):
    raiomago = Animation("imagens/raioTorre.png", 4)
    raiomago.set_sequence_time(0, 3, 80, True)
    for j in range(len(upgradetorremago)):
        if time3 >= 4.89 - (upgradetorremago[j] * 0.22):
            for i in lista_torre_mago_real:
                if verificarareaarthemis(i,lista_torre_mago_real, arthemis):
                    raiomago.x,raiomago.y = [i.x-35, i.y+15]
                    lista_raio_mago.append(raiomago)
            time3 = 0
    else:
        time3 += janela.delta_time()
    money, vidaarthemis = colisaoarcoarthemis(lista_raio_mago,arthemis,money,vidaarthemis)
    movimentodotiro(lista_raio_mago, arthemis, janela, upgradetorremago)
    return lista_raio_mago, time3, money, vidaarthemis

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

def verificarareaarthemis(i,listatorrereal,arthemis):
    if (i.y - 200 < arthemis.y < i.y + 200) or arthemis.y == i.y:
        return True
    return False

def movimentodotiro(lista_raio_mago,lista_scorpion,janela, upgradetorremago):
    for j in range (len(upgradetorremago)):
        veldotiroraio = 10 +(upgradetorremago[j] * 4)
        for i in lista_raio_mago:
            if 0 <= i.x:
                i.x += veldotiroraio * janela.delta_time() * -1
            if i.x >= janela.width - i.width or i.x < 0 or i.y >= janela.height - i.height or i.y < 0:
                lista_raio_mago.remove(i)

def colisaoraiomob(lista_raio_mago,lista_scorpion,money, contadorscorpionmorto):
    for i in lista_raio_mago:
        for j in lista_scorpion:
            if i.collided(j):
                money += 150
                lista_scorpion.remove(j)
                lista_raio_mago.remove(i)
                contadorscorpionmorto += 1
    return money, contadorscorpionmorto

def colisaoarcoarthemis(lista_raio_mago,arthemis,money, vidaarthemis):
    for i in lista_raio_mago:
        if Collision.collided(i, arthemis):
            money += 100
            lista_raio_mago.remove(i)
            vidaarthemis += 1
    return money, vidaarthemis

def colisaomagoogro(lista_raio_mago,lista_scorpion,money, contadorscorpionmorto, lista_vida_ogros):
    for i in lista_raio_mago:
        for j in lista_scorpion:
            if i.collided(j):
                money += 150
                lista_scorpion.remove(j)
                lista_raio_mago.remove(i)
                contadorscorpionmorto += 1
    return money, contadorscorpionmorto, lista_vida_ogros