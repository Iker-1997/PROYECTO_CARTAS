from lucha import *


def liga(mazo_aliado, jornada=0, jugador2=aleatorio(baraja), jugador3=aleatorio(baraja), jugador4=aleatorio(baraja),
         jugador5=aleatorio(baraja), jugador6=aleatorio(baraja), puntos_aliado=0, puntos_jugador2=0, puntos_jugador3=0,
         puntos_jugador4=0, puntos_jugador5=0, puntos_jugador6=0):
        # Asignamos mazos aleatorios a cada jugador y 0 puntos a cada uno.
    while jornada < 5:
        # Bucle que enfrentará a todos los jugadores hasta la jornada 5. Se sumarán 20 puntos a los que vayan ganando.
        if jornada == 0:
            resultado1 = lucha_liga(mazo_aliado, jugador2)
            if resultado1[0] > resultado1[1]:
                puntos_aliado += 20
            else:
                puntos_jugador2 += 20
            resultado2 = lucha_liga(jugador3, jugador4)
            if resultado2[0] > resultado2[1]:
                puntos_jugador3 += 20
            else:
                puntos_jugador4 += 20
            resultado3 = lucha_liga(jugador5, jugador6)
            if resultado3[0] > resultado3[1]:
                puntos_jugador5 += 20
            else:
                puntos_jugador6 += 20
        elif jornada == 1:
            resultado1 = lucha_liga(jugador6, jugador3)
            if resultado1[0] > resultado1[1]:
                puntos_jugador6 += 20
            else:
                puntos_jugador3 += 20
            resultado2 = lucha_liga(jugador2, jugador5)
            if resultado2[0] > resultado2[1]:
                puntos_jugador2 += 20
            else:
                puntos_jugador5 += 20
            resultado3 = lucha_liga(jugador4, mazo_aliado)
            if resultado3[0] > resultado3[1]:
                puntos_jugador4 += 20
            else:
                puntos_aliado += 20
        elif jornada == 2:
            resultado1 = lucha_liga(mazo_aliado, jugador6)
            if resultado1[0] > resultado1[1]:
                puntos_aliado += 20
            else:
                puntos_jugador6 += 20
            resultado2 = lucha_liga(jugador3, jugador5)
            if resultado2[0] > resultado2[1]:
                puntos_jugador3 += 20
            else:
                puntos_jugador5 += 20
            resultado3 = lucha_liga(jugador4, jugador2)
            if resultado3[0] > resultado3[1]:
                puntos_jugador4 += 20
            else:
                puntos_jugador2 += 20
        elif jornada == 3:
            resultado1 = lucha_liga(jugador6, jugador4)
            if resultado1[0] > resultado1[1]:
                puntos_jugador6 += 20
            else:
                puntos_jugador4 += 20
            resultado2 = lucha_liga(jugador3, jugador2)
            if resultado2[0] > resultado2[1]:
                puntos_jugador3 += 20
            else:
                puntos_jugador2 += 20
            resultado3 = lucha_liga(jugador5, mazo_aliado)
            if resultado3[0] > resultado3[1]:
                puntos_jugador5 += 20
            else:
                puntos_aliado += 20
        else:
            resultado1 = lucha_liga(mazo_aliado, jugador3)
            if resultado1[0] > resultado1[1]:
                puntos_aliado += 20
            else:
                puntos_jugador3 += 20
            resultado2 = lucha_liga(jugador5, jugador4)
            if resultado2[0] > resultado2[1]:
                puntos_jugador5 += 20
            else:
                puntos_jugador4 += 20
            resultado3 = lucha_liga(jugador2, jugador6)
            if resultado3[0] > resultado3[1]:
                puntos_jugador2 += 20
            else:
                puntos_jugador6 += 20
        print("Jornada: ", jornada + 1)
        print("\nAliado: ", puntos_aliado, "\nJugador 2: ", puntos_jugador2, "\nJugador 3: ", puntos_jugador3,
              "\nJugador 4: ", puntos_jugador4, "\nJugador 5: ", puntos_jugador5, "\nJugador 6: ", puntos_jugador6,
              "\n")
        jornada += 1
