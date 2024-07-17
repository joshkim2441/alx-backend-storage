#!/usr/bin/env python3
"""
uses the requests module to obtain
the HTML content of a particular URL and returns it.
"""
import requests
import redis
import time
from typing import Callable
from functools import wraps

""" Initialize Redis client """
redis_client = redis.Redis()


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        key = f'count:{url}'
        redis_client.incr(key)
        cached = redis.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        result = method(url)
        redis.setex(f"cached:{url}", 10, result)
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


if __name__ == "__main__":
    test_url = "https://slowwly.robertomurray.co.uk"
    html_content = get_page(test_url)
    print(f"HTML content for {test_url}:\n{html_content}")
