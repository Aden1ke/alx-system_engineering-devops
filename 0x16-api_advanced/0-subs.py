#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    class for number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
