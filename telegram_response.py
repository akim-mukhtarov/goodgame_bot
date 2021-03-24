class Telegram_Response:
    def __init__(self, response_obj):
        self.__status_code = response_obj.status_code
        self.data = response_obj.json()
        self.messages = self.data['result']

    def is_ok(self):
        # проверяем коды http код ответа и код ответа телеграмма
        if self.__status_code and self.data['ok']: return True
        
    def get_new_messages(self, since):
        # получаем только те сообщения, которые новее прочитанных
        return filter(lambda x: x['update_id'] >= since, self.messages)
