#!/usr/bin/python3
"""1-top_ten.py"""

import requests

def top_ten(subreddit):
    """
    The  function queries the Reddit API and prints the titles of the first 10 
    hot posts listed for a given subreddit.
    
    Keyword arguments:
    subreddit -- The specified subreddit
    Return: If not a valid subreddit, print None.
    Ensure that you are not following redirects.
    """
    # Define headers
    headers = {
        'User-Agent': 'MyApp/1.1 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Make a Get req to the api and store the response
    response = requests.get('https://www.reddit.com/r/{:}/hot.json?limit=10'.format(subreddit), headers=headers, allow_redirects=False)
    # Parse the response
    if response.status_code < 300:
        json_body = response.json()
        data = json_body.get('data')
        hottest = data.get('children')

        for post in hottest:
            sub = post.get('data')
            print(sub.get('title'))
    
    else:
        print(None)