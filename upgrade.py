from PPlay.animation import *
def upgradearco1(upgradetorre, mouse, janela,listatorrereal, money, iramudar, upgradetorrearco):
    if (mouse.is_button_pressed(1)) and money >= 150:
        if (mouse.is_over_object(upgradetorre)):
            iramudar = 1
    if iramudar == 1:
        if upgradetorrearco == 0:
            for i in range (len(listatorrereal)):
                if (mouse.is_button_pressed(1)):
                    if (mouse.is_over_object(listatorrereal[i])):
                        print("chegou aqui")
                        torrearcoupgrade1 = Animation("imagens/Torrelvl2.png",6)
                        torrearcoupgrade1.set_sequence_time(0,5,100,True)
                        torrearcoupgrade1.x, torrearcoupgrade1.y = listatorrereal[i].x , listatorrereal[i].y
                        listatorrereal[i] = torrearcoupgrade1
                        money -= 150
                        upgradetorrearco = 1
                        iramudar = 0
    return listatorrereal, money, iramudar, upgradetorrearco

def upgradearco2(upgradetorre2, mouse, janela,listatorrereal, money, iramudar, upgradetorrearco):
    if (mouse.is_button_pressed(1)) and money >= 300:
        if (mouse.is_over_object(upgradetorre2)):
            iramudar = 1
    if iramudar == 1:
        if upgradetorrearco == 1:
            for i in range (len(listatorrereal)):
                if (mouse.is_button_pressed(1)):
                    if (mouse.is_over_object(listatorrereal[i])):
                        torrearcoupgrade2 = Animation("imagens/Torrelvl3.png",6)
                        torrearcoupgrade2.set_sequence_time(0,5,100,True)
                        torrearcoupgrade2.x, torrearcoupgrade2.y = listatorrereal[i].x , listatorrereal[i].y
                        listatorrereal[i] = torrearcoupgrade2
                        money -= 300
                        upgradetorrearco = 2
                        iramudar = 0
    return listatorrereal, money, iramudar, upgradetorrearco

def upgrademago1(upgrademago, mouse, janela,lista_torre_mago_real, money, iramudarmago, upgradetorremago):
    if (mouse.is_button_pressed(1)) and money >= 270:
        if (mouse.is_over_object(upgrademago)):
            iramudarmago = 1
    if iramudarmago == 1:
        if upgradetorremago == 0:
            for i in range (len(lista_torre_mago_real)):
                if (mouse.is_button_pressed(1)):
                    if (mouse.is_over_object(lista_torre_mago_real[i])):
                        torremagoupgrade1 = Animation("imagens/magic-2.png",1)
                        torremagoupgrade1.set_sequence_time(0,0,100,True)
                        torremagoupgrade1.x, torremagoupgrade1.y = lista_torre_mago_real[i].x , lista_torre_mago_real[i].y
                        lista_torre_mago_real[i] = torremagoupgrade1
                        money -= 150
                        upgradetorremago = 1
                        iramudarmago = 0
    return lista_torre_mago_real, money, iramudarmago, upgradetorremago

def upgrademago_2(upgrademago2, mouse, janela,lista_torre_mago_real, money, iramudarmago, upgradetorremago):
    if (mouse.is_button_pressed(1)) and money >= 400:
        if (mouse.is_over_object(upgrademago2)):
            iramudarmago = 1
    if iramudarmago == 1:
        if upgradetorremago == 1:
            for i in range (len(lista_torre_mago_real)):
                if (mouse.is_button_pressed(1)):
                    if (mouse.is_over_object(lista_torre_mago_real[i])):
                        torremagoupgrade2 = Animation("imagens/magic-3.png",1)
                        torremagoupgrade2.set_sequence_time(0,0,100,True)
                        torremagoupgrade2.x, torremagoupgrade2.y = lista_torre_mago_real[i].x , lista_torre_mago_real[i].y
                        lista_torre_mago_real[i] = torremagoupgrade2
                        money -= 400
                        upgradetorremago = 2
                        iramudarmago = 0
    return lista_torre_mago_real, money, iramudarmago, upgradetorremago
