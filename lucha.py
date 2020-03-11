from PROYECTO_CARTAS.inn_tur import *
from PROYECTO_CARTAS.mazos.mazos import *


def lucha(mazo_aliado, mazo_enemigo, turno, defecto_aliado=10, defecto_enemigo=10):
    vida_aliado = defecto_aliado
    vida_enemigo =defecto_enemigo
    aliado = invocar(mazo_aliado)
    enemigo = invocar(mazo_enemigo)
    print(aliado)
    print(enemigo)
    mano_aliada = aliado
    mano_enemiga = enemigo
    turnos = 0
    if turno == 0:
        print("Ataca primero aliado", turno)
    else:
        print("Ataca primero enemigo", turno)
    while turnos < 3 and len(mano_enemiga) > 0 and len(mano_aliada) > 0:
        if turno == 0:
            if len(mano_aliada) <= len(mano_enemiga):
                for i in range(0, len(mano_aliada)):
                    res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                    if res > 0:
                        del mano_enemiga[i]
                        vida_enemigo = vida_enemigo - res
            else:
                for i in range(0, len(mano_enemiga)):
                    res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                    if res > 0:
                        del mano_enemiga[i]
                        vida_enemigo = vida_enemigo - res
                for j in range(len(mano_enemiga), len(mano_aliada)):
                    vida_enemigo = vida_enemigo - int(mano_aliada[j]["attack"])
            if len(mano_enemiga) == 0:
                break
            else:
                if len(mano_enemiga) <= len(mano_aliada):
                    for i in range(0, len(mano_enemiga)):
                        res = int(mano_enemiga[i]["attack"]) - int(mano_aliada[i]["defense"])
                        if res > 0:
                            del mano_aliada[i]
                            vida_aliado = vida_aliado - res
                else:
                    for i in range(0, len(mano_aliada)):
                        res = int(mano_enemiga[i]["attack"]) - int(mano_aliada[i]["defense"])
                        if res > 0:
                            del mano_aliada[i]
                            vida_aliado = vida_aliado - res
                    for j in range(len(mano_aliada), len(mano_enemiga)):
                        vida_aliado = vida_aliado - int(mano_enemiga[j]["attack"])
        else:
            if len(mano_enemiga) <= len(mano_aliada):
                for i in range(0, len(mano_enemiga)):
                    res = int(mano_enemiga[i]["attack"]) - int(mano_aliada[i]["defense"])
                    if res > 0:
                        del mano_aliada[i]
                        vida_aliado = vida_aliado - res
            else:
                for i in range(0, len(mano_aliada)):
                    res = int(mano_enemiga[i]["attack"]) - int(mano_aliada[i]["defense"])
                    if res > 0:
                        del mano_aliada[i]
                        vida_aliado = vida_aliado - res
                for j in range(len(mano_aliada), len(mano_enemiga)):
                    vida_aliado = vida_aliado - int(mano_enemiga[j]["attack"])
            if len(mano_aliada) == 0:
                break
            else:
                if len(mano_aliada) <= len(mano_enemiga):
                    for i in range(0, len(mano_aliada)):
                        res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                        if res > 0:
                            del mano_enemiga[i]
                            vida_enemigo = vida_enemigo - res
                else:
                    for i in range(0, len(mano_enemiga)):
                        res = int(mano_aliada[i]["attack"]) - int(mano_enemiga[i]["defense"])
                        if res > 0:
                            del mano_enemiga[i]
                            vida_enemigo = vida_enemigo - res
                    for j in range(len(mano_enemiga), len(mano_aliada)):
                        vida_enemigo = vida_enemigo - int(mano_aliada[j]["attack"])
        turnos += 1
        print("Se ha/han pasado", turnos, "turno/s.")
    print("Mano aliada", mano_aliada)
    print("Mano enemiga", mano_enemiga)
    print("Vida enemigo: ", vida_enemigo)
    print("Vida aliado: ", vida_aliado)


lucha(equilibrado(baraja), equilibrado(baraja), turno_aleatorio())
