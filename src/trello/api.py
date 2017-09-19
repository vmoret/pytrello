from urllib.parse import urljoin
from functools import partial, wraps
import requests

from .immutable import Map, JSONEncoder

__all__ = ('get', 'post', 'put', 'delete')

_build_url = partial(urljoin, 'https://api.trello.com/1/')


def tojson(func):
    @wraps(func)
    def inner(*args, **kwargs):
        resp = func(*args, **kwargs)
        code = resp.status_code
        if code == 200:
            return resp.json()
        elif code < 400:
            return None
        raise Exception('{func}(): Returned error {code}: {error}'.format(
            func=func.__name__, code=code, error=resp.text));
    return inner


@tojson
def get(url, key=None, token=None, params=None, **kwargs):
    return requests.get(_build_url(url), params=Params(key, token, params),
                        **kwargs)


@tojson
def post(url, data, key=None, token=None, params=None, headers=None, **kwargs):
    return requests.post(_build_url(url), JSONEncoder().encode(data),
                         params=Params(key, token, params),
                         headers=Headers(headers), **kwargs)


@tojson
def put(url, data, key=None, token=None, params=None, headers=None, **kwargs):
    return requests.put(_build_url(url), JSONEncoder().encode(data),
                        params=Params(key, token, params),
                        headers=Headers(headers), **kwargs)


@tojson
def delete(url, key=None, token=None, params=None, **kwargs):
    return requests.delete(_build_url(url), params=Params(key, token, params),
                           **kwargs)


class Params(Map):
    def __init__(self, key, token, params):
        if not isinstance(key, str):
            raise TypeError('Params(): Expected `key` to be a string')
        if len(key) == 0:
            raise ValueError('Params(): Expected `key` to be not empty')
        if not isinstance(token, str):
            raise TypeError('Params(): Expected `token` to be a string')
        if len(token) == 0:
            raise ValueError('Params(): Expected `token` to be not empty')
        super().__init__(Map(key=key, token=token, **Map(params)))


class Headers(Map):
    def __init__(self, headers=None):
        default = {'Content-Type': 'application/json'}
        super().__init__(Map(**default, **Map(headers)))

