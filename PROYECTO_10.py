import random
import numpy as np

# ---------------------------------------------------------
# 1. Probabilidades base
# ---------------------------------------------------------

# Goles posibles y sus probabilidades
GOLES = [0, 1, 2, 3, 4]
P_GOLES = [0.40, 0.30, 0.20, 0.07, 0.03]  # suman 1

# Decisiones tácticas posibles
TACTICAS = ["equilibrado", "ofensivo", "defensivo"]
P_TACTICAS = [0.50, 0.30, 0.20]  # se elige una por partido

# Equipos del torneo
equipos = ["Equipo A", "Equipo B", "Equipo C", "Equipo D"]

# Tabla de puntos
tabla = {e: {"pts":0, "pj":0, "gf":0, "gc":0} for e in equipos}

partidos_jugados = []

# ---------------------------------------------------------
# 2. Funciones de probabilidad
# ---------------------------------------------------------

def generar_goles():
    """Genera goles usando random.choices (probabilidades)."""
    return random.choices(GOLES, weights=P_GOLES, k=1)[0]

def elegir_tactica():
    """Elige táctica usando NumPy (probabilidades)."""
    return np.random.choice(TACTICAS, p=P_TACTICAS)

def factor_tactico(tactica):
    """Aplica un pequeño efecto según la táctica."""
    if tactica == "ofensivo":
        return 1.20
    if tactica == "defensivo":
        return 0.85
    return 1.00  # equilibrado

# ---------------------------------------------------------
# 3. Simulación de un partido
# ---------------------------------------------------------

def jugar_partido(eq1, eq2):
    tactica1 = elegir_tactica()
    tactica2 = elegir_tactica()

    # generar goles base
    g1 = generar_goles()
    g2 = generar_goles()

    # aplicar factores tácticos
    g1 = int(round(g1 * factor_tactico(tactica1)))
    g2 = int(round(g2 * factor_tactico(tactica2)))

    # actualizar tabla
    tabla[eq1]["pj"] += 1
    tabla[eq2]["pj"] += 1

    tabla[eq1]["gf"] += g1
    tabla[eq1]["gc"] += g2
    tabla[eq2]["gf"] += g2
    tabla[eq2]["gc"] += g1

    # puntos
    if g1 > g2:
        tabla[eq1]["pts"] += 3
        resultado = f"GANA {eq1}"
    elif g2 > g1:
        tabla[eq2]["pts"] += 3
        resultado = f"GANA {eq2}"
    else:
        tabla[eq1]["pts"] += 1
        tabla[eq2]["pts"] += 1
        resultado = "EMPATE"

    partidos_jugados.append(
        f"{eq1} {g1} - {g2} {eq2}  → {resultado} (Tácticas: {tactica1} vs {tactica2})"
    )

# ---------------------------------------------------------
# 4. Simular TODO el torneo
# ---------------------------------------------------------

def simular_torneo():
    for i in range(len(equipos)):
        for j in range(i+1, len(equipos)):
            jugar_partido(equipos[i], equipos[j])

# ---------------------------------------------------------
# 5. Mostrar tabla final
# ---------------------------------------------------------

def mostrar_tabla():
    print("\n===== TABLA FINAL =====")
    print("Equipo           | Pts | PJ | GF | GC | DG")
    print("--------------------------------------------")

    for eq, datos in tabla.items():
        dg = datos["gf"] - datos["gc"]
        print(f"{eq:15} | {datos['pts']:<3} | {datos['pj']:<2} | {datos['gf']:<2} | {datos['gc']:<2} | {dg}")

# ---------------------------------------------------------
# 6. Mostrar campeón
# ---------------------------------------------------------

def mostrar_campeon():
    ganador = max(tabla.items(), key=lambda x: x[1]["pts"])[0]
    print("\n****************************************")
    print(f" ¡El campeón del torneo es: {ganador}!")
    print("****************************************")

# ---------------------------------------------------------
# EJECUCIÓN
# ---------------------------------------------------------

print("\n===== PARTIDOS JUGADOS =====\n")
simular_torneo()

for p in partidos_jugados:
    print(p)

mostrar_tabla()
mostrar_campeon()