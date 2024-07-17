#!/usr/bin/env python3
"""
uses the requests module to obtain
the HTML content of a particular URL and returns it.
"""
import requests
import redis
from typing import Callable
from functools import wraps

""" Initialize Redis client """
redis_client = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and
    outputs for a particular function.
    """
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        key = f'count:{url}'
        redis_client.incr(key)
        cached = redis_client.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        result = method(url)
        redis_client.set(f"cached:{url}", 0)
        redis_client.setex(f"cached:{url}", 10, result)
        return result
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """ Returns the HTML content of a given URL
    after caching the request's response
    and tracking the request.
    """
    response = requests.get(url)
    return response.text
