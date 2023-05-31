#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ This function returns the numer of subscribers,
        if not valid subreddit, returns 0.
    """
    headers = {
        'User-Agent': 'vickey'
    }
    url = f"https://reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response:
        return (0)
    response = response.json()
    subscribers = response['data']['subscribers']
    return (subscribers)
