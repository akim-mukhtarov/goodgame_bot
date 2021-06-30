import telebot
from scene  import Scene
from accounts_backend  import User

bot = telebot.TeleBot(
    "",
    parse_mode = "HTML"
)

scene = Scene()

@bot.message_handler(commands=['start'])
def greetings(message):
    user = User(message.chat.id)
    if not user.is_new(): return

    bot.send_message(
        message.chat.id,
        text=scene.text,
        reply_markup=scene.markup
        )

@bot.message_handler(commands=['pay'])
def pay(message):
    user = User(message.chat.id)
    msg = message.text.split()
    if len(msg) < 2:
        amount = 0
    else: 
        try:
            amount = int(msg[1])
            resp = user.pay(amount)
        except ValueError:
            bot.send_message(
                chat_id=message.chat.id,
                text="Сумма пополнения должна быть целым числом"
                )

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    print(call.data)
    scene.update(call)

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=scene.text,
        reply_markup=scene.markup
        )

@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text != 'КЕЙСЫ':
	    bot.send_message(
            message.chat.id, text="don't understand"
            )
    else:
        bot.send_message(
            message.chat.id, 
            text = scene.texts.start,
            reply_markup = scene.markups.start
            )

bot.polling()
