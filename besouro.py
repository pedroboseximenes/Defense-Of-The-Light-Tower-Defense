from PPlay.sprite import *
from PPlay.animation import *
from random import *
from pygame import *
def besouroanimation(janela,lista_besouro,time,contadordebesouro, roundgame):
    if time >= 18:
        if contadordebesouro <= 3 * roundgame:
            besouro = Animation("imagens/besouropeludo.png", 10, True)
            besouro.set_sequence_time(0, 9, 40, True)
            t = randint(1,4)
            if t == 1:
                besouro.x = 3
                besouro.y = 140
            if t == 2:
                besouro.x = 3
                besouro.y = 260
            if t == 3:
                besouro.x = 3
                besouro.y = 450
            if t ==4:
                besouro.x = 3
                besouro.y = 680
            lista_besouro.append(besouro)
            contadordebesouro += 1
        time = 0
    else:
        time += janela.delta_time()
    return lista_besouro, time, contadordebesouro

def besouromovimento(lista_besouro,janela,vida):
    for besouro in lista_besouro:

        velMonstro = 80
        if besouro.x >= 0:
            besouro.x += velMonstro * janela.delta_time()
        if besouro.x > besouro.height + 1000:
            lista_besouro.remove(besouro)
            vida -= 2
    return vida

def colisaotorrebesouro(listatorrereal, lista_besouro):
    for i in listatorrereal:
        for j in lista_besouro:
            if j.collided(i):
                listatorrereal.remove(i)
                lista_besouro.remove(j)