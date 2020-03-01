from selenium import webdriver
import time
import pas
from selenium.webdriver.common.keys import Keys
import pandas as pd
import bs4
import random
import datetime
import os

status = True
driver = webdriver.Chrome('chromedriver.exe')
if status:
    driver.get('https://www.twitter.com')
    time.sleep(5)
    # login
    driver.find_element_by_name('session[username_or_email]').send_keys(pas.login)
    driver.find_element_by_name('session[password]').send_keys(pas.pasword)
    driver.find_element_by_xpath("//*[contains(text(), 'Log in')]").click()
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div[2]/div/div/span/span').click()
    except:
        print("no cookies, no problem")

def capture_tweets(driver, css_selector="div[class='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-5f2r5o r-1mi0q7o']"):
    page = driver.page_source
    html_page = bs4.BeautifulSoup(page, 'html.parser')
    # current selector is based on page inspection - might change
    tweets = html_page.select(css_selector)
    return tweets

def capture_ẗweet_data(tweets):
    # tweets is a list containing a number of BS4 tag objects
    user = []
    datetime = []
    tweet_text = []
    comments = []
    retweets = []
    likes = []
    tweet_url = []

    for index, tweet in enumerate(tweets):
        print("fetching tweet number", index)
        user.append(tweet.find('a')['href'])
        if tweet.select_one("time") is None:
            datetime.append("no datetime found")
        else:
            datetime.append(tweet.select_one("time")['datetime'])
        if tweet.select_one("div[class='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0']") is None:
            tweet_text.append("no text found - could be vid of pic only")
        else:
            tweet_text.append(tweet.select_one("div[class='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0']").text)
        social = tweet.select("div[class='css-1dbjc4n r-1iusvr4 r-18u37iz r-16y2uox r-1h0z5md']")
        comments.append(social[0].text)
        retweets.append(social[1].text)
        likes.append(social[2].text)
        try:
            tweet_url.append(tweet.select_one("a[class='css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']")['href'])
        except:
            tweet_url.append("no url found")
    kle = pd.DataFrame(list(zip(user, datetime, tweet_text, comments, retweets, likes, tweet_url)),
                       columns=["sender", "datetime", "text", "comments", "retweets", "likes", "tweet_url"])
    return kle

def scroll(driver, key1=Keys.HOME, key2=None):
    # as a standard it scrolls to top of the page using the home key but any key can be used
    # this should always be a call to the Keys function
    if key2:
        driver.find_element_by_tag_name('body').send_keys(key1 + key2)
    else:
        driver.find_element_by_tag_name('body').send_keys(key1)

def scroll_to_bottom(driver, security=1):
    # https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
    # higher security means that we will keep on trying more times to scroll to the bottom
    # the reason for this is that Twitter sometimes loads slowly so with low security you run the danger of
    # stopping too fast

    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(security):
        status = True
        while status:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(random.randint(6, 10))
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                status = False
            last_height = new_height
    scroll(driver, Keys.CONTROL, Keys.DOWN)
    return print("we reached the bottom aye aye")

def collect_full_timeline(driver, testing=False, test_runs=3, return_cleaned=True, write_csv=True):
    #write_csv writes the dataframe to a csv file named timeline.csv in the current folder
    twets = pd.DataFrame(columns=["sender", "datetime", "text", "comments", "retweets", "likes", "tweet_url"])
    top_reached = False
    if testing:
        print("starting up test procedure")
        for i in range(test_runs):
            tweets = capture_tweets(driver)
            twets = twets.append(capture_ẗweet_data(tweets))
            driver.execute_script("window.scroll(0, window.scrollY - window.innerHeight);")
            driver.execute_script("window.scroll(0, window.scrollY - window.innerHeight);")
            time.sleep(random.randint(1, 5))
        print("we successfully acquired", test_runs, " pages of tweets")
    else:
        while not top_reached:
            print("starting data collection")
            tweets = capture_tweets(driver)
            twets = twets.append(capture_ẗweet_data(tweets))
            driver.execute_script("window.scroll(0, window.scrollY - window.innerHeight);")
            driver.execute_script("window.scroll(0, window.scrollY - window.innerHeight);")
            time.sleep(random.randint(1, 5))
            location = driver.execute_script("return window.scrollY")
            if location <= 50:
                top_reached = True
                print("we reached the top aye aye")
    if return_cleaned:
        twets = twets.drop_duplicates()
    if write_csv:
        today = datetime.datetime.today().strftime("%d%m%Y_%H%M%S")
        twets.to_csv("timeline_" + today + ".csv", sep=";")
        print("your csv file can be found in your current working directory which is: ", os.getcwd())
    return twets

scroll_to_bottom(driver, security=1)
timeline = collect_full_timeline(driver, testing=True, test_runs=4, return_cleaned=True, write_csv=True)




