This repository servers as a demonstrator for selenium. It does so by providing some examples to scrape Twitter.
At the moment, there is a functional timeline scraper. It collects basic information on the tweets that appear on one's timeline. More specifically this includes:
- account name of sender of tweet,
- datetime information,
- tweet text,
- hyperlink to the individual tweet.

You will need to install Python on your machine:
1. https://realpython.com/installing-python/

And to make life a lot easier, also install Pycharm (makes working with Python a bit easier):
1. https://www.jetbrains.com/pycharm/

You will need the following packages:
1. selenium (https://pypi.org/project/selenium/) -> pip install selenium,
2. pandas -> pip install pandas,
3. beautifulsoup (https://pypi.org/project/beautifulsoup4/) -> pip install beautifulsoup4.

To make the script running: 
1. make sure you have a Twitter account with login information (user name and pswd),
2. add geckodriver or chromedriver to the directory in which you copy the files of this repository (for our demonstration please download chromedriver here: https://chromedriver.chromium.org/downloads),
3. run twitter_scraping.py, sit back and let the tweets come in.
 
