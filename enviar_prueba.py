import os
import requests

TOKEN = os.getenv("TOKEN_TELEGRAM")
CHAT_ID = os.getenv("CHAT_ID")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

mensaje = {
    "chat_id": CHAT_ID,
    "text": "✅ GR Mundial conectado correctamente a GitHub Actions."
}

respuesta = requests.post(url, json=mensaje)

print(respuesta.text)
