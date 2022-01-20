from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.collision import *
from torre import *
from scorpion import *
from tiro import *
global money
def cliquenatorre(teste,tempo,mouse,clique,money):
    if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
        clique = True

    return clique



def game(janela):
    fundo = GameImage("imagens/FUNDO AREIA COMPLETO.jpg")
    janela.set_title("Defense of the Light")

    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()
    lista = []
    tempo = 0
    """
    dinheiro:
    """
    money = 200

    teste = GameImage("imagens/ico_8.png")
    teste.x, teste.y = [50,10]
    coracao = GameImage("imagens/heart.png")
    coracao.x,coracao.y = [500,10]
    clique = False
    torre = Sprite("imagens/torrefeita.png",1)
    tiroarco = Sprite("imagens/arqueiro tower/37.png", 1)
    listatiro = []
    vida_scorpion = 100

    scorpion = scorpionanimation(janela)
    time = 0

    while True:
        tempo += janela.delta_time()
        # mecanicas:
        if (teclado.key_pressed("ESC")):
            break
        """
        vendo se ta sendo click e se te money
        """
        if (mouse.is_over_object(teste) and mouse.is_button_pressed(1) and tempo >= 0.75 and clique == False and money >= 100):
            clique = True
            money -= 100
        ""
        clique = movimentotorre(lista, mouse, tempo, clique, teste,torre,scorpion)
        scorpionmovimento(scorpion,janela)
        listatiro, time = tirotorre(torre, scorpion, lista, listatiro, vida_scorpion, janela, time,tiroarco)
        # desenhos:
        fundo.draw()
        for i in lista:
            i.draw()
        for j in listatiro:
            j.draw()
        scorpion.draw()
        janela.draw_text(str(money), janela.width/2, 10, 27, (255, 0, 0), "Boulder", False, False)
        teste.draw()
        scorpion.update()
        janela.update()