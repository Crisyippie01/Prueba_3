import funciones as fn

clientes = []
opcion = None

while opcion != 4:
    print('''
            [- Menu -]
        
        1. Registrar pedido
        2. Listar los todos los pedidos
        3. Imprimir hoja de ruta
        4. Salir del programa
            ''')
    try:
        opcion = int(input("Opcion: "))
        if opcion in range(1,5):
            print()
    except:
        print("¡Error! Opcion no es un numero, intenta nuevamente")
    else:
        if opcion == 1:
            fn.registrar_pedido(clientes)
        elif opcion == 2:
            fn.listar_pedidos()
        elif opcion == 3:
            fn.imprimir_hoja_ruta(clientes)
        elif opcion == 4:
            print("Saliendo.")
            print("Saliendo..")
            print("Saliendo...")

