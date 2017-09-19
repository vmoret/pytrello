from .api import *
from .recipes import SingletonMeta


class TrelloAPI(object, metaclass=SingletonMeta):

    def __init__(self, key=None, token=None):
        self.key = key
        self.token = token

    def get(self, url, **kwargs):
        return get(url, key=self.key, token=self.token, **kwargs)

    def post(self, url, data, **kwargs):
        return post(url, data, key=self.key, token=self.token, **kwargs)

    def put(self, url, data, **kwargs):
        return put(url, data, key=self.key, token=self.token, **kwargs)

    def delete(self, url, **kwargs):
        return delete(url, key=self.key, token=self.token, **kwargs)

