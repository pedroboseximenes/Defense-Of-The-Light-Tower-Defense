from PPlay.animation import *
from PPlay.sprite import *
from pygame import *
def scorpionanimation(janela):
    scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
    scorpion.x = 100
    scorpion.y = 375
    scorpion.set_sequence_time(0, 19, 50, True)
    return scorpion

def scorpionmovimento(scorpion,janela):
    velMonstro = 80
    if scorpion.x >= 0:
        if scorpion.x < janela.height:
            scorpion.x += velMonstro * janela.delta_time()
    if scorpion.x > 690:
        scorpion.y += velMonstro * janela.delta_time()