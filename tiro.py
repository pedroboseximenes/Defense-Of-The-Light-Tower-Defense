from PPlay.collision import *
from PPlay.sprite import *

def tirotorrescorpion(torre,lista_scorpion,listatorrereal,listatiro,janela,time2,tiroarco, money, contadorscorpionmorto, upgradetorrearco):
    tiroarco = Sprite("imagens/37.png", 1)
    for j in range(len(upgradetorrearco)):
        if time2 >= 4.89  - (upgradetorrearco[j] * 0.3) :
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


def tirotorreogro(torre,lista_ogro,listatorrereal,listatiro,janela,timeogrotorre,tiroarco, money, contadorogromorto,lista_vida_ogros, upgradetorrearco):
    tiroarco = Sprite("imagens/37.png", 1)
    for j in range(len(upgradetorrearco)):
        if timeogrotorre >= 4.89  - (upgradetorrearco[j] * 0.3):
            for i in listatorrereal:
                if verificararea(i,listatorrereal,lista_ogro):
                    tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                    listatiro.append(tiroarco)
            timeogrotorre = 0
        else:
            timeogrotorre += janela.delta_time()
    movimentodotiro(listatiro, lista_ogro, janela)
    money, contadorogromorto, lista_vida_ogros = colisaoarcoogro(listatiro,lista_ogro,money, contadorogromorto, lista_vida_ogros)
    return listatiro, timeogrotorre , money , contadorogromorto, lista_vida_ogros


def tirotorrebesouro(torre,lista_besouro,listatorrereal,listatiro,janela,time3,tiroarco, money, contadorbesouromorto, upgradetorrearco):
    tiroarco = Sprite("imagens/37.png", 1)
    for j in range(len(upgradetorrearco)):
        if time3 >= 7.89 - (upgradetorrearco[j] * 0.3):
            for i in listatorrereal:
                print(upgradetorrearco)
                if verificararea(i,listatorrereal,lista_besouro):
                    tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                    listatiro.append(tiroarco)
            time3 = 0
        else:
            time3 += janela.delta_time()
    money, contadorbesouromorto = colisaoarcoscorpion(listatiro, lista_besouro, money, contadorbesouromorto)
    movimentodotiro(listatiro, lista_besouro, janela)
    return listatiro, time3, money, contadorbesouromorto

def tirotorrearthemis(torre,arthemis,listatorrereal,listatiro,janela,time3,tiroarco, money, vidaarthemis, upgradetorrearco):
    tiroarco = Sprite("imagens/37.png", 1)
    for j in range(len(upgradetorrearco)):
        if time3 >= 4.89 - (upgradetorrearco[j] * 0.3):
            for i in listatorrereal:
                if verificarareaarthemis(i,listatorrereal, arthemis):
                    tiroarco.x,tiroarco.y = [i.x + 45, i.y + 30]
                    listatiro.append(tiroarco)
            time3 = 0
        else:
            time3 += janela.delta_time()
    money, vidaarthemis = colisaoarcoarthemis(listatiro,arthemis,money,vidaarthemis)
    movimentodotiro(listatiro, arthemis, janela)
    return listatiro, time3, money, vidaarthemis


def desenhartiro(listatiro):
    for j in listatiro:
        j.draw()
def verificarareaarthemis(i,listatorrereal,arthemis):
    if (i.y - 270 < arthemis.y < i.y + 270) or arthemis.y == i.y:
        return True
    return False
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
    veldotiroarco = 20
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
        if Collision.collided(i, arthemis):
            money += 100
            listatiro.remove(i)
            vidaarthemis += 1
    return money, vidaarthemis

def colisaoarcoogro(listatiro,lista_scorpion,money, contadorscorpionmorto, lista_vida_ogros):
    for i in listatiro:
        for j in range (len(lista_scorpion)):
            for k in range(len(lista_vida_ogros)):
                if j ==k:
                    if i.collided(lista_scorpion[j]):
                        money += 100
                        lista_vida_ogros[j] -= 1
                        listatiro.remove(i)
    return money, contadorscorpionmorto, lista_vida_ogros