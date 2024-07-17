#!/usr/bin/env python3
"""
uses the requests module to obtain
the HTML content of a particular URL and returns it.
"""
import requests
import redis
import time
from functools import wraps

""" Initialize Redis client """
redis_client = redis.Redis()

def count_calls(func):
    @wraps(func)
    def wrapper(url):
        """ Wrapper for decorator functionality """
        key = f'count:{url}'
        redis_client.incr(key)
        return func(url)
    return wrapper

@count_calls
def get_page(url: str) -> str:
    """ Simulate slow
    response using slowwly.robertomurray.co.uk
    """
    url = f"https://slowwly.robertomurray.co.uk/delay/10000/url/{url}"
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    test_url = "https://slowwly.robertomurray.co.uk"
    html_content = get_page(test_url)
    print(f"HTML content for {test_url}:\n{html_content}")
