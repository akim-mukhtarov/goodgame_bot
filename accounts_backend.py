import requests as r
import json

class User():
    def __init__(self, tg_id):
        self.tg_id = tg_id
        self.url = 'http://127.0.0.1:8000/'
    
    def pay(self, amount):
        resp = r.get(
            url=self.url+'pay',
            params={
                'tg_id': self.tg_id,
                'amount': amount
                }
            )
        return resp

    def is_new(self):
        resp = r.get(
            url=self.url+'isPartisipant/',
            params={
                'tg_id': self.tg_id
                }
            )
        if resp.status_code == 201:
            return True
        else:
            return False


class AccountsBackend():
    def __init__(self):
        self.url='http://127.0.0.1:8000/'
        self.handlers = {
            'getPresentsList': self.getPresentsList,
            'getPresent': self.getPresent,
            'getCategories': self.getCategories
        }

    def get(self, url, params):
        handler = self.handlers[url]
        return handler(params)

    def getPresentsList(self, params): 
        # get user's presents list from db
        resp = r.get(
            self.url+'getPresentsList/',
            params=params
            )
        resp = resp.json()

        d = {
            'text': {
                'data': resp,
                'from': 'getPresentsList'
                }
            }
        return d


    def getPresent(self, params):
        # randomly pick present from selected category
        resp = r.get(
            self.url+'getPresent/',
            params=params
            )
        resp = resp.json()

        d = {
            'text': {
                'data': resp,
                'from': 'getPresent'
                }
            }
        return d
    

    def getCategories(self, params):
        # get a list of available categories
        resp = r.get(
            self.url+'getCategories/',
            params=params
            )
        print(resp.text)
        resp = resp.json()
        
        d = {
            'text': {
                'data': resp,
                'from': 'getCategories'
                },
            'markup': resp
            }
        return d

