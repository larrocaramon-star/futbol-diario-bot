import json
import os

ARCHIVO = "data/usuarios.json"


def cargar_usuarios():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)


def agregar_usuario(chat_id):
    usuarios = cargar_usuarios()

    if chat_id not in usuarios:
        usuarios.append(chat_id)
        guardar_usuarios(usuarios)
