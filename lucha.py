from inn_tur import *
from mazos.mazos import *


def lucha(mazo_aliado_fijo, mazo_enemigo_fijo, vida_aliado, vida_enemigo):
    turno = turno_aleatorio()
    mazito_a = mazo_aliado_fijo.copy()
    mazito_e = mazo_enemigo_fijo.copy()
    aliado = invocar(mazito_a)
    enemigo = invocar(mazito_e)
    print("Cartas invocadas")
    print("Aliado", aliado)
    print("Enemigo", enemigo)
    mano_aliada = aliado.copy()
    mano_enemiga = enemigo.copy()
    turnos = 0
    if turno == 0:
        print("\nAtaca primero el aliado")
    else:
        print("\nAtaca primero el enemigo")
    while turnos < 3 and len(mano_enemiga) > 0 and len(mano_aliada) > 0:
        if vida_aliado < 0 or vida_enemigo < 0:
            break
        turnos += 1
        print("\nSe ha/han pasado", turnos, "turno/s.")
        if turno == 0:
            if len(mano_aliada) > len(mano_enemiga):
                if len(mano_enemiga) == 1:
                    if mano_aliada[0]["type"] == "infantry" and mano_enemiga[0]["type"] == "lancer" \
                            or mano_aliada[0]["type"] == "lancer" and mano_enemiga[0]["type"] == "chivalry" \
                            or mano_aliada[0]["type"] == "chivalry" and mano_enemiga[0]["type"] == "infantry":
                        print("Multiplicador")
                        res = (int(mano_aliada[0]["attack"])*2) - int(mano_enemiga[0]["defense"])
                    else:
                        res = int(mano_aliada[0]["attack"]) - int(mano_enemiga[0]["defense"])
                    if res > 0:
                        del mano_enemiga[0]
                        vida_enemigo = vida_enemigo - res
                    for j in range(len(mano_aliada)-1, 0, -1):
                        vida_enemigo = vida_enemigo - int(mano_aliada[j]["attack"])
                else:
                    for i in range(0, len(mano_enemiga)):
                        if mano_aliada[i]["type"] == "infantry" and mano_enemiga[i]["type"] == "lancer" \
                                or mano_aliada[i]["type"] == "lancer" and mano_enemiga[i]["type"] == "chivalry" \
                                or mano_aliada[i]["type"] == "chivalry" and mano_enemiga[i]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_aliada[i]["attack"]) * 2) - int(mano_enemiga[i]["defense"])
                        else:
                            res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                        if res > 0:
                            del mano_enemiga[i]
                            vida_enemigo = vida_enemigo - res
                    for j in range(len(mano_aliada)-1, len(mano_enemiga)-1, -1):
                        vida_enemigo = vida_enemigo - int(mano_aliada[j]["attack"])
            else:
                if len(mano_aliada) == 1 and len(mano_enemiga) == 1:
                    if mano_aliada[0]["type"] == "infantry" and mano_enemiga[0]["type"] == "lancer" \
                            or mano_aliada[0]["type"] == "lancer" and mano_enemiga[0]["type"] == "chivalry" \
                            or mano_aliada[0]["type"] == "chivalry" and mano_enemiga[0]["type"] == "infantry":
                        print("Multiplicador")
                        res = (int(mano_aliada[0]["attack"]) * 2) - int(mano_enemiga[0]["defense"])
                    else:
                        res = int(mano_aliada[0]["attack"]) - int(mano_enemiga[0]["defense"])
                    if res > 0:
                        del mano_enemiga[0]
                        vida_enemigo = vida_enemigo - res
                else:
                    for i in range(len(mano_aliada)-1, -1, -1):
                        if mano_aliada[i]["type"] == "infantry" and mano_enemiga[i]["type"] == "lancer" \
                                or mano_aliada[i]["type"] == "lancer" and mano_enemiga[i]["type"] == "chivalry" \
                                or mano_aliada[i]["type"] == "chivalry" and mano_enemiga[i]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_aliada[i]["attack"]) * 2) - int(mano_enemiga[i]["defense"])
                        else:
                            res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                        if res > 0:
                            del mano_enemiga[i]
                            vida_enemigo = vida_enemigo - res
            if len(mano_enemiga) == 0:
                break
            else:
                if len(mano_enemiga) <= len(mano_aliada):
                    if len(mano_enemiga) == 1 and len(mano_aliada) == 1:
                        if mano_enemiga[0]["type"] == "infantry" and mano_aliada[0]["type"] == "lancer" \
                                or mano_enemiga[0]["type"] == "lancer" and mano_aliada[0]["type"] == "chivalry" \
                                or mano_enemiga[0]["type"] == "chivalry" and mano_aliada[0]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_enemiga[0]["attack"])*2) - int(mano_aliada[0]["defense"])
                        else:
                            res = int(mano_enemiga[0]["attack"]) - int(mano_aliada[0]["defense"])
                        if res > 0:
                            del mano_aliada[0]
                            vida_aliado = vida_aliado - res
                    else:
                        for i in range(len(mano_enemiga)-1, -1, -1):
                            if mano_enemiga[i]["type"] == "infantry" and mano_aliada[i]["type"] == "lancer" \
                                    or mano_enemiga[i]["type"] == "lancer" and mano_aliada[i]["type"] == "chivalry" \
                                    or mano_enemiga[i]["type"] == "chivalry" and mano_aliada[i]["type"] == "infantry":
                                print("Multiplicador")
                                res = (int(mano_enemiga[i]["attack"]) * 2) - int(mano_aliada[i]["defense"])
                            else:
                                res = int(mano_enemiga[i]["attack"]) - int(mano_aliada[i]["defense"])
                            if res > 0:
                                del mano_aliada[i]
                                vida_aliado = vida_aliado - res
                else:
                    if len(mano_aliada) == 1:
                        if mano_enemiga[0]["type"] == "infantry" and mano_aliada[0]["type"] == "lancer" \
                                or mano_enemiga[0]["type"] == "lancer" and mano_aliada[0]["type"] == "chivalry" \
                                or mano_enemiga[0]["type"] == "chivalry" and mano_aliada[0]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_enemiga[0]["attack"]) * 2) - int(mano_aliada[0]["defense"])
                        else:
                            res = int(mano_enemiga[0]["attack"]) - int(mano_aliada[0]["defense"])
                        if res > 0:
                            del mano_aliada[0]
                            vida_aliado = vida_aliado - res
                        for j in range(len(mano_enemiga)-1, 0, -1):
                            vida_aliado = vida_aliado - int(mano_enemiga[j]["attack"])
                    else:
                        for i in range(0, len(mano_aliada)):
                            if mano_enemiga[i]["type"] == "infantry" and mano_aliada[i]["type"] == "lancer" \
                                    or mano_enemiga[i]["type"] == "lancer" and mano_aliada[i]["type"] == "chivalry" \
                                    or mano_enemiga[i]["type"] == "chivalry" and mano_aliada[i]["type"] == "infantry":
                                print("Multiplicador")
                                res = (int(mano_enemiga[i]["attack"]) * 2) - int(mano_aliada[i]["defense"])
                            else:
                                res = int(mano_enemiga[i]["attack"]) - int(mano_aliada[i]["defense"])
                            if res > 0:
                                del mano_aliada[i]
                                vida_aliado = vida_aliado - res
                        for j in range(len(mano_enemiga)-1, len(mano_aliada)-1, -1):
                            vida_aliado = vida_aliado - int(mano_enemiga[j]["attack"])
        else:
            if len(mano_enemiga) > len(mano_aliada):
                if len(mano_aliada) == 1:
                    if mano_enemiga[0]["type"] == "infantry" and mano_aliada[0]["type"] == "lancer" \
                            or mano_enemiga[0]["type"] == "lancer" and mano_aliada[0]["type"] == "chivalry" \
                            or mano_enemiga[0]["type"] == "chivalry" and mano_aliada[0]["type"] == "infantry":
                        print("Multiplicador")
                        res = (int(mano_enemiga[0]["attack"]) * 2) - int(mano_aliada[0]["defense"])
                    else:
                        res = int(mano_enemiga[0]["attack"]) - int(mano_aliada[0]["defense"])
                    if res > 0:
                        del mano_aliada[0]
                        vida_aliado = vida_aliado - res
                    for j in range(len(mano_enemiga)-1, 0, -1):
                        vida_aliado = vida_aliado - int(mano_enemiga[j]["attack"])
                else:
                    for i in range(len(mano_aliada)-1, -1, -1):
                        if mano_aliada[i]["type"] == "infantry" and mano_enemiga[i]["type"] == "lancer" \
                                or mano_aliada[i]["type"] == "lancer" and mano_enemiga[i]["type"] == "chivalry" \
                                or mano_aliada[i]["type"] == "chivalry" and mano_enemiga[i]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_aliada[i]["attack"]) * 2) - int(mano_enemiga[i]["defense"])
                        else:
                            res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                        if res > 0:
                            del mano_aliada[i]
                            vida_aliado = vida_aliado - res
                    for j in range(len(mano_enemiga)-1, len(mano_aliada)-1, -1):
                        vida_aliado = vida_aliado - int(mano_enemiga[j]["attack"])
            else:
                if len(mano_enemiga) == 1 and len(mano_aliada) == 1:
                    if mano_enemiga[0]["type"] == "infantry" and mano_aliada[0]["type"] == "lancer" \
                            or mano_enemiga[0]["type"] == "lancer" and mano_aliada[0]["type"] == "chivalry" \
                            or mano_enemiga[0]["type"] == "chivalry" and mano_aliada[0]["type"] == "infantry":
                        print("Multiplicador")
                        res = (int(mano_enemiga[0]["attack"]) * 2) - int(mano_aliada[0]["defense"])
                    else:
                        res = int(mano_enemiga[0]["attack"]) - int(mano_aliada[0]["defense"])
                    if res > 0:
                        del mano_aliada[0]
                        vida_aliado = vida_aliado - res
                else:
                    for i in range(len(mano_enemiga)-1, -1, -1):
                        if mano_enemiga[i]["type"] == "infantry" and mano_aliada[i]["type"] == "lancer" \
                                or mano_enemiga[i]["type"] == "lancer" and mano_aliada[i]["type"] == "chivalry" \
                                or mano_enemiga[i]["type"] == "chivalry" and mano_aliada[i]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_enemiga[i]["attack"]) * 2) - int(mano_aliada[i]["defense"])
                        else:
                            res = int(mano_enemiga[i]["attack"]) - int(mano_aliada[i]["defense"])
                        if res > 0:
                            del mano_aliada[i]
                            vida_aliado = vida_aliado - res
            if len(mano_aliada) == 0:
                break
            else:
                if len(mano_aliada) <= len(mano_enemiga):
                    if len(mano_aliada) == 1 and len(mano_enemiga) == 1:
                        if mano_aliada[0]["type"] == "infantry" and mano_enemiga[0]["type"] == "lancer" \
                                or mano_aliada[0]["type"] == "lancer" and mano_enemiga[0]["type"] == "chivalry" \
                                or mano_aliada[0]["type"] == "chivalry" and mano_enemiga[0]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_aliada[0]["attack"]) * 2) - int(mano_enemiga[0]["defense"])
                        else:
                            res = int(mano_aliada[0]["attack"]) - int(mano_enemiga[0]["defense"])
                        if res > 0:
                            del mano_enemiga[0]
                            vida_enemigo = vida_enemigo - res
                    else:
                        for i in range(len(mano_aliada)-1, -1, -1):
                            if mano_aliada[i]["type"] == "infantry" and mano_enemiga[i]["type"] == "lancer" \
                                    or mano_aliada[i]["type"] == "lancer" and mano_enemiga[i]["type"] == "chivalry" \
                                    or mano_aliada[i]["type"] == "chivalry" and mano_enemiga[i]["type"] == "infantry":
                                print("Multiplicador")
                                res = (int(mano_aliada[i]["attack"]) * 2) - int(mano_enemiga[i]["defense"])
                            else:
                                res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                            if res > 0:
                                del mano_enemiga[i]
                                vida_enemigo = vida_enemigo - res
                else:
                    if len(mano_enemiga) == 1:
                        if mano_aliada[0]["type"] == "infantry" and mano_enemiga[0]["type"] == "lancer" \
                                or mano_aliada[0]["type"] == "lancer" and mano_enemiga[0]["type"] == "chivalry" \
                                or mano_aliada[0]["type"] == "chivalry" and mano_enemiga[0]["type"] == "infantry":
                            print("Multiplicador")
                            res = (int(mano_aliada[0]["attack"]) * 2) - int(mano_enemiga[0]["defense"])
                        else:
                            res = int(mano_aliada[0]["attack"]) - int(mano_enemiga[0]["defense"])
                        if res > 0:
                            del mano_enemiga[0]
                            vida_enemigo = vida_enemigo - res
                        for j in range(len(mano_aliada)-1, -1, -1):
                            vida_enemigo = vida_enemigo - int(mano_aliada[j]["attack"])
                    else:
                        for i in range(len(mano_enemiga)-1, -1, -1):
                            if mano_aliada[i]["type"] == "infantry" and mano_enemiga[i]["type"] == "lancer" \
                                    or mano_aliada[i]["type"] == "lancer" and mano_enemiga[i]["type"] == "chivalry" \
                                    or mano_aliada[i]["type"] == "chivalry" and mano_enemiga[i]["type"] == "infantry":
                                print("Multiplicador")
                                res = (int(mano_aliada[i]["attack"]) * 2) - int(mano_enemiga[i]["defense"])
                            else:
                                res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                            if res > 0:
                                del mano_enemiga[i]
                                vida_enemigo = vida_enemigo - res
                        for j in range(len(mano_aliada)-1, len(mano_enemiga)-1, -1):
                            vida_enemigo = vida_enemigo - int(mano_aliada[j]["attack"])
    print("\n", "Mano aliada", mano_aliada)
    print("\n", "Vida aliado: ", vida_aliado)
    print("\n", "Mano enemiga", mano_enemiga)
    print("\n", "Vida enemigo: ", vida_enemigo)

    return[vida_aliado, vida_enemigo]

