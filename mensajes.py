def resumen_hoy(partidos):

    if not partidos:
        return "⚽ No encontré partidos para mostrar."

    texto = "⚽ PARTIDOS DEL DÍA\n\n"

    for partido in partidos[:15]:

        local = partido["homeTeam"]["name"]
        visitante = partido["awayTeam"]["name"]

        fecha = partido["utcDate"]

        hora = fecha[11:16]

        texto += (
            f"🕐 {hora}\n"
            f"{local} vs {visitante}\n\n"
        )

    return texto
