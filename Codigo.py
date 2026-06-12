import os

# -------------------------------------------------
#  Datos del simulador
# -------------------------------------------------
CONTRASENA_CORRECTA = "2046"
NOMBRE_ESTUDIANTE = "Hailyen Jullieth Grajales Quinonez"
CURSO = "Estructura de Datos"

VALOR_CREDITO = 159000

DESCUENTO_ESTRATO = {
    1: 15,
    2: 15,
    3: 10,
    4: 10,
    5: 5,
    6: 5,
}

GENEROS = {
    "1": "MASCULINO",
    "2": "FEMENINO",
    "3": "NO BINARIO",
    "4": "PREFIERO NO DECIRLO",
}

# Base de datos en memoria
base_de_datos = []


# -------------------------------------------------
#  Utilidades
# -------------------------------------------------
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def separador(ancho=52):
    print("-" * ancho)


def mostrar_encabezado_principal():
    print("=" * 52)
    print("   UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA")
    print("                     UNAD")
    print("=" * 52)
    print()
    print("          SIMULADOR DE MATRICULA")
    print()
    print(f"  Nombre del estudiante: {NOMBRE_ESTUDIANTE}")
    print(f"  Curso: {CURSO}")
    print()


def fmt(valor):
    return f"$ {int(valor):,}".replace(",", ".")


# -------------------------------------------------
#  Modulo 1: Contrasena
# -------------------------------------------------
def solicitar_contrasena():
    intento = 1
    while True:
        limpiar_pantalla()
        mostrar_encabezado_principal()
        separador()
        print("           CONTRASENA DE ACCESO")
        separador()

        if intento > 1:
            print()
            print("  ERROR: Contrasena incorrecta. Vuelve a intentarlo.")
            print(f"  (Intento #{intento})")

        print()
        contrasena = input("  Ingresa la contrasena: ").strip()

        if contrasena == CONTRASENA_CORRECTA:
            print()
            print("  Contrasena correcta! Acceso concedido.")
            input("\n  Presiona Enter para continuar...")
            break
        else:
            intento += 1


# -------------------------------------------------
#  Modulo 2: Formulario de datos
# -------------------------------------------------
def pedir_identificacion():
    while True:
        valor = input("  Identificacion: ").strip()
        if valor.isdigit() and len(valor) > 0:
            return valor
        print("  ERROR: Ingresa solo numeros.")


def pedir_nombre():
    while True:
        valor = input("  Nombre Completo: ").strip()
        if len(valor) >= 3:
            return valor
        print("  ERROR: Nombre demasiado corto.")


def pedir_genero():
    print()
    print("  SELECCION DE GENERO:")
    for clave, nombre in GENEROS.items():
        print(f"    {clave}. {nombre}")
    while True:
        opcion = input("  Elige una opcion (1-4): ").strip()
        if opcion in GENEROS:
            return GENEROS[opcion]
        print("  ERROR: Opcion no valida. Elige entre 1 y 4.")


def pedir_creditos():
    while True:
        try:
            creditos = int(input("  Cantidad de creditos (1 a 21): ").strip())
            if 1 <= creditos <= 21:
                return creditos
            print("  ERROR: Debe estar entre 1 y 21.")
        except ValueError:
            print("  ERROR: Ingresa un numero entero.")


def pedir_estrato():
    while True:
        try:
            estrato = int(input("  Estrato Socioeconomico (1-6): ").strip())
            if 1 <= estrato <= 6:
                return estrato
            print("  ERROR: Debe estar entre 1 y 6.")
        except ValueError:
            print("  ERROR: Ingresa un numero entero.")


def pedir_certificado_electoral():
    while True:
        resp = input("  Certificado Electoral (Si o No): ").strip().upper()
        if resp in ("SI", "NO"):
            return resp
        print("  ERROR: Responde SI o NO.")


def capturar_datos():
    limpiar_pantalla()
    mostrar_encabezado_principal()
    separador()
    print("         SIMULAR DE MATRICULA - DATOS")
    separador()
    print()

    identificacion = pedir_identificacion()
    nombre = pedir_nombre()
    genero = pedir_genero()
    creditos = pedir_creditos()
    estrato = pedir_estrato()
    certificado = pedir_certificado_electoral()

    return {
        "identificacion": identificacion,
        "nombre": nombre,
        "genero": genero,
        "creditos": creditos,
        "estrato": estrato,
        "certificado": certificado,
    }


# -------------------------------------------------
#  Modulo 3: Calculo de matricula
# -------------------------------------------------
def calcular_matricula(datos):
    creditos = datos["creditos"]
    estrato = datos["estrato"]
    cert = datos["certificado"]

    valor_base = creditos * VALOR_CREDITO
    pct_estrato = DESCUENTO_ESTRATO[estrato]
    pct_electoral = 10 if cert == "SI" else 0
    pct_total = pct_estrato + pct_electoral

    descuento_estrato = valor_base * pct_estrato / 100
    descuento_electoral = valor_base * pct_electoral / 100
    descuento_total = descuento_estrato + descuento_electoral
    valor_final = valor_base - descuento_total

    return {
        "valor_base": valor_base,
        "pct_estrato": pct_estrato,
        "descuento_estrato": descuento_estrato,
        "pct_electoral": pct_electoral,
        "descuento_electoral": descuento_electoral,
        "pct_total": pct_total,
        "descuento_total": descuento_total,
        "valor_final": valor_final,
    }


