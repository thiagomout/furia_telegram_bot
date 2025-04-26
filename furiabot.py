from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou o bot da equipe de Counter Strike da FURIA.")
    await update.message.reply_text("Estou aqui para ajudar você com informações sobre o time e o jogo.")
    await update.message.reply_text("Digite /ajuda para ver os comandos disponíveis.")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7220702039:AAGfNDwqLkal2aSU9Ue2AT-9A9bbVFemshY").build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()