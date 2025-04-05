# funciones.py
# aca van todas las funciones que usamos para simular el juego

# calcula el puntaje segun kills, asistencias y muertes
def calcular_puntaje(kills, assists, deaths):
    puntos = (kills * 3) + (assists * 1) - (1 if deaths else 0)
    return puntos

# toma una ronda y actualiza las estadisticas de los jugadores
def procesar_ronda(ronda, acumulador, mvps):
    puntajes_ronda = {}

    for jugador, acciones in ronda.items():
        kills = acciones['kills']
        assists = acciones['assists']
        deaths = acciones['deaths']
        puntos = calcular_puntaje(kills, assists, deaths)

        if jugador not in acumulador:
            acumulador[jugador] = {
                'kills': 0,
                'assists': 0,
                'deaths': 0,
                'puntos': 0
            }

        acumulador[jugador]['kills'] += kills
        acumulador[jugador]['assists'] += assists
        acumulador[jugador]['deaths'] += 1 if deaths else 0
        acumulador[jugador]['puntos'] += puntos

        puntajes_ronda[jugador] = puntos

    # MVP = jugador con mas puntos en esta ronda
    mvp = max(puntajes_ronda, key=puntajes_ronda.get)
    mvps[mvp] = mvps.get(mvp, 0) + 1

# muestra la tabla del ranking
def imprimir_ranking(acumulador, mvps, ronda=None):
    if ronda is not None:
        print(f"\nRanking ronda {ronda+1}:")
    else:
        print("\nRanking final:")

    print("Jugador     Kills  Asistencias  Muertes  MVPs  Puntos")
    print("-------------------------------------------------------")

    ranking = []
    for jugador, stats in acumulador.items():
        ranking.append({
            'jugador': jugador,
            'kills': stats['kills'],
            'assists': stats['assists'],
            'deaths': stats['deaths'],
            'puntos': stats['puntos'],
            'mvps': mvps.get(jugador, 0)
        })

    ranking.sort(key=lambda x: x['puntos'], reverse=True)

    for datos in ranking:
        print(f"{datos['jugador']:<10}  {datos['kills']:<5}  {datos['assists']:<10}  {datos['deaths']:<7}  {datos['mvps']:<4}  {datos['puntos']}")

    print("-------------------------------------------------------")
