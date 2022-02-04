from PPlay.animation import *
from random import *
def ogroanimation(janela,lista_ogro,time,contadordeogro, roundgame,fase, lista_vida_ogros):
    if fase == 1:
        if time >= 10:
            if contadordeogro < 3 + roundgame:
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
                vidaogro = 2
                lista_vida_ogros.append(vidaogro)
                lista_ogro.append(ogro)
                contadordeogro += 1
            time = 0
        else:
            time += janela.delta_time()
        return lista_ogro, time, contadordeogro, lista_vida_ogros
    elif fase == 2:
        if time >= 10:
            if contadordeogro < 3 * roundgame:
                ogro = Animation("imagens/ogro.png", 20, True)
                ogro.set_sequence_time(0, 19, 70, True)
                t = randint(1, 4)
                if t == 1:
                    ogro.x = 3
                    ogro.y = 70
                if t == 2:
                    ogro.x = 3
                    ogro.y = 260
                if t == 3:
                    ogro.x = 3
                    ogro.y = 450
                if t == 4:
                    ogro.x = 3
                    ogro.y = 600
                vidaogro = 2
                lista_vida_ogros.append(vidaogro)
                lista_ogro.append(ogro)
                contadordeogro += 1
            time = 0
        else:
            time += janela.delta_time()
        return lista_ogro, time, contadordeogro, lista_vida_ogros
    elif fase == 3:
        if time >= 6:
            if contadordeogro < 3 * roundgame:
                ogro = Animation("imagens/ogro.png", 20, True)
                ogro.set_sequence_time(0, 19, 50, True)
                t = randint(1, 6)
                if t == 1:
                    ogro.x = 3
                    ogro.y = 0

                if t == 2:
                    ogro.x = 3
                    ogro.y = 100

                if t == 3:
                    ogro.x = 3
                    ogro.y = 236

                if t == 4:
                    ogro.x = 3
                    ogro.y = 400

                if t == 5:
                    ogro.x = 3
                    ogro.y = 550

                if t == 6:
                    ogro.x = 3
                    ogro.y = 710
                vidaogro = 2
                lista_vida_ogros.append(vidaogro)
                lista_ogro.append(ogro)
                contadordeogro += 1
            time = 0
        else:
            time += janela.delta_time()
        return lista_ogro, time, contadordeogro, lista_vida_ogros

def ogromovimento(lista_ogro,janela,vida, contadorogromorto):
    for ogro in lista_ogro:
        velMonstro = 30
        if ogro.x >= 0:
            ogro.x += velMonstro * janela.delta_time()
        if ogro.x > ogro.height + 1000:
            lista_ogro.remove(ogro)
            vida -= 3
            contadorogromorto += 1
    return vida, contadorogromorto

def colisaotorreogro(listatorrereal, lista_ogro, contadorogromorto,lista_vida_ogros):
    for i in listatorrereal:
        for j in range (len(lista_ogro)):
            for k in range(len(lista_vida_ogros)):
                if k == j:
                    if lista_ogro[j].collided(i):
                        listatorrereal.remove(i)
                        lista_vida_ogros[j] -= 1
                        #contadorogromorto += 1
    return contadorogromorto, lista_vida_ogros

def verificarvidaogro(lista_vida_ogros, lista_ogro, contadorogromorto):
    for j in range(len(lista_ogro)):
        for i in range(len(lista_vida_ogros)):
            if i == j :
                if lista_vida_ogros[i] <= 0:
                    lista_ogro.remove(lista_ogro[j])
                    lista_vida_ogros.remove(lista_vida_ogros[j])
                    contadorogromorto += 1
    return lista_ogro, contadorogromorto
