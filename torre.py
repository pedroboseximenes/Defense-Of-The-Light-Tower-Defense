from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
global torre
def movimentotorre(listatorre,mouse,tempo,clique,teste,torre,listatorrereal):
    if clique:
        torre2 = Animation("imagens/torrefeita.png",6)
        torre2.set_sequence_time(0, 6, 1000, True)
        torre.x, torre.y = mouse.get_position()
        torre.x -= torre.width / 2
        torre.y -= torre.height / 2
        listatorre.append(torre)
        if (mouse.is_button_pressed(3) and mouse.is_over_area):
            torre2.x = torre.x
            torre2.y = torre.y
            listatorrereal.append(torre2)
            clique = False
    return listatorrereal,clique