from PPlay.collision import *
from PPlay.sprite import *

def tirotorrescorpion(torre,lista_scorpion,listatorrereal,listatiro,janela,time2,tiroarco, money, contadorscorpionmorto):
    tiroarco = Sprite("imagens/37.png", 1)
    if time2 >= 4.89:
        for i in listatorrereal:
            if verificararea(i,listatorrereal,lista_scorpion):
                tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                listatiro.append(tiroarco)
        time2 = 0
    else:
        time2 += janela.delta_time()
    movimentodotiro(listatiro, lista_scorpion, janela)
    money, contadorscorpionmorto = colisaoarcoscorpion(listatiro, lista_scorpion, money, contadorscorpionmorto)
    return listatiro, time2 , money, contadorscorpionmorto


def tirotorreogro(torre,lista_ogro,listatorrereal,listatiro,janela,timeogrotorre,tiroarco, money, contadorogromorto):
    tiroarco = Sprite("imagens/37.png", 1)
    if timeogrotorre >= 4.89:
        for i in listatorrereal:
            if verificararea(i,listatorrereal,lista_ogro):
                tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                listatiro.append(tiroarco)
        timeogrotorre = 0
    else:
        timeogrotorre += janela.delta_time()
    movimentodotiro(listatiro, lista_ogro, janela)
    money, contadorogromorto = colisaoarcoscorpion(listatiro, lista_ogro, money, contadorogromorto)
    return listatiro, timeogrotorre , money , contadorogromorto


def tirotorrebesouro(torre,lista_besouro,listatorrereal,listatiro,janela,time3,tiroarco, money, contadorbesouromorto):
    tiroarco = Sprite("imagens/37.png", 1)
    if time3 >= 4.89:
        for i in listatorrereal:
            if verificararea(i,listatorrereal,lista_besouro):
                tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                listatiro.append(tiroarco)
        time3 = 0
    else:
        time3 += janela.delta_time()
    money, contadorbesouromorto = colisaoarcoscorpion(listatiro, lista_besouro, money, contadorbesouromorto)
    movimentodotiro(listatiro, lista_besouro, janela)
    return listatiro, time3, money, contadorbesouromorto


def desenhartiro(listatiro):
    for j in listatiro:
        j.draw()

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

def movimentodotiro(listatiro,lista_scorpion,janela):
    veldotiroarco = 40
    for i in listatiro:
        if 0 <= i.x:
            i.x += veldotiroarco * janela.delta_time() * -1
        if i.x >= janela.width - i.width or i.x < 0 or i.y >= janela.height - i.height or i.y < 0:
            listatiro.remove(i)

def colisaoarcoscorpion(listatiro,lista_scorpion,money, contadorscorpionmorto):
    for i in listatiro:
        for j in lista_scorpion:
            if i.collided(j):
                money += 100
                lista_scorpion.remove(j)
                listatiro.remove(i)
                contadorscorpionmorto += 1
    return money, contadorscorpionmorto


def colisaoarcoarthemis(listatiro,arthemis,money, vidaarthemis):
    for i in listatiro:
        if arthemis.collided(i):
                money += 100
                vidaarthemis += 1
                listatiro.remove(i)
    return money, vidaarthemis