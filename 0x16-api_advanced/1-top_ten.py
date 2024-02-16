#!/usr/bin/python3

"""
print the titles of the first 10 hot posts in subreddits
"""

import requests


def top_ten(subreddit):
    """ 10 hot posts listed for a given subreddit"""
    url = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".
                       format(subreddit),
                       headers={"User-Agent": "Custom"})

    if url.status_code == requests.codes.ok:
        for post in url.json()['data']['children']:
            post_data = post["data"]
            print(post_data["title"])
    else:
        print(None)
