from telegram.ext import ApplicationBuilder, CommandHandler
from bot.bot_fan_cs import start, lineup, ranking
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():

    if not BOT_TOKEN:
        print("❌ BOT_TOKEN não encontrado. Verifique o .env.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Adiciona comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lineup", lineup))
    app.add_handler(CommandHandler("ranking", ranking))

    print("🤖 FURIA Bot está online...")
    app.run_polling()

if __name__ == "__main__":
    main()
