from telegram import Update
from telegram.ext import CallbackContext
from scraper.hltv_scraper import get_lineup_furia,get_ranking_furia

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("🎯 Bem-vindo ao FURIA Bot!\nComandos disponíveis:\n/ranking\n/lineup\n/ultimosjogos")



async def lineup(update: Update, context: CallbackContext):
    lineup = get_lineup_furia()
    if lineup:
        msg = "👥 Lineup atual da FURIA:\n" + "\n".join(f"• {p}" for p in lineup)
    else:
        msg = "❌ Não foi possível capturar a lineup."
    await update.message.reply_text(msg)


async def ranking(update: Update, context: CallbackContext):
    ranking = get_ranking_furia()
    msg = f"🏆 Ranking atual da FURIA:\n{ranking}" if ranking else "❌ Não foi possível capturar o ranking."
    await update.message.reply_text(msg)