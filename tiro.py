
from PPlay.sprite import *

def tirotorre(torre,scorpion,lista,listatiro,vida_scorpion,janela,time,tiroarco):
    for i in lista:
        tiroarco = Sprite("imagens/arqueiro tower/37.png", 1)
        if time >= 2.1:
            time = 0
            print("chegou aqui")

            tiroarco.x,tiroarco.y = [i.x, i.y]

            if not tiroarco.collided(scorpion):
                if (tiroarco.y > scorpion.y):
                    tiroarco.y -= 3000 * janela.delta_time()
                if tiroarco.x < scorpion.x:
                    tiroarco.x += 30000 * janela.delta_time()
            listatiro.append(tiroarco)
    else:
        time += janela.delta_time()
    return listatiro, time


def desenhartiro(listatiro):
    for j in listatiro:
        j.draw()

