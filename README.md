This repository servers as a demonstrator for selenium. It does so by providing some examples to scrape Twitter.
At the moment, there is a functional feed scraper which scrapes the user's timeline. It collects basic information on the tweets that appear on one's timeline. More specifically this includes:
- Account name of sender of tweet
- Datetime information
- Tweet text
- Hyperlink to the individual tweet.

To get started for the timeline scraper:

You will need the following packages:

1. selenium (https://pypi.org/project/selenium/) -> pip install selenium
2. pandas -> pip install pandas
3. beautifulsoup (https://pypi.org/project/beautifulsoup4/) -> pip install beautifulsoup4

To make the script running: 

1. make sure you have a Twitter account with login information (user name and pswd)
2. add geckodriver or chromedriver to the directory in which you copy the files of this repository
3. run twitter_scraping.py, sit back and let the tweets come in
 
