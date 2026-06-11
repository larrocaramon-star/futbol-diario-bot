from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from config import TOKEN_TELEGRAM
from api_futbol import partidos_hoy
from mensajes import resumen_hoy
from usuarios import agregar_usuario
from favoritos import seguir


async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE):

    agregar_usuario(update.effective_chat.id)

    await update.message.reply_text(
        "⚽ Bienvenido a GR Mundial\n\n"
        "Comandos:\n"
        "/hoy\n"
        "/seguir Uruguay\n"
        "/ayuda"
    )


async def hoy(update: Update,
              context: ContextTypes.DEFAULT_TYPE):

    partidos = partidos_hoy()

    mensaje = resumen_hoy(partidos)

    await update.message.reply_text(mensaje)


async def ayuda(update: Update,
                context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "/start\n"
        "/hoy\n"
        "/seguir Uruguay\n"
        "/ayuda"
    )


async def seguir_equipo(update: Update,
                        context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text(
            "Ejemplo:\n/seguir Uruguay"
        )
        return

    equipo = " ".join(context.args)

    seguir(
        update.effective_chat.id,
        equipo
    )

    await update.message.reply_text(
        f"✅ Ahora sigues a {equipo}"
    )


def main():

    app = (
        ApplicationBuilder()
        .token(TOKEN_TELEGRAM)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("hoy", hoy)
    )

    app.add_handler(
        CommandHandler("ayuda", ayuda)
    )

    app.add_handler(
        CommandHandler("seguir", seguir_equipo)
    )

    print("GR Mundial iniciado")

    app.run_polling()


if __name__ == "__main__":
    main()
