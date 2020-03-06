from mazos.mazos import equilibrado
import xml.etree.ElementTree as ET
import random


def invocar(mazo):
    mazo_invocar = mazo
    puntos_inv = 5
    x = 0
    invocacion = []

    while puntos_inv > 0:
        if len(mazo_invocar) > 1:
            y = random.randrange(0, len(mazo_invocar) - 1)
            carta = mazo_invocar[y]
            del mazo_invocar[y]
            if int(carta["summonPoints"]) <= puntos_inv:
                invocacion.append(carta)
                puntos_inv = puntos_inv - int(invocacion[x]["summonPoints"])
                x += 1
        elif len(mazo_invocar) == 1:
            carta = mazo_invocar[0]
            del mazo_invocar[0]
            if int(carta["summonPoints"]) <= puntos_inv:
                invocacion.append(carta)
                puntos_inv = puntos_inv - int(invocacion[x]["summonPoints"])
                x += 1
        else:
            break
    return invocacion


baraja = ET.parse("myBaraja.xml")
mazo = equilibrado(baraja)
aliado = invocar(mazo)
enemigo = invocar(mazo)
print(aliado)
print(enemigo)
