from lucha import *
from inn_tur import *
from mazos.mazos import *
from gestion_partidas import *


def menu_partida():
    print("\n", "\n")
    print("MENU DE PARTIDA", "\n1) Seguir jugando", "\n2) Guardar y finalizar.", "\n0) Finalizar")


def partida(mazo_aliado, mazo_enemigo, tipo, defecto_aliado=10, defecto_enemigo=10,):
    opcio = 1
    momento_partida = 0
    vida_aliado = defecto_aliado
    vida_enemigo = defecto_enemigo
    bucle_menu = False
    while not bucle_menu:
        valido = 1
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")

        while opcio < 0 or opcio > 2:

            print("TECLEA UN NUMERO ENTERO VALIDO.")
            menu_partida()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("NO VALIDO.")
        while 0 <= opcio <= 2:
            # Una vegada ha entrat al bucle, tenim les condicions per a cada opcio
            if opcio == 1:
                resultado = lucha(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo)
                vida_aliado = resultado[0]
                vida_enemigo = resultado[1]
                momento_partida += 1
                if vida_enemigo <= 0 or vida_aliado <= 0:
                    print("Partida acabada")
                    bucle_menu = True
                    break
            elif opcio == 2:
                print("Partida guardada")
                if tipo == "arcade":
                    partida_guardada_arcade(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo)
                    existe_arcade_guardada = True
                    return existe_arcade_guardada
                else:
                    partida_guardada_jugadores(mazo_aliado, mazo_enemigo, vida_aliado, vida_enemigo)
                    existe_jugadores_guardada = True
                    return existe_jugadores_guardada
                bucle_menu = True
                break
            else:
                bucle_menu = True
                break
            menu_partida()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("TECLEA UN NUMERO ENTERO VALIDO.")
            while opcio < 0 or opcio > 2:
                menu_partida()
                valido = 0
                while valido == 0:
                    try:
                        opcio = int(input("Que opcion quieres escoger?:\n"))
                        valido = 1
                    except ValueError:
                        print("TECLEA UN NUMERO ENTERO VALIDO.")
