from typing import Callable

from flask import Response


def add_headers(func: Callable[..., Response]):
    def decorator(*args, **kwargs):
        response = func(*args, **kwargs)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return decorator
    return add_headers
