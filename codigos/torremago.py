from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
global torre
def movimentotorremago(lista_torre_mago_real,cliquemago,mouse,lista_torre_mago, torremago):
    if cliquemago:
        torre_mago2 = Sprite("imagens/magic-1.png",1)
        torremago.x, torremago.y = mouse.get_position()
        torremago.x -= torremago.width / 2
        torremago.y -= torremago.height / 2
        lista_torre_mago.append(torremago)
        if (mouse.is_button_pressed(3) and mouse.is_over_area):
            torre_mago2.x = torremago.x
            torre_mago2.y = torremago.y
            lista_torre_mago_real.append(torre_mago2)
            cliquemago = False
    return lista_torre_mago_real,cliquemago