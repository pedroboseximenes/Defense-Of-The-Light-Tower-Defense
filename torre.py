from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
global torre
def movimentotorre(lista,mouse,tempo,clique,teste,torre,scorpion):
    if clique:
        torre2 = Sprite("imagens/torrefeita.png",1)
        torre.x, torre.y = mouse.get_position()
        torre.x -= torre.width / 2
        torre.y -= torre.height / 2

        if (mouse.is_button_pressed(3)):
            torre2.x = torre.x
            torre2.y = torre.y
            lista.append(torre2)
            lista.remove(torre)
            print(lista)
            clique = False
        lista.append(torre)
    return clique
