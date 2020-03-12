from lucha import *
from inn_tur import *
from mazos.mazos import *



def partida(defecto_aliado=10, defecto_enemigo=10):
    momento_partida = 0
    vida_aliado = defecto_aliado
    vida_enemigo = defecto_enemigo
    resultado = lucha(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo)
    print(resultado)
    vida_aliado = resultado[0]
    vida_enemigo = resultado[1]
    momento_partida += 1
    while vida_aliado > 0 and vida_enemigo > 0:
        resultado = lucha(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo)
        vida_aliado = resultado[0]
        print(vida_aliado)
        vida_enemigo = resultado[1]
        print(vida_enemigo)
        input()

mazo_aliado = equilibrado(baraja)
mazo_enemigo = equilibrado(baraja)
partida()