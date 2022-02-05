from PPlay.animation import *
from PPlay.sprite import *
global torre
def movimentotorredefesa(lista_torre_defesa_real,cliquedefesa,mouse,lista_torre_defesa, torredefesa, listavidastorresdefesa):
    if cliquedefesa:
        torredefesa_2 = Sprite("imagens/7.png",1)
        torredefesa.x, torredefesa.y = mouse.get_position()
        torredefesa.x -= torredefesa.width / 2
        torredefesa.y -= torredefesa.height / 2
        lista_torre_defesa.append(torredefesa)
        if (mouse.is_button_pressed(3) and mouse.is_over_area):
            torredefesa_2.x = torredefesa.x
            torredefesa_2.y = torredefesa.y
            lista_torre_defesa_real.append(torredefesa_2)
            vidadefesa = 5
            listavidastorresdefesa.append(vidadefesa)
            cliquedefesa = False
    return lista_torre_defesa_real,cliquedefesa, listavidastorresdefesa