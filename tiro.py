from PPlay.collision import *
from PPlay.sprite import *

def tirotorre(torre,lista_scorpion,listatorrereal,listatiro,vida_scorpion,janela,time2,tiroarco, money):
    tiroarco = Sprite("imagens/arqueiro tower/37.png", 1)
    if time2 >= 4.89:
        for i in listatorrereal:
            if verificararea(i,listatorrereal,lista_scorpion):
                tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                listatiro.append(tiroarco)
        time2 = 0
    else:
        time2 += janela.delta_time()
    movimentodotiro(listatiro, lista_scorpion, janela)
    money = colisaoarcoscorpion(listatiro, lista_scorpion, money)
    return listatiro, time2 , money


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
        for j in lista_scorpion:
            if 0 < i.x:
                i.x += veldotiroarco * janela.delta_time() * -1
        if i.x >= janela.width - i.width or i.x < 0 or i.y >= janela.height - i.height or i.y < 0:
            listatiro.remove(i)

def colisaoarcoscorpion(listatiro,lista_scorpion,money):
    for i in listatiro:
        for j in lista_scorpion:
            if i.collided(j):
                money += 100
                lista_scorpion.remove(j)
                listatiro.remove(i)
    return money

