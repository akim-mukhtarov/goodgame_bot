from telebot import types as teletypes

class TelegramFmtMarkups():
    def __init__(self):
        start = teletypes.InlineKeyboardMarkup()
        start.add(
            teletypes.InlineKeyboardButton(
                text = "Открыть кейс",
                callback_data = '{"action": "getCategories"}'
                )
            )
        start.add(
            teletypes.InlineKeyboardButton(
                text = 'Мои призы',
                callback_data = '{"action": "getPresentsList"}'
                )
            )
        start.add(
            teletypes.InlineKeyboardButton(
                text = 'Призы',
                callback_data = '{"action": "getPresentsAll"}'
                )
            )

        goBack = teletypes.InlineKeyboardMarkup()
        goBack.add(
            teletypes.InlineKeyboardButton(
                text = 'Назад',
                callback_data = '{"action": "goBack"}'
                )
            )

        self.start = start
        self.goBack = goBack


    def fmt(self, data):
        if 'markup' in data:
            keyboard = data['markup']
            if not keyboard['available_categories']:
                return self.goBack

            markup = teletypes.InlineKeyboardMarkup()
            for button in keyboard['available_categories']:
                markup.add(
                    teletypes.InlineKeyboardButton(
                        text = button['name'],
                        callback_data = '{"action": "getPresent", "params": {"category":' + str(button['required_amount'])+'}}'
                        )
                    )
        return markup
