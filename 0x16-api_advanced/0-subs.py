#!/usr/bin/python3
""" This script queries the reddit api """
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
    response = requests.get(url, headers=headers)
    if not response:
        return (0)
    response = response.json()
    subscribers = response['data']['subscribers']
    return (subscribers)


if __name__ == "__main__":
    """ calls the function """
    subreddit = sys.argv[1]
    number_of_subscribers(subreddit)
