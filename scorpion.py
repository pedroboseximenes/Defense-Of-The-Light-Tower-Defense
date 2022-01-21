from PPlay.animation import *
from PPlay.sprite import *
from pygame import *
def scorpionanimation(janela,lista_scorpion):
    for i in range(3):
        scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
        scorpion.set_sequence_time(0, 19, 50, True)
        lista_scorpion.append(scorpion)
    return lista_scorpion

def scorpionmovimento(lista_scorpion,janela):
    for scorpion in lista_scorpion:
        velMonstro = 80
        if scorpion.x >= 0:
            if scorpion.x < janela.height:
                scorpion.x += velMonstro * janela.delta_time()
        if scorpion.x > 690:
            scorpion.y += velMonstro * janela.delta_time()