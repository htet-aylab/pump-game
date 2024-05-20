from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = '6726144774:AAEbBWrAo4zP4rW-Ln8q-HJngQWzR1WX2TY'
GAME_URL = 'https://maxhtuan.github.io/Aylab-TMA/'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome to the WebGL Game Bot! Type /play to start the game.')

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Play the game here: {GAME_URL}')

def main() -> None:
    # Initialize the Application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
