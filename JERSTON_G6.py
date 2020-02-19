def menu_inicial():
    # Creamos el menu para utilizarlo despues.
    print("MENU INICIAL", "\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n0) Finalizar",
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


baraja_cargada = False
enemigo_cargado = False
mazo_aliado = False
mazo_enemigo = False
# Aqui comienza el menu inicial.
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
        print("Cargar cartas")
        baraja_cargada = True
        input("Pulsa cualquier tecla para volver al menu")
        break
    elif opcio == 2:
        print("Cargar cartas Enemigo")
        enemigo_cargado = True
        input("Pulsa cualquier tecla para volver al menu")
    else:
        break
    menu_inicial()
    valido = 0
    while valido == 0:
        try:
            opcio = int(input("Que opcion quieres escoger?:\n"))
            valido = 1
        except ValueError:
            print("TECLEA UN NUMERO ENTERO VALIDO.")
    while opcio < 0 or opcio > 2 and baraja_cargada == False:
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
if baraja_cargada is True and enemigo_cargado is False:
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

    while 0 <= opcio <= 6 and enemigo_cargado == False and mazo_aliado == False:

        if opcio == 1:
            print("Cargar cartas")
            baraja_cargada = True
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 2:
            print("Cargar cartas Enemigo")
            enemigo_cargado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 3:
            print("Crear mazo aleatorio")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 4:
            print("Crear mazo ofensivo")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 5:
            print("Crear mazo defensivo")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 6:
            print("Crear mazo equilibrado")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        else:
            break
        menu_mazo_individual()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")
        while opcio < 0 or opcio > 6 and enemigo_cargado == False and mazo_aliado == False:
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
            print("Cargar cartas")
            input("Pulsa cualquier tecla para volver al menu")
            baraja_cargada = True
        elif opcio == 2:
            print("Cargar cartas Enemigo")
            input("Pulsa cualquier tecla para volver al menu")
            enemigo_cargado = True
            break
        elif opcio == 3:
            print("Crear mazo aleatorio")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 4:
            print("Crear mazo ofensivo")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 5:
            print("Crear mazo defensivo")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 6:
            print("Crear mazo equilibrado")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 12:
            print("Luchar Jugador vs Bot (arcade)")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 13:
            print("Luchar Jugador vs Bot (liga)")
            input("Pulsa cualquier tecla para volver al menu")
        else:
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

# Aqui empieza el menu para cuando tenemos las dos barajas cargadas sin mazos creados.
if baraja_cargada is True and enemigo_cargado is True and mazo_aliado is False and mazo_enemigo is False:
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
            print("Cargar cartas")
            input("Pulsa cualquier tecla para volver al menu")
            baraja_cargada = True
        elif opcio == 2:
            print("Cargar cartas Enemigo")
            input("Pulsa cualquier tecla para volver al menu")
            enemigo_cargado = True
        elif opcio == 3:
            print("Crear mazo aleatorio")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 4:
            print("Crear mazo ofensivo")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 5:
            print("Crear mazo defensivo")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 6:
            print("Crear mazo equilibrado")
            mazo_aliado = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 7:
            print("Crear mazo aleatorio Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 8:
            print("Crear mazo ofensivo Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 9:
            print("Crear mazo defensivo Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 10:
            print("Crear mazo equilibrado Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
        else:
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
# Aqui termina el menu para cuando tenemos las dos barajas cargadas sin mazos creados.

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
            print("Cargar cartas")
            input("Pulsa cualquier tecla para volver al menu")
            baraja_cargada = True
        elif opcio == 2:
            print("Cargar cartas Enemigo")
            input("Pulsa cualquier tecla para volver al menu")
            enemigo_cargado = True
        elif opcio == 3:
            print("Crear mazo aleatorio")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 4:
            print("Crear mazo ofensivo")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 5:
            print("Crear mazo defensivo")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 6:
            print("Crear mazo equilibrado")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 7:
            print("Crear mazo aleatorio Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 8:
            print("Crear mazo ofensivo Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 9:
            print("Crear mazo defensivo Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 10:
            print("Crear mazo equilibrado Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
            break
        elif opcio == 12:
            print("Luchar Jugador vs Bot (arcade)")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 13:
            print("Luchar Jugador vs Bot (liga)")
            input("Pulsa cualquier tecla para volver al menu")
        else:
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

# Aqui empieza el menu para cuando tenemos las dos barajas cargadas pero solo el mazo aliado hecho.
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
            print("Cargar cartas")
            input("Pulsa cualquier tecla para volver al menu")
            baraja_cargada = True
        elif opcio == 2:
            print("Cargar cartas Enemigo")
            input("Pulsa cualquier tecla para volver al menu")
            enemigo_cargado = True
        elif opcio == 3:
            print("Crear mazo aleatorio")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 4:
            print("Crear mazo ofensivo")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 5:
            print("Crear mazo defensivo")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 6:
            print("Crear mazo equilibrado")
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 7:
            print("Crear mazo aleatorio Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 8:
            print("Crear mazo ofensivo Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 9:
            print("Crear mazo defensivo Enemigo")
            mazo_enemigo = True
            input("Pulsa cualquier tecla para volver al menu")
        elif opcio == 10:
            print("Crear mazo equilibrado Enemigo")
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
# Aqui termina el menu para cuando tenemos las dos barajas cargadas pero solo el mazo aliado hecho.
