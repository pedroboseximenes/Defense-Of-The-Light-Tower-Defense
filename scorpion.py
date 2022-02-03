from PPlay.sprite import *
from PPlay.animation import *
from random import *
from pygame import *
def scorpionanimation(janela,lista_scorpion,timescorpion,contadordescorpion,roundgame,fase):
    if fase == 1:
        if timescorpion >= 4:
            if contadordescorpion < 2 + roundgame:
                scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
                scorpion.set_sequence_time(0, 19, 50, True)
                t = randint(1,4)
                if contadordescorpion == 0 or contadordescorpion == 1:
                    t = 3
                if t == 1:
                    scorpion.x = 3
                    scorpion.y = 140
                if t == 2:
                    scorpion.x = 3
                    scorpion.y = 260
                if t == 3:
                    scorpion.x = 3
                    scorpion.y = 450
                if t ==4:
                    scorpion.x = 3
                    scorpion.y = 680
                lista_scorpion.append(scorpion)
                contadordescorpion += 1
            timescorpion = 0
        else:
            timescorpion += janela.delta_time()
        return lista_scorpion, timescorpion, contadordescorpion
    elif fase == 2:
        if timescorpion >= 4:
            if contadordescorpion < 2 + roundgame:
                scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
                scorpion.set_sequence_time(0, 19, 50, True)
                t = randint(1, 4)
                if contadordescorpion == 0 or contadordescorpion == 1:
                    t = 3
                if t == 1:
                    scorpion.x = 3
                    scorpion.y = 70
                if t == 2:
                    scorpion.x = 3
                    scorpion.y = 260
                if t == 3:
                    scorpion.x = 3
                    scorpion.y = 450
                if t == 4:
                    scorpion.x = 3
                    scorpion.y = 600
                lista_scorpion.append(scorpion)
                contadordescorpion += 1
            timescorpion = 0
        else:
            timescorpion += janela.delta_time()
        return lista_scorpion, timescorpion, contadordescorpion
    elif fase == 3:
        if timescorpion >= 4:
            if contadordescorpion < 2 + roundgame:
                scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
                scorpion.set_sequence_time(0, 19, 50, True)
                t = randint(1, 6)
                if t == 1:
                    scorpion.x = 3
                    scorpion.y = 0
                if t == 2:
                    scorpion.x = 3
                    scorpion.y = 100

                if t == 3:
                    scorpion.x = 3
                    scorpion.y = 236
                if t == 4:
                    scorpion.x = 3
                    scorpion.y = 400
                if t == 5:
                    scorpion.x = 3
                    scorpion.y = 550
                if t == 6:
                    scorpion.x = 3
                    scorpion.y = 710
                lista_scorpion.append(scorpion)
                contadordescorpion += 1
            timescorpion = 0
        else:
            timescorpion += janela.delta_time()
        return lista_scorpion, timescorpion, contadordescorpion

def scorpionmovimento(lista_scorpion,janela,vida):
    for scorpion in lista_scorpion:
        velMonstro = 68
        if scorpion.x >= 0:
            scorpion.x += velMonstro * janela.delta_time()
        if scorpion.x > scorpion.height + 1000:
            lista_scorpion.remove(scorpion)
            vida -= 2
    return vida

def colisaotorrescorpion(listatorrereal, lista_scorpions, contadorscorpionmorto):
    for i in listatorrereal:
        for j in lista_scorpions:
            if j.collided(i):
                listatorrereal.remove(i)
                lista_scorpions.remove(j)
                contadorscorpionmorto += 1
    return contadorscorpionmorto