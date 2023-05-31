#!/usr/bin/python3
""" This script queries the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """ This function prints the titles of the first 10
        hot posts listed for a given subreddit.
    """
    headers = {
        'User-Agent': 'vickey'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response:
        print(None)
        return (0)
    response = response.json()
    for i, post in enumerate(response['data']['children'][:10], 1):
        title = post['data']['title']
        print("{}".format(title))
    return response
