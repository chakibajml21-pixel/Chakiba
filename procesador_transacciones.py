def leer_y_almacenar_datos(nombre_archivo):
    transacciones = []

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                cliente_id, tipo, monto = linea.strip().split(",")

                transaccion = {
                    "ClienteID": cliente_id,
                    "Tipo": tipo,
                    "Monto": float(monto)
                }

                transacciones.append(transaccion)

        return transacciones

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
        return []


def calcular_monto_total(lista_transacciones):
    total = 0

    for transaccion in lista_transacciones:
        total += transaccion["Monto"]

    return total


def filtrar_por_tipo(lista_transacciones, tipo_filtro):
    lista_filtrada = []

    for transaccion in lista_transacciones:
        if transaccion["Tipo"] == tipo_filtro:
            lista_filtrada.append(transaccion)

    return lista_filtrada


def ejecutar_sistema():
    datos = leer_y_almacenar_datos("transacciones.txt")

    print("=== TRANSACCIONES CARGADAS ===")
    for transaccion in datos:
        print(transaccion)

    total = calcular_monto_total(datos)

    print("\n=== MONTO TOTAL ===")
    print(total)

    creditos = filtrar_por_tipo(datos, "CREDITO")

    print("\n=== TRANSACCIONES CREDITO ===")
    for transaccion in creditos:
        print(transaccion)


ejecutar_sistema()