def menu():
    # Creamos el menu para utilizarlo despues.
    print("MENU PRINCIPAL", "\n1) Cargar cartas.", "\n2) Cargar cartas Enemigo.", "\n3) Crear mazo aleatorio",
          "\n4) Crear mazo ofensivo", "\n5) Crear mazo defensivo", "\n6) Crear mazo equilibrado",
          "\n7) Crear mazo aleatorio Enemigo", "\n8) Crear mazo ofensivo Enemigo", "\n9) Crear mazo defensivo Enemigo",
          "\n10) Crear mazo equilibrado Enemigo", "\n11) Luchar Jugador vs Jugador",
          "\n12) Luchar Jugador vs Bot (arcade)", "\n13) Luchar Jugador vs Bot (liga)", "\n0) Finalizar")

# Comentario de prueba skhfbvkgjdanhlkfjlhksda
menu()
valido = 0
while valido == 0:
    try:
        opcio = int(input("Que opcion quieres escoger?:\n"))
        valido = 1
    except ValueError:
        print("TECLEA UN NUMERO ENTERO VALIDO.")


while opcio < 0 or opcio > 13:

    print("TECLEA UN NUMERO ENTERO VALIDO.")
    menu()
    valido = 0
    while valido == 0:
        try:
            opcio = int(input("Que opcion quieres escoger?:\n"))
            valido = 1
        except ValueError:
            print("TECLEA UN NUMERO ENTERO VALIDO.")

while 0 <= opcio <= 13:
    # Una vegada ha entrat al bucle, tenim les condicions per a cada opcio
    if opcio == 1:
        print("Cargar cartas")
        input("Pulsa cualquier tecla para volver al menu")
        opcio = 15
    elif opcio == 2:
        print("Cargar cartas Enemigo")
        input("Pulsa cualquier tecla para volver al menu")
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
        input("Pulsa cualquier tecla para volver al menu")
    elif opcio == 8:
        print("Crear mazo ofensivo Enemigo")
        input("Pulsa cualquier tecla para volver al menu")
    elif opcio == 9:
        print("Crear mazo defensivo Enemigo")
        input("Pulsa cualquier tecla para volver al menu")
    elif opcio == 10:
        print("Crear mazo equilibrado Enemigo")
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
    menu()
    valido = 0
    while valido == 0:
        try:
            opcio = int(input("Que opcion quieres escoger?:\n"))
            valido = 1
        except ValueError:
            print("TECLEA UN NUMERO ENTERO VALIDO.")

    while opcio < 0 or opcio > 13:
        menu()
        valido = 0
        while valido == 0:
            try:
                opcio = int(input("Que opcion quieres escoger?:\n"))
                valido = 1
            except ValueError:
                print("TECLEA UN NUMERO ENTERO VALIDO.")
