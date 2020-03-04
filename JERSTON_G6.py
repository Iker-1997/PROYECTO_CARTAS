import xml.etree.ElementTree as ET
from PROYECTO_CARTAS.mazos.mazos import aleatorio
from PROYECTO_CARTAS.mazos.mazos import ataque
from PROYECTO_CARTAS.mazos.mazos import defensa
from PROYECTO_CARTAS.mazos.mazos import equilibrado


def menu_inicial():
    # Creamos el menu para utilizarlo despues.
    print("MENU INICIAL","\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n0) Finalizar",
          "\n¡ALERTA! El juego no continuara hasta cargar la baraja propia.")


def menu_mazo_individual():
    # Creamos el menu para utilizarlo despues.
    print("MENU MAZO", "\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n3) Crear mazo aleatorio",
          "\n4) Crear mazo ofensivo", "\n5) Crear mazo defensivo", "\n6) Crear mazo equilibrado", "\n0) Finalizar")


def menu_mazo_completo():
    # Creamos el menu para utilizarlo despues.
    print("MENU DE MAZO", "\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n3) Crear mazo aleatorio",
          "\n4) Crear mazo ofensivo", "\n5) Crear mazo defensivo", "\n6) Crear mazo equilibrado",
          "\n7) Crear mazo aleatorio Enemigo", "\n8) Crear mazo ofensivo Enemigo", "\n9) Crear mazo defensivo Enemigo",
          "\n10) Crear mazo equilibrado Enemigo", "\n0) Finalizar",
          "\n¡ALERTA! Hasta no tener un mazo aliado creado, el juego no continuara")


def menu_juego_individual():
    # Creamos el menu para utilizarlo despues.
    print("MENU DE JUEGO", "\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n3) Crear mazo aleatorio",
          "\n4) Crear mazo ofensivo", "\n5) Crear mazo defensivo", "\n6) Crear mazo equilibrado",
          "\n12) Luchar Jugador vs Bot (arcade)", "\n13) Luchar Jugador vs Bot (liga)", "\n0) Finalizar")


def menu_juego_individual_barajas():
    print("MENU DE JUEGO", "\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n3) Crear mazo aleatorio",
          "\n4) Crear mazo ofensivo", "\n5) Crear mazo defensivo", "\n6) Crear mazo equilibrado",
          "\n7) Crear mazo aleatorio Enemigo", "\n8) Crear mazo ofensivo Enemigo", "\n9) Crear mazo defensivo Enemigo",
          "\n10) Crear mazo equilibrado Enemigo", "\n12) Luchar Jugador vs Bot (arcade)",
          "\n13) Luchar Jugador vs Bot (liga)", "\n0) Finalizar")


def menu_final():
    # Creamos el menu para utilizarlo despues.
    print("MENU DE JUEGO", "\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n3) Crear mazo aleatorio",
          "\n4) Crear mazo ofensivo", "\n5) Crear mazo defensivo", "\n6) Crear mazo equilibrado",
          "\n7) Crear mazo aleatorio Enemigo", "\n8) Crear mazo ofensivo Enemigo", "\n9) Crear mazo defensivo Enemigo",
          "\n10) Crear mazo equilibrado Enemigo", "\n11) Luchar Jugador vs Jugador",
          "\n12) Luchar Jugador vs Bot (arcade)", "\n13) Luchar Jugador vs Bot (liga)", "\n0) Finalizar")


bucle_menu = False
baraja_cargada = False
enemigo_cargado = False
mazo_aliado = False
mazo_enemigo = False

