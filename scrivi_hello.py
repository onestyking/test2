import telegram

TOKEN = "TUO_TOKEN_BOT"
CHAT_ID = "TUO_CHAT_ID"

bot = telegram.Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Ciao!")
