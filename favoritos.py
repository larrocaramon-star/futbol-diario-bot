import json
import os

ARCHIVO = "data/favoritos.json"


def cargar():
    if not os.path.exists(ARCHIVO):
        return {}

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)


def seguir(chat_id, equipo):
    datos = cargar()

    datos[str(chat_id)] = equipo

    guardar(datos)
