import requests
from config import API_KEY

BASE_URL = "https://api.football-data.org/v4"


def partidos_hoy():

    headers = {
        "X-Auth-Token": API_KEY
    }

    try:
        respuesta = requests.get(
            f"{BASE_URL}/matches",
            headers=headers,
            timeout=30
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        return datos.get("matches", [])

    except Exception as error:
        print(f"Error obteniendo partidos: {error}")
        return []
