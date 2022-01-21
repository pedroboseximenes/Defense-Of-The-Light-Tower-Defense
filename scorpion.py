from PPlay.sprite import *
from PPlay.animation import *
from random import *
from pygame import *
def scorpionanimation(janela,lista_scorpion,time,contadordescorpion):
    if time >= 5:
        if contadordescorpion <= 20:
            scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
            scorpion.set_sequence_time(0, 19, 50, True)
            t = randint(1,5)
            if t == 1:
                scorpion.x = 3
                scorpion.y = 30
            if t == 2:
                scorpion.x = 3
                scorpion.y = 200
            if t == 3:
                scorpion.x = 3
                scorpion.y = 373
            if t ==4:
                scorpion.x = 3
                scorpion.y = 550
            if t == 5:
                scorpion.x = 3
                scorpion.y = 670
            lista_scorpion.append(scorpion)
            contadordescorpion += 1
        time = 0
    else:
        time += janela.delta_time()
    return lista_scorpion, time, contadordescorpion

def scorpionmovimento(lista_scorpion,janela,vida):
    for scorpion in lista_scorpion:

        velMonstro = 80
        if scorpion.x >= 0:
            scorpion.x += velMonstro * janela.delta_time()
        if scorpion.x > scorpion.height + 1000:
            lista_scorpion.remove(scorpion)
            vida -= 2
    return vida

def colisaotorrescorpion(listatorrereal, lista_scorpions):
    for i in listatorrereal:
        for j in lista_scorpions:
            if j.collided(i):
                listatorrereal.remove(i)
                lista_scorpions.remove(j)
