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
    url = f'https://reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers)
    if not response:
        print(None)
        return (0)
    response = response.json()
    for i, post in enumerate(response['data']['children'][:10], 1):
        title = post['data']['title']
        print(f"{title}")
    return response


if __name__ == "__main__":
    """ calls the function """
    subreddit = sys.argv[1]
    top_ten(subreddit)
