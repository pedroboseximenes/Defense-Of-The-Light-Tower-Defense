def colisaotorredefesascorpion(lista_torre_defesa_real, lista_scorpion, listavidastorresdefesa, money, contadorscorpionmorto):
    for i in range (len(lista_torre_defesa_real)):
        for k in range(len(listavidastorresdefesa)):
            if i == k:
                for j in lista_scorpion:
                    if j.collided(lista_torre_defesa_real[i]):
                        listavidastorresdefesa[k] -= 1
                        money += 35
                        lista_scorpion.remove(j)
                        contadorscorpionmorto += 1
            if listavidastorresdefesa[k] <= 0:
                lista_torre_defesa_real.remove(lista_torre_defesa_real[i])
    return listavidastorresdefesa, money , contadorscorpionmorto

def colisaotorredefesaogro(lista_torre_defesa_real, lista_ogro, listavidastorresdefesa, money, contadorogromorto):
    for i in range (len(lista_torre_defesa_real)):
        for k in range(len(listavidastorresdefesa)):
            if i == k:
                for j in lista_ogro:
                    if j.collided(lista_torre_defesa_real[i]):
                        listavidastorresdefesa[k] -= 2
                        money += 65
                        lista_ogro.remove(j)
                        contadorogromorto += 1
            if listavidastorresdefesa[k] <= 0:
                lista_torre_defesa_real.remove(lista_torre_defesa_real[i])
    return listavidastorresdefesa, money, contadorogromorto

def colisaotorredefesabesouro(lista_torre_defesa_real, lista_besouro, listavidastorresdefesa, money, contadorbesouromorto):
    for i in range (len(lista_torre_defesa_real)):
        for k in range(len(listavidastorresdefesa)):
            if i == k:
                for j in lista_besouro:
                    if j.collided(lista_torre_defesa_real[i]):
                        listavidastorresdefesa[k] -= 2
                        money += 55
                        lista_besouro.remove(j)
                        contadorbesouromorto += 1
            if listavidastorresdefesa[k] <= 0:
                lista_torre_defesa_real.remove(lista_torre_defesa_real[i])
    return listavidastorresdefesa, money, contadorbesouromorto