while bucle_menu == False:
    # Aqui comienza el menu inicial.
    if baraja_cargada is False and enemigo_cargado is False:
        menu_inicial()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")

        while opcio < 0 or opcio > 2:

            print("TECLEA UN NUMERO ENTERO VALIDO.")
            menu_inicial()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("NO VALIDO.")

        while 0 <= opcio <= 2 and baraja_cargada is False:
            # Una vegada ha entrat al bucle, tenim les condicions per a cada opcio
            if opcio == 1:
                try:
                    baraja = ET.parse("myBaraja.xml")
                    print("Cartas cargadas.")
                    baraja_cargada = True
                    break
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 2:
                try:
                    enemigo = ET.parse("Enemigo.xml")
                    print("Cartas enemigas cargadas.")
                    enemigo_cargado = True
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            else:
                bucle_menu = True
                break
            menu_inicial()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("TECLEA UN NUMERO ENTERO VALIDO.")
            while opcio < 0 or opcio > 2 and baraja_cargada is False:
                menu_inicial()
                valido = 0
                while valido == 0:
                    try:
                        opcio = int(input("Que opcion quieres escoger?:\n"))
                        valido = 1
                    except ValueError:
                        print("TECLEA UN NUMERO ENTERO VALIDO.")
    # Aqui termina el menu inicial.

    # Aqui empieza el menu para cuando solo se ha cargado la baraja aliada
    if baraja_cargada is True and enemigo_cargado is False and mazo_aliado is False:
        menu_mazo_individual()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")

        while opcio < 0 or opcio > 6:

            print("TECLEA UN NUMERO ENTERO VALIDO.")
            menu_mazo_individual()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("NO VALIDO.")

        while 0 <= opcio <= 6 and enemigo_cargado is False and mazo_aliado is False:

            if opcio == 1:
                try:
                    baraja = ET.parse("myBaraja.xml")
                    print("Cartas cargadas.")
                    baraja_cargada = True
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 2:
                try:
                    enemigo = ET.parse("Enemigo.xml")
                    print("Cartas enemigas cargadas.")
                    enemigo_cargado = True
                    break
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 3:
                print("Crear mazo aleatorio")
                mazo_aliado_jugar = aleatorio(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            elif opcio == 4:
                print("Crear mazo ofensivo")
                mazo_aliado_jugar = ataque(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            elif opcio == 5:
                print("Crear mazo defensivo")
                mazo_aliado_jugar = defensa(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            elif opcio == 6:
                print("Crear mazo equilibrado")
                mazo_aliado_jugar = equilibrado(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            else:
                bucle_menu = True
                break
            menu_mazo_individual()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("TECLEA UN NUMERO ENTERO VALIDO.")
            while opcio < 0 or opcio > 6 and enemigo_cargado is False and mazo_aliado is False:
                menu_mazo_individual()
                valido = 0
                while valido == 0:
                    try:
                        opcio = int(input("Que opcion quieres escoger?:\n"))
                        valido = 1
                    except ValueError:
                        print("TECLEA UN NUMERO ENTERO VALIDO.")
    # Aqui termina el menu para cuando solo se ha cargado la baraja aliada.

    # Aqui empieza el menu para cuando solo tenemos un mazo aliado creado.
    if baraja_cargada is True and mazo_aliado is True and enemigo_cargado is False:

        menu_juego_individual()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")

        while opcio < 0 or (6 < opcio < 12) or opcio > 13:

            print("TECLEA UN NUMERO ENTERO VALIDO.")
            menu_juego_individual()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("NO VALIDO.")

        while 0 <= opcio <= 6 or 12 <= opcio <= 13:

            if opcio == 1:
                try:
                    baraja = ET.parse("myBaraja.xml")
                    print("Cartas cargadas.")
                    baraja_cargada = True
                    mazo_aliado = False
                    break
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 2:
                try:
                    enemigo = ET.parse("Enemigo.xml")
                    print("Cartas enemigas cargadas.")
                    enemigo_cargado = True
                    break
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 3:
                print("Crear mazo aleatorio")
                mazo_aliado_jugar = aleatorio(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 4:
                print("Crear mazo ofensivo")
                mazo_aliado_jugar = ataque(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 5:
                print("Crear mazo defensivo")
                mazo_aliado_jugar = defensa(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 6:
                print("Crear mazo equilibrado")
                mazo_aliado_jugar = equilibrado(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 12:
                print("Luchar Jugador vs Bot (arcade)")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 13:
                print("Luchar Jugador vs Bot (liga)")
                input("Pulsa cualquier tecla para volver al menu")
            else:
                bucle_menu = True
                break
            menu_juego_individual()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("TECLEA UN NUMERO ENTERO VALIDO.")
            while opcio < 0 or (6 < opcio < 12) or opcio > 13:
                menu_juego_individual()
                valido = 0
                while valido == 0:
                    try:
                        opcio = int(input("Que opcion quieres escoger?:\n"))
                        valido = 1
                    except ValueError:
                        print("TECLEA UN NUMERO ENTERO VALIDO.")
    # Aqui termina el menu para cuando solo tenemos un mazo aliado creado.

    # Aqui empieza el menu para cuando tenemos las dos barajas cargadas sin mazo aliado creado.
    if baraja_cargada is True and enemigo_cargado is True and mazo_aliado is False:
        menu_mazo_completo()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")

        while opcio < 0 or opcio > 10:

            print("TECLEA UN NUMERO ENTERO VALIDO.")
            menu_mazo_completo()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("NO VALIDO.")

        while 0 <= opcio <= 10:

            if opcio == 1:
                try:
                    baraja = ET.parse("myBaraja.xml")
                    print("Cartas cargadas.")
                    baraja_cargada = True
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 2:
                try:
                    enemigo = ET.parse("Enemigo.xml")
                    print("Cartas enemigas cargadas.")
                    enemigo_cargado = True
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 3:
                print("Crear mazo aleatorio")
                mazo_aliado_jugar = aleatorio(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            elif opcio == 4:
                print("Crear mazo ofensivo")
                mazo_aliado_jugar = ataque(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            elif opcio == 5:
                print("Crear mazo defensivo")
                mazo_aliado_jugar = defensa(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            elif opcio == 6:
                print("Crear mazo equilibrado")
                mazo_aliado_jugar = equilibrado(baraja)
                print(mazo_aliado_jugar)
                mazo_aliado = True
                input("Pulsa cualquier tecla para volver al menu")
                break
            elif opcio == 7:
                print("Crear mazo aleatorio Enemigo")
                mazo_enemigo_jugar = aleatorio(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 8:
                print("Crear mazo ofensivo Enemigo")
                mazo_enemigo_jugar = ataque(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 9:
                print("Crear mazo defensivo Enemigo")
                mazo_enemigo_jugar = defensa(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 10:
                print("Crear mazo equilibrado Enemigo")
                mazo_enemigo_jugar = equilibrado(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            else:
                bucle_menu = True
                break
            menu_mazo_completo()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("TECLEA UN NUMERO ENTERO VALIDO.")
            while opcio < 0 or opcio > 10:
                menu_mazo_completo()
                valido = 0
                while valido == 0:
                    try:
                        opcio = int(input("Que opcion quieres escoger?:\n"))
                        valido = 1
                    except ValueError:
                        print("TECLEA UN NUMERO ENTERO VALIDO.")
    # Aqui termina el menu para cuando tenemos las dos barajas cargadas sin mazo aliado creado.

    # Aqui empieza el menu para cuando tenemos las dos barajas cargadas pero solo el mazo aliado hecho.
    if baraja_cargada is True and enemigo_cargado is True and mazo_aliado is True and mazo_enemigo is False:

        menu_juego_individual_barajas()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")

        while opcio < 0 or (10 < opcio < 12) or opcio > 13:

            print("TECLEA UN NUMERO ENTERO VALIDO.")
            menu_juego_individual_barajas()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("NO VALIDO.")

        while 0 <= opcio <= 10 or 12 <= opcio <= 13:

            if opcio == 1:
                try:
                    baraja = ET.parse("myBaraja.xml")
                    print("Cartas cargadas.")
                    baraja_cargada = True
                    mazo_aliado = False
                    break
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 2:
                try:
                    enemigo = ET.parse("Enemigo.xml")
                    print("Cartas enemigas cargadas.")
                    enemigo_cargado = True
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 3:
                print("Crear mazo aleatorio")
                mazo_aliado_jugar = aleatorio(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 4:
                print("Crear mazo ofensivo")
                mazo_aliado_jugar = ataque(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 5:
                print("Crear mazo defensivo")
                mazo_aliado_jugar = defensa(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 6:
                print("Crear mazo equilibrado")
                mazo_aliado_jugar = equilibrado(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 7:
                print("Crear mazo aleatorio Enemigo")
                mazo_enemigo_jugar = aleatorio(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 8:
                print("Crear mazo ofensivo Enemigo")
                mazo_enemigo_jugar = ataque(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 9:
                print("Crear mazo defensivo Enemigo")
                mazo_enemigo_jugar = defensa(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 10:
                print("Crear mazo equilibrado Enemigo")
                mazo_enemigo_jugar = equilibrado(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 12:
                print("Luchar Jugador vs Bot (arcade)")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 13:
                print("Luchar Jugador vs Bot (liga)")
                input("Pulsa cualquier tecla para volver al menu")
            else:
                bucle_menu = True
                break
            menu_juego_individual_barajas()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("TECLEA UN NUMERO ENTERO VALIDO.")
            while opcio < 0 or (10 < opcio < 12) or opcio > 13:
                menu_juego_individual_barajas()
                valido = 0
                while valido == 0:
                    try:
                        opcio = int(input("Que opcion quieres escoger?:\n"))
                        valido = 1
                    except ValueError:
                        print("TECLEA UN NUMERO ENTERO VALIDO.")
    # Aqui termina el menu para cuando tenemos las dos barajas cargadas pero solo el mazo aliado hecho.

    # Aqui empieza el menu final.
    if baraja_cargada is True and enemigo_cargado is True and mazo_aliado is True and mazo_enemigo is True:

        menu_final()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")

        while opcio < 0 or opcio > 13:

            print("TECLEA UN NUMERO ENTERO VALIDO.")
            menu_juego_individual_barajas()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("NO VALIDO.")

        while 0 <= opcio <= 13:

            if opcio == 1:
                try:
                    baraja = ET.parse("myBaraja.xml")
                    print("Cartas cargadas.")
                    baraja_cargada = True
                    mazo_aliado = False
                    break
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 2:
                try:
                    enemigo = ET.parse("Enemigo.xml")
                    print("Cartas enemigas cargadas.")
                    enemigo_cargado = True
                    mazo_enemigo = False
                    break
                except FileNotFoundError:
                    print("No se ha podido leer el fichero")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 3:
                print("Crear mazo aleatorio")
                mazo_aliado_jugar = aleatorio(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 4:
                print("Crear mazo ofensivo")
                mazo_aliado_jugar = ataque(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 5:
                print("Crear mazo defensivo")
                mazo_aliado_jugar = defensa(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 6:
                print("Crear mazo equilibrado")
                mazo_aliado_jugar = equilibrado(baraja)
                print(mazo_aliado_jugar)
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 7:
                print("Crear mazo aleatorio Enemigo")
                mazo_enemigo_jugar = aleatorio(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 8:
                print("Crear mazo ofensivo Enemigo")
                mazo_enemigo_jugar = ataque(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 9:
                print("Crear mazo defensivo Enemigo")
                mazo_enemigo_jugar = defensa(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 10:
                print("Crear mazo equilibrado Enemigo")
                mazo_enemigo_jugar = equilibrado(enemigo)
                print(mazo_enemigo_jugar)
                mazo_enemigo = True
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 11:
                print("Luchar Jugador vs Jugador")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 12:
                print("Luchar Jugador vs Bot (arcade)")
                input("Pulsa cualquier tecla para volver al menu")
            elif opcio == 13:
                print("Luchar Jugador vs Bot (liga)")
                input("Pulsa cualquier tecla para volver al menu")
            else:
                bucle_menu = True
                break
            menu_final()
            valido = 0
            while valido == 0:
                try:
                    opcio = int(input("Que opcion quieres escoger?:\n"))
                    valido = 1
                except ValueError:
                    print("TECLEA UN NUMERO ENTERO VALIDO.")
            while opcio < 0 or opcio > 13:
                menu_final()
                valido = 0
                while valido == 0:
                    try:
                        opcio = int(input("Que opcion quieres escoger?:\n"))
                        valido = 1
                    except ValueError:
                        print("TECLEA UN NUMERO ENTERO VALIDO.")
    # Aqui termina el menu final.