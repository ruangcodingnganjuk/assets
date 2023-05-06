import telebot
api = '5887781535:AAF8AXMDMtfAjjrr0zEaShztySq-vw6utno'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'hello')

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'pikir sendiri')
bot.polling()