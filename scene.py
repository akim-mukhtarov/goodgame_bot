from markups import TelegramFmtMarkups
from texts import TelegramFmtTexts
from accounts_backend import AccountsBackend
import json

class Scene():
    '''
    Класс предоставляет форматированные для бота
    текст и разметку в зависимости от колбэка.
    данные либо локальные, либо берутся с сервера
    '''
    def __init__(self):
        self.backend = AccountsBackend()
        self.markups = TelegramFmtMarkups()
        self.texts = TelegramFmtTexts()

        self.markup = self.markups.start
        self.text = self.texts.start

        self.source_map = {
            'goBack': {
                'text': {
                    'data': self.texts.start,
                    'is_static': True
                    },
                'markup': self.markups.start
                },

            'getPresentsList': {
                'text': {
                    'data': self.texts.getPresentsList,
                    'is_static': False
                    },
                'markup': self.markups.goBack
                },

            'getPresentsAll': {
                'text': {
                    'data': self.texts.getPresentsAll,
                    'is_static': True
                    },
                'markup': self.markups.goBack
                },

            'getPresent': {
                'text': {
                    'data': self.texts.present_success,
                    'is_static': False
                    },
                'markup': self.markups.goBack
                },
            }


    def update(self, callback):
        call_data = json.loads(callback.data)
        action  = call_data['action']
        params = {}
        
        if 'params' in call_data:
            params = call_data['params']
            if not 'tg_id' in params:
                params['tg_id'] = callback.message.chat.id
        else:
            params['tg_id'] = callback.message.chat.id

        if action in self.source_map:
            scene = self.source_map[action]
            # определяем текст
            if scene['text']['is_static']:
                self.text = scene['text']['data']
            else:
                resp = self.backend.get(
                    url=action,
                    params=params
                    )
                self.text = self.texts.fmt(resp)
            self.markup = scene['markup']
        else:
            resp = self.backend.get(
                url=action,
                params=params
                )
            self.markup = self.markups.fmt(resp)
            self.text = self.texts.fmt(resp)

