def colisaotorredefesascorpion(lista_torre_defesa_real, lista_scorpion, listavidastorresdefesa, money):
    for i in range (len(lista_torre_defesa_real)):
        for k in range(len(listavidastorresdefesa)):
            if i == k:
                for j in lista_scorpion:
                    if j.collided(lista_torre_defesa_real[i]):
                        listavidastorresdefesa[k] -= 1
                        money += 35
                        lista_scorpion.remove(j)
            if listavidastorresdefesa[k] <= 0:
                lista_torre_defesa_real.remove(lista_torre_defesa_real[i])
    return listavidastorresdefesa, money

def colisaotorredefesaogro(lista_torre_defesa_real, lista_ogro, listavidastorresdefesa, money):
    for i in range (len(lista_torre_defesa_real)):
        for k in range(len(listavidastorresdefesa)):
            if i == k:
                for j in lista_ogro:
                    if j.collided(lista_torre_defesa_real[i]):
                        listavidastorresdefesa[k] -= 2
                        money += 65
                        lista_ogro.remove(j)
            if listavidastorresdefesa[k] <= 0:
                lista_torre_defesa_real.remove(lista_torre_defesa_real[i])
    return listavidastorresdefesa, money

def colisaotorredefesabesouro(lista_torre_defesa_real, lista_besouro, listavidastorresdefesa, money):
    for i in range (len(lista_torre_defesa_real)):
        for k in range(len(listavidastorresdefesa)):
            if i == k:
                for j in lista_besouro:
                    if j.collided(lista_torre_defesa_real[i]):
                        listavidastorresdefesa[k] -= 2
                        money += 55
                        lista_besouro.remove(j)
            if listavidastorresdefesa[k] <= 0:
                lista_torre_defesa_real.remove(lista_torre_defesa_real[i])
    return listavidastorresdefesa, money