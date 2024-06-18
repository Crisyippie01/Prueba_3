import json

def registrar_pedido(clientes):
    
    tipos_cilindros = ['5kg','15kg','45kg']
    sectores = ['colina','centro','industrias']
    cilindros = []
    #contadores
    cinco = 0 
    quince = 0
    cuarenta_y_cinco = 0 

    nombre = input("Nombre_Apellido: ")
    direccion = input("direccion: ")
    while True:
        sector = input("sector (colina/centro/industrias): ").lower()
        if sector in sectores:
            break
        else:
            print("Sector fuera de las opciones, ingrese nuevamente.")
    while True:
        while True:
            cilindro = input("¿Cual cilindro busca? (5kg/15kg/45kg): ").lower()
            if cilindro == "5kg":
                cinco += 1
                break
            elif cilindro == "15kg":
                quince += 1
                break
            elif cilindro == "45kg":
                cuarenta_y_cinco += 1
                break
            else:
                print("Opcion invalida, ingrese nuevamente.")
        print("¿Desea seguir agregando mas cilindros?")
        opcion = input("(s/n) --> ")

        if opcion == "n":
            print("Saliendo...")
            break 
        else:
            print("Siguiente: ")
    cilindros.append({
        'cil. 5kg':cinco,
        'cil. 15kg':quince,
        'cil. 45kg':cuarenta_y_cinco
    })

    clientes.append({
        'nombre':nombre,
        'direccion':direccion,
        'sector':sector,
        'cilindros':cilindros
    })

    with open('clientes.json','w') as archivo:
        json.dump(clientes,archivo,indent=4)


def listar_pedidos():
    
    with open('clientes.json','r') as archivo: 
        leer_datos = json.load(archivo)

        for dato in leer_datos:
            print(dato)


def imprimir_hoja_ruta(clientes):
    sectores = ['colina','centro','industrias']
    cliente_por_sector = []

    print("¿Que sector quieres imprimir?")
    while True:
        opcion = input("(Colina/Centro/Industrial) --> ").lower()
        if opcion in sectores:
            print("Sector dentro del rango")
            break
        else:
            print("Sector invalido, ingrese nuevamente.")

    with open('clientes.json','r') as archivo: 
            leer_datos = json.load(archivo)

            for dato in leer_datos:
                if dato['sector'] == opcion:
                    cliente_por_sector.append(dato)

            for persona in cliente_por_sector:
                nombre = str(persona)

            
            with open('sector.txt','w') as archivo:
                escritor = archivo.write(nombre)


