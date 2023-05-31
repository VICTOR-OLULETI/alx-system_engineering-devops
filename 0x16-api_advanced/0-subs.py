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
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return (0)
    response = res.json()
    if 'data' not in response:
        return (0)
    if 'subscribers' not in response.get('data'):
        return (0)
    subscribers = response['data']['subscribers']
    return (subscribers)
