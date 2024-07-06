from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
import os
from dotenv import load_dotenv
load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_USERNAME= os.environ.get('BOT_USERNAME')

#Commands
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your friendly syc clerk!')

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('let me know what you need help with')

async def custom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('custom command')

# Responses 
def handle_response(text:str) -> str:
    if 'hello' in text:
        return 'Hey there!'
    else:
        return 'Not free'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: {text}')
    if BOT_USERNAME in text:
        new_text: str = text.replace(BOT_USERNAME, '').strip()
        response: str = handle_response(new_text)
    else:
        response: str = handle_response(text)

    await update.message.reply_text(response)

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).build()

    # Command with the / function in telegram
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    # others
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling()
