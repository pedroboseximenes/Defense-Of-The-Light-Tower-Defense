from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from torre import *
from scorpion import *
global money
def cliquenatorre(teste,tempo,mouse,clique,money):
    if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
        clique = True

    return clique
def movimentotorre(lista,mouse,tempo,clique,teste,torre):
    if clique:
        torre2 = Sprite("imagens/2.png",1)
        torre.x, torre.y = mouse.get_position()
        torre.x -= torre.width / 2
        torre.y -= torre.height / 2
        lista.append(torre)
        if (mouse.is_button_pressed(3)):
            torre2.x = torre.x
            torre2.y = torre.y
            lista.append(torre2)
            lista.remove(torre)
            clique = False
    return clique



def game(janela):
    fundo = GameImage("imagens/FUNDO AREIA COMPLETO.jpg")
    janela.set_title("Defense of the Light")

    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
    global lista
    lista = []
    tempo = 0
    """
    dinheiro:
    """
    money = 100

    teste = GameImage("imagens/ico_8.png")
    teste.x = 50
    teste.y = 10
    global clique
    clique = False
    #global torre
    #torre = Sprite("imagens/2.png",1)
    torre = Sprite("imagens/2.png",1)

    scorpion = scorpionanimation(janela)

    while True:
        tempo += janela.delta_time()
        # mecanicas:
        if (teclado.key_pressed("ESC")):
            break
        if (mouse.is_over_object(teste) and mouse.is_button_pressed(
                1) and tempo >= 0.75 and clique == False and money >= 100):
            clique = True
            money -= 100

        #clique = cliquenatorre(teste,tempo,mouse,clique,money)
        clique = movimentotorre(lista, mouse, tempo, clique, teste,torre)

        scorpionmovimento(scorpion,janela)

        # desenhos:
        fundo.draw()
        for i in lista:
            i.draw()
        scorpion.draw()
        janela.draw_text(str(money), janela.width/2, 10, 27, (255, 0, 0), "Boulder", False, False)
        scorpion.update()
        teste.draw()
        janela.update()