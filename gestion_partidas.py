def partida_guardada_arcade(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo):
    f = open("mazo_aliado_arcade", "w")
    g = open("mazo_enemigo_arcade", "w")
    h = open("vidas_arcade", "w")
    for carta in mazo_aliado:
        f.write(str(carta))
        f.write("\n")
    for card in mazo_enemigo:
        g.write(str(card))
        g.write("\n")
    h.write(str(vida_aliado))
    h.write(";")
    h.write(str(vida_enemigo))


def partida_guardada_jugadores(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo):
    f = open("mazo_aliado_jugadores", "w")
    g = open("mazo_enemigo_jugadores", "w")
    h = open("vidas_jugadores", "w")
    for carta in mazo_aliado:
        f.write(str(carta))
        f.write("\n")
    for card in mazo_enemigo:
        g.write(str(card))
        g.write("\n")
    h.write(str(vida_aliado))
    h.write(";")
    h.write(str(vida_enemigo))
