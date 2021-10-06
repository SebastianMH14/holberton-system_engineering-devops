#!/usr/bin/python3
"""recursive function that queries the Reddit API """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing the
    titles of all hot articles"""
    params = {"limit": 1, "after": after}
    headers = {"User-agent": "holbie"}
    data = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), allow_redirects=False,
        params=params, headers=headers)
    if data.status_code == 200:
        data = data.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        if after is not None:
            hot_list.append(posts[0]["data"]["title"])
            return recurse(subreddit, hot_list, after)
        else:
            return (hot_list)
    else:
        return(None)
