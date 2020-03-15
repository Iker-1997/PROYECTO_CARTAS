import json


def partida_guardada_arcade(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo):
    f = open("mazo_aliado_arcade", "w")
    g = open("mazo_enemigo_arcade", "w")
    h = open("vidas_arcade", "w")
    json.dump(mazo_aliado, f)
    json.dump(mazo_enemigo, g)
    h.write(str(vida_aliado))
    h.write(";")
    h.write(str(vida_enemigo))
    f.close()
    g.close()
    h.close()


def partida_guardada_jugadores(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo):
    f = open("mazo_aliado_jugadores", "w")
    g = open("mazo_enemigo_jugadores", "w")
    h = open("vidas_jugadores", "w")
    json.dump(mazo_aliado, f)
    json.dump(mazo_enemigo, g)
    h.write(str(vida_aliado))
    h.write(";")
    h.write(str(vida_enemigo))
    f.close()
    g.close()
    h.close()


def cargar_partida(archivo_aliado, archivo_enemigo, archivo_vidas):
    f = open(archivo_aliado, "r")
    mazo_aliado = json.load(f)
    g = open(archivo_enemigo, "r")
    mazo_enemigo = json.load(g)
    h = open(archivo_vidas, "r")
    vidas = h.read().split(";")
    vida_aliado = vidas[0]
    vida_enemigo = vidas[1].rstrip("\n")
    f.close()
    g.close()
    h.close()
    return mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo