from PPlay.animation import *
def upgradearco1(upgradetorre, mouse, janela,listatorrereal, money, iramudararco1, upgradetorrearco):
    if (mouse.is_button_pressed(1)) and money >= 150:
        if (mouse.is_over_object(upgradetorre)):
            iramudararco1 = 1
    if iramudararco1 == 1:
        for j in range(len(upgradetorrearco)):
            if upgradetorrearco[j] == 0:
                for i in range (len(listatorrereal)):
                    if j == i:
                        if (mouse.is_button_pressed(1)):
                            if (mouse.is_over_object(listatorrereal[i])):
                                torrearcoupgrade1 = Animation("imagens/Torrelvl2.png",6)
                                torrearcoupgrade1.set_sequence_time(0,5,100,True)
                                torrearcoupgrade1.x, torrearcoupgrade1.y = listatorrereal[i].x +28 , listatorrereal[i].y +25
                                listatorrereal[i] = torrearcoupgrade1
                                money -= 150
                                upgradetorrearco[j] = 1
                                iramudararco1 = 0
    return listatorrereal, money, iramudararco1, upgradetorrearco

def upgradearco2(upgradetorre2, mouse, janela,listatorrereal, money, iramudararco2, upgradetorrearco):
    if (mouse.is_button_pressed(1)) and money >= 300:
        if (mouse.is_over_object(upgradetorre2)):
            iramudararco2 = 1
    if iramudararco2 == 1:
        for j in range (len(upgradetorrearco)):
            if upgradetorrearco[j] == 1:
                for i in range (len(listatorrereal)):
                    if j == i:
                        if (mouse.is_button_pressed(1)):
                            if (mouse.is_over_object(listatorrereal[i])):
                                torrearcoupgrade2 = Animation("imagens/Torrelvl3.png",6)
                                torrearcoupgrade2.set_sequence_time(0,5,100,True)
                                torrearcoupgrade2.x, torrearcoupgrade2.y = listatorrereal[i].x , listatorrereal[i].y
                                listatorrereal[i] = torrearcoupgrade2
                                money -= 300
                                upgradetorrearco[j] = 2
                                iramudararco2 = 0
    return listatorrereal, money, iramudararco2, upgradetorrearco

def upgrademago1(upgrademago, mouse, janela,lista_torre_mago_real, money, iramudarmago1, upgradetorremago):
    if (mouse.is_button_pressed(1)) and money >= 270:
        if (mouse.is_over_object(upgrademago)):
            iramudarmago1 = 1
    if iramudarmago1 == 1:
        for j in range(len(upgradetorremago)):
            if upgradetorremago[j] == 0:
                for i in range (len(lista_torre_mago_real)):
                    if j == i:
                        if (mouse.is_button_pressed(1)):
                            if (mouse.is_over_object(lista_torre_mago_real[i])):
                                torremagoupgrade1 = Animation("imagens/magic-2.png",1)
                                torremagoupgrade1.set_sequence_time(0,0,100,True)
                                torremagoupgrade1.x, torremagoupgrade1.y = lista_torre_mago_real[i].x, lista_torre_mago_real[i].y
                                lista_torre_mago_real[i] = torremagoupgrade1
                                money -= 150
                                upgradetorremago[j] = 1
                                iramudarmago1 = 0
    return lista_torre_mago_real, money, iramudarmago1, upgradetorremago

def upgrademago_2(upgrademago2, mouse, janela,lista_torre_mago_real, money, iramudarmago2, upgradetorremago):
    if (mouse.is_button_pressed(1)) and money >= 400:
        if (mouse.is_over_object(upgrademago2)):
            iramudarmago2 = 1
    if iramudarmago2 == 1:
        for j in range(len(upgradetorremago)):
            if upgradetorremago[j] == 1:
                for i in range (len(lista_torre_mago_real)):
                    if j == i:
                        if (mouse.is_button_pressed(1)):
                            if (mouse.is_over_object(lista_torre_mago_real[i])):
                                torremagoupgrade2 = Animation("imagens/magic-3.png",1)
                                torremagoupgrade2.set_sequence_time(0,0,100,True)
                                torremagoupgrade2.x, torremagoupgrade2.y = lista_torre_mago_real[i].x , lista_torre_mago_real[i].y
                                lista_torre_mago_real[i] = torremagoupgrade2
                                money -= 400
                                upgradetorremago[j] = 2
                                iramudarmago2 = 0
    return lista_torre_mago_real, money, iramudarmago2, upgradetorremago