# -------------------------------------------------
#  Modulo 4: Mostrar resultado individual
# -------------------------------------------------
def mostrar_resumen(datos, calculo):
    limpiar_pantalla()
    mostrar_encabezado_principal()
    separador()
    print("         RESULTADO DE LA MATRICULA")
    separador()

    print()
    print(f"  Identificacion : {datos['identificacion']}")
    print(f"  Nombre         : {datos['nombre']}")
    print(f"  Genero         : {datos['genero']}")
    print(f"  Creditos       : {datos['creditos']}")
    print(f"  Estrato        : {datos['estrato']}")
    print(f"  Cert. Electoral: {datos['certificado']}")

    print()
    separador()
    print("  CALCULO FINAL")
    separador()
    cred = datos["creditos"]
    vb = fmt(calculo["valor_base"])
    print(f"  Valor base ({cred} creditos)     : {vb}")
    pct_e = calculo["pct_estrato"]
    est = datos["estrato"]
    desc_e = fmt(calculo["descuento_estrato"])
    print(f"  Descuento estrato {est} ({pct_e}%)  : - {desc_e}")
    if calculo["pct_electoral"] > 0:
        desc_el = fmt(calculo["descuento_electoral"])
        print(f"  Descuento cert. electoral (10%): - {desc_el}")
    else:
        print(f"  Descuento cert. electoral (0%) : - {fmt(0)}")
    separador()
    pct_t = calculo["pct_total"]
    desc_t = fmt(calculo["descuento_total"])
    vf = fmt(calculo["valor_final"])
    print(f"  TOTAL DESCUENTOS ({pct_t}%)        : - {desc_t}")
    print(f"  VALOR A PAGAR                  : {vf}")
    separador()
    print()


# -------------------------------------------------
#  Modulo 5: Base de datos
# -------------------------------------------------
def mostrar_base_de_datos():
    limpiar_pantalla()
    mostrar_encabezado_principal()
    separador()
    print("       ESTUDIANTES REGISTRADOS")
    separador()

    total = len(base_de_datos)
    print()
    print(f"  Total de estudiantes registrados: {total}")
    separador()

    if total == 0:
        print()
        print("  No hay estudiantes registrados.")
        print()
    else:
        for i, registro in enumerate(base_de_datos, start=1):
            datos = registro["datos"]
            calculo = registro["calculo"]
            print()
            print(f"  ESTUDIANTE #{i} de {total}")
            separador()
            print(f"  Identificacion    : {datos['identificacion']}")
            print(f"  Nombre            : {datos['nombre']}")
            print(f"  Genero            : {datos['genero']}")
            print(f"  Creditos          : {datos['creditos']}")
            print(f"  Estrato           : {datos['estrato']}")
            print(f"  Cert. Electoral   : {datos['certificado']}")
            print()
            vb = fmt(calculo["valor_base"])
            pct_e = calculo["pct_estrato"]
            est = datos["estrato"]
            desc_e = fmt(calculo["descuento_estrato"])
            pct_el = calculo["pct_electoral"]
            desc_el = fmt(calculo["descuento_electoral"])
            pct_t = calculo["pct_total"]
            desc_t = fmt(calculo["descuento_total"])
            vf = fmt(calculo["valor_final"])
            cred = datos["creditos"]
            print(f"  Valor base ({cred} cred.)    : {vb}")
            print(f"  Desc. estrato {est} ({pct_e}%)   : - {desc_e}")
            print(f"  Desc. cert. electoral ({pct_el}%): - {desc_el}")
            print(f"  Total descuentos ({pct_t}%)   : - {desc_t}")
            print(f"  VALOR A PAGAR         : {vf}")
            separador()

        print()
        print(f"  Fin del listado. Total: {total} estudiante(s).")
    print()
    input("  Presiona Enter para volver al menu...")


def limpiar_base_de_datos():
    limpiar_pantalla()
    mostrar_encabezado_principal()
    separador()
    print("       LIMPIAR BASE DE DATOS")
    separador()
    print()
    print(f"  Hay {len(base_de_datos)} registro(s) almacenado(s).")
    print()
    print("  Esta accion eliminara TODOS los registros.")
    confirmar = input("  Confirma (SI para continuar): ").strip().upper()
    if confirmar == "SI":
        base_de_datos.clear()
        print()
        print("  Base de datos limpiada correctamente.")
    else:
        print()
        print("  Operacion cancelada.")
    print()
    input("  Presiona Enter para volver al menu...")


# -------------------------------------------------
#  Modulo 6: Menu principal
# -------------------------------------------------
def menu_principal():
    while True:
        limpiar_pantalla()
        mostrar_encabezado_principal()
        separador()
        print("              MENU PRINCIPAL")
        separador()
        print()
        print(f"  Registros almacenados: {len(base_de_datos)}")
        print()
        print("  1. Registrar estudiante")
        print("  2. Visualizar datos almacenados")
        print("  3. Limpiar base de datos")
        print("  4. Salir")
        print()
        opcion = input("  Elige una opcion (1-4): ").strip()

        if opcion == "1":
            datos = capturar_datos()
            calculo = calcular_matricula(datos)
            base_de_datos.append({"datos": datos, "calculo": calculo})
            mostrar_resumen(datos, calculo)
            input("  Presiona Enter para volver al menu...")

        elif opcion == "2":
            mostrar_base_de_datos()

        elif opcion == "3":
            limpiar_base_de_datos()

        elif opcion == "4":
            limpiar_pantalla()
            print()
            print("  Hasta luego.")
            print()
            break
        else:
            print()
            print("  ERROR: Opcion no valida. Elige entre 1 y 4.")
            input("  Presiona Enter para continuar...")


# -------------------------------------------------
#  Punto de entrada
# -------------------------------------------------
if __name__ == "__main__":
    limpiar_pantalla()
    solicitar_contrasena()
    menu_principal()
