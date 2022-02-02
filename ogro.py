from PPlay.animation import *
from random import *
def ogroanimation(janela,lista_ogro,time,contadordeogro, roundgame):
    if time >= 10:
        if contadordeogro <= 4 * roundgame:
            ogro = Animation("imagens/ogro.png", 20, True)
            ogro.set_sequence_time(0, 19, 70, True)
            t = randint(1, 4)
            if t == 1:
                ogro.x = 3
                ogro.y = 140
            if t == 2:
                ogro.x = 3
                ogro.y = 260
            if t == 3:
                ogro.x = 3
                ogro.y = 450
            if t == 4:
                ogro.x = 3
                ogro.y = 680
            lista_ogro.append(ogro)
            contadordeogro += 1
        time = 0
    else:
        time += janela.delta_time()
    return lista_ogro, time, contadordeogro

def ogromovimento(lista_ogro,janela,vida):
    for ogro in lista_ogro:
        velMonstro = 50
        if ogro.x >= 0:
            ogro.x += velMonstro * janela.delta_time()
        if ogro.x > ogro.height + 1000:
            lista_ogro.remove(ogro)
            vida -= 2
    return vida

def colisaotorreogro(listatorrereal, lista_ogro):
    for i in listatorrereal:
        for j in lista_ogro:
            if j.collided(i):
                listatorrereal.remove(i)
                lista_ogro.remove(j)
