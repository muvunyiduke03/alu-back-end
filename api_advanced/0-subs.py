#!/usr/bin/python3'
"""Queries the Reddit api and Returns the number of subscribers"""

import requests

def numSubscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'python:subressit.subscriber.count:v1.0 (by /u/fakeuser)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
        
    except Exception:
        return 0
