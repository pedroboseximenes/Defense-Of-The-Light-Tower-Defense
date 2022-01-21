
from PPlay.sprite import *

def tirotorre(torre,lista_scorpion,listatorrereal,listatiro,vida_scorpion,janela,time2,tiroarco):
    for i in listatorrereal:
        tiroarco = Sprite("imagens/arqueiro tower/37.png", 1)
        if time2 >= 2.5:
            if verificararea(listatorrereal,lista_scorpion):
                tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                listatiro.append(tiroarco)
            time2 = 0
        movimentodotiro(listatiro, lista_scorpion, janela)
    else:
        time2 += janela.delta_time()
    return listatiro, time2


def desenhartiro(listatiro):
    for j in listatiro:
        j.draw()

def verificararea(listatorrereal,lista_scorpion):
    """
    calcular area em volta da torre e ver se o mob está na area
    :return: True or False
    """
    for i in listatorrereal:
        for j in lista_scorpion:
            if j.x > i.x - 350 or j.x < i.x + 300:
                if j.y > i.y - 350 or j.y < i.y + 300:
                    return True
    return False

def movimentodotiro(listatiro,lista_scorpion,janela):
    veldotiroarco = 5
    for i in listatiro:
        for j in lista_scorpion:
            if i.y < j.y:
                i.y -= veldotiroarco * janela.delta_time()
            if i.y > j.y:
                i.y += veldotiroarco * janela.delta_time()
            if i.x < j.x:
                i.x += veldotiroarco * janela.delta_time()
            if i.x > j.x:
                i.x -= veldotiroarco * janela.delta_time()


