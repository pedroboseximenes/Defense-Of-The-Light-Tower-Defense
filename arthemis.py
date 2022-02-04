from PPlay.animation import *
from random import *
from PPlay.collision import *
def arthemisanimation(janela):
    arthemis = Animation("imagens/ARTHEMIS.png", 20, True)
    arthemis.set_sequence_time(0, 19, 50, True)
    t = randint(1, 6)
    arthemis.x = 3
    if t == 1:
        arthemis.y = 0
    if t == 2:
        arthemis.y = 100
    if t == 3:
        arthemis.y = 236
    if t == 4:
        arthemis.y = 400
    if t == 5:
        arthemis.y = 550
    if t == 6:
        arthemis.y = 710
    return arthemis

def arthemismovimento(arthemis,janela,vida):
    velarthemis = 20
    if arthemis.x >= 0:
        arthemis.x += velarthemis * janela.delta_time()
    if arthemis.x > arthemis.height +877:
        vida -= 50
    return vida

def colisaotorrearthemis(listatorrereal, arthemis, vidaarthemis):
    for i in listatorrereal:
        if arthemis.collided(i):
            listatorrereal.remove(i)
            vidaarthemis += 1
    return vidaarthemis

def colisaotorremagoarthemis(lista_torre_mago_real, arthemis, vidaarthemis):
    for i in lista_torre_mago_real:
        if arthemis.collided(i):
            lista_torre_mago_real.remove(i)
            vidaarthemis += 1
    return vidaarthemis
def colisaotorredefesaarthemis(lista_torre_defesa_real, arthemis, vidaarthemis):
    for i in lista_torre_defesa_real:
        if arthemis.collided(i):
            lista_torre_defesa_real.remove(i)
            vidaarthemis += 1
    return vidaarthemis

def arthemisbullet(janela, arthemis):
    hadoken = Animation("imagens/hadoken.png", 1)
    hadoken.x = arthemis.x +60
    hadoken.y = arthemis.y +60
    return hadoken

def hadokencolisao(janela, listatorrereal, torre_mago_real, torre_defesa_real, hadoken):
    hadoken.x += 300 * janela.delta_time()
    a = True
    for i in listatorrereal:
        if i.collided(hadoken):
            listatorrereal.remove(i)
            a = False
    for i in torre_mago_real:
        if i.collided(hadoken):
            torre_mago_real.remove(i)
            a = False
    for i in torre_defesa_real:
        if i.collided(hadoken):
            torre_defesa_real.remove(i)
            a = False
    return listatorrereal, torre_mago_real, torre_defesa_real,  a