from PPlay.sprite import *
from PPlay.animation import *
from random import *
from pygame import *
def besouroanimation(janela,lista_besouro,time,contadordebesouro, roundgame, fase):
    if fase == 1:
        if time >= 18:
            if contadordebesouro < 2 + roundgame:
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

    elif fase == 2:
        if time >= 13:
            if contadordebesouro < 2 * roundgame:
                besouro = Animation("imagens/besouropeludo.png", 10, True)
                besouro.set_sequence_time(0, 9, 40, True)
                t = randint(1,4)
                if t == 1:
                    besouro.x = 3
                    besouro.y = 70
                if t == 2:
                    besouro.x = 3
                    besouro.y = 260
                if t == 3:
                    besouro.x = 3
                    besouro.y = 450
                if t ==4:
                    besouro.x = 3
                    besouro.y = 600
                lista_besouro.append(besouro)
                contadordebesouro += 1
            time = 0
        else:
            time += janela.delta_time()
        return lista_besouro, time, contadordebesouro

    elif fase == 3:
        if time >= 7:
            if contadordebesouro < 3 * roundgame:
                besouro = Animation("imagens/besouropeludo.png", 10, True)
                besouro.set_sequence_time(0, 9, 40, True)
                t = randint(1, 6)
                if t == 1:
                    besouro.x = 3
                    besouro.y = 0
                if t == 2:
                    besouro.x = 3
                    besouro.y = 100

                if t == 3:
                    besouro.x = 3
                    besouro.y = 236

                if t == 4:
                    besouro.x = 3
                    besouro.y = 400

                if t == 5:
                    besouro.x = 3
                    besouro.y = 550

                if t == 6:
                    besouro.x = 3
                    besouro.y = 710
                lista_besouro.append(besouro)
                contadordebesouro += 1
            time = 0
        else:
            time += janela.delta_time()
        return lista_besouro, time, contadordebesouro

def besouromovimento(lista_besouro,janela,vida, contadorbesouromorto):
    for besouro in lista_besouro:

        velMonstro = 40
        if besouro.x >= 0:
            besouro.x += velMonstro * janela.delta_time()
        if besouro.x > besouro.height + 1000:
            lista_besouro.remove(besouro)
            vida -= 2
            contadorbesouromorto += 1
    return vida, contadorbesouromorto

def colisaotorrebesouro(listatorrereal, lista_besouro, contadorbesouromorto):
    for i in listatorrereal:
        for j in lista_besouro:
            if j.collided(i):
                listatorrereal.remove(i)
                lista_besouro.remove(j)
                contadorbesouromorto += 1
    return contadorbesouromorto