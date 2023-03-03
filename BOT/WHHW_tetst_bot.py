from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def language(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.language_code}')


app = ApplicationBuilder().token("5781594007:AAFY2uP5qISh-zCN-NWyVyMqU6pAxMz6rec").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()