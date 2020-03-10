from PROYECTO_CARTAS.inn_tur import *
from PROYECTO_CARTAS.mazos.mazos import *




def lucha(mazo_aliado, mazo_enemigo, turno):
    vida_aliado = 10
    vida_enemigo = 10
    aliado = invocar(mazo_aliado)
    enemigo = invocar(mazo_enemigo)
    if turno == 0:
        print("Ataca primero aliado", turno)
        if len(aliado) <= len(enemigo):
            for i in range(0, len(aliado)):
                res = int(aliado[i]["attack"]) - int(enemigo[i]["defense"])
                if res > 0:
                    vida_enemigo = vida_enemigo - res
        else:
            for i in range(0, len(enemigo)):
                res = int(aliado[i]["attack"]) - int(enemigo[i]["defense"])
                if res > 0:
                    vida_enemigo = vida_enemigo - res
            for j in range(len(enemigo), len(aliado)):
                vida_enemigo = vida_enemigo - int(aliado[j]["attack"])
    else:
        print("Ataca primero enemigo", turno)
        if len(enemigo) <= len(aliado):
            for i in range(0, len(enemigo)):
                res = int(enemigo[i]["attack"]) - int(aliado[i]["defense"])
                if res > 0:
                    vida_aliado = vida_aliado - res
        else:
            for i in range(0, len(aliado)):
                res = int(enemigo[i]["attack"]) - int(aliado[i]["defense"])
                if res > 0:
                    vida_aliado = vida_aliado - res
            for j in range(len(enemigo), len(aliado)):
                vida_enemigo = vida_enemigo - int(aliado[j]["attack"])

lucha(equilibrado(baraja), equilibrado(baraja), turno_aleatorio())