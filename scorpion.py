from PPlay.animation import *
from PPlay.sprite import *
from pygame import *
def scorpionanimation(janela):
    scorpion = Animation("imagens/escopion_andando_metade.png", 20, True)
    scorpion.x = janela.width/2 - scorpion.width/2
    scorpion.y = janela.height/2 - scorpion.height/2
    scorpion.set_sequence_time(0, 19, 50, True)
    return scorpion

def scorpionmovimento(scorpion,janela):
    if scorpion.x >= 0:
        if scorpion.x < janela.height :
            scorpion.x += 1.1