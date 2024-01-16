#!/usr/bin/python3
"""
The Module querries the reddit api and returns the number of subscribers
"""
# Import required modules
import requests

def number_of_subscribers(subreddit):
    """ The function uses requests to gather info
    for a given subreddit
    """
    # Define a custom User-Agent in the headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make a GET request to reddit using the specified subreddit
    response = requests.get('https://www.reddit.com/r/{:}/about.json'.format(
        subreddit), headers=headers, allow_redirects=False)
    
    # Check the response status
    if response.status_code >= 300:
        return 0
    
    # Parse the Jason Response
    json_body = response.json()

    # Extarct the data from json_body
    data = json_body.get('data')
    return(data.get('subscribers'))