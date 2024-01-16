API Advanced
------------------------
![API](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png)
-------------------------------------------------------------

Contents
-------------------------------------------------

[Introduction](#introduction)
[Author](#author)
[Tasks](#tasks)

------------------------------------------------------------

# Introduction
--------------------------------------------------------------
- For the API Advanced project we are going to practice with an actual API

- A Great Application Programming Interface to use for practice is the [Reddit](https://www.reddit.com/dev/api/) API.

- There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented.

- Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.
-----------------------------------------------------------

# Author
-----------------------------------------
Natalie Wanjiru Wanjiku

---------------------------------------------------

# Tasks
----------------------------------------------------------

Task 0
-------------

0. How many subs?
mandatory
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
-----------------------------------------------------

Task 1
----------

1. Top Ten
mandatory
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
----------------------------------------------------------

Task 2
---------------

2. Recurse it!
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

Prototype: def recurse(subreddit, hot_list=[])
Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
If not a valid subreddit, return None.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)
---------------------------------------------------

![reddit](https://th.bing.com/th/id/OIP.GC_uJfO9sXnkJyXYJutCrwHaIk?rs=1&pid=ImgDetMain)