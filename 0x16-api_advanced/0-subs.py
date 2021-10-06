#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    headers = {"User-agent": "goat"}
    try:
        r = requests.get('https://www.reddit.com/r/{}/about/.json'.format(
                subreddit), headers=headers)
        data = r.json()
        return(data['data']['subscribers'])
    except:
        return (0)
