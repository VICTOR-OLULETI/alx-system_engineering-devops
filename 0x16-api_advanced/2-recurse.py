#!/usr/bin/python3
""" This script queries Reddit API """
import requests
import sys


def recurse_temp(subreddit, hot_list=[], params={}):
    """ recurse temp, this function helps to perform the recursion
        Variables: subreddit - chosen subreddit by user input
                    hot_list - contains the list of the hot
                            posts of the subreddit
                    params  - stores the param to check if it has the
                            the after property.
    """
    headers = {
        'User-Agent': 'vickey'
    }
    url = f'https://reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, params=params)
    if not response:
        return (None)
    response = response.json()
    posts = response['data']['children']

    for post in posts:
        title = post['data']['title']
        hot_list.append(title)
    if 'after' in response['data']:
        params['after'] = response['data']['after']
        recurse_temp(subreddit, hot_list, params)
    return hot_list


def recurse(subreddit, hot_list=[]):
    """ This function returns a list containing the titles
        of all hot articles for a given subreddit.
        Pagination is used for separating pages of responses.
        Variables: subreddit - subreddit chosen by user
                    hot_list - contains the list of titles of hot articles
    """
    params = {'limit': 100}
    hot_list = recurse_temp(subreddit, hot_list, params)
    return (hot_list)


if __name__ == "__main__":
    """ call function """
    subreddit = sys.argv[1]
    recurse(subreddit)
