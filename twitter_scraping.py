from selenium import webdriver
from html import unescape
import csv
import bs4
import random
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.twitter.com')

button = driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]')
button.click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys('fdgrove')
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys('@hxeini60')
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div[2]/div/div/span/span').click()

# scrolling down to the bottom of a page

#solution 1
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(random.randint(0, 10))

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



#solution 2
last_height = driver.execute_script("return document.body.scrollHeight")
new_height = 0

while last_height != new_height:
from selenium.webdriver.common.keys import Keys
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

# HTML from `<html>`
#all = driver.execute_script("return document.documentElement.outerHTML;")
#all = driver.execute_script("return document.body.outerHTML;")

all = driver.page_source
html_dump = bs4.BeautifulSoup(all, 'html.parser')
results = html_dump.find_all("div", {"data-testid" : "tweet"})
hyperlinks = html_dump.find_all("a", href = True)

for link in hyperlinks:
    if 'status' in link['href'] and not '/photo/' in link['href']:
        print(link['href'])

for index, result in enumerate(results):
    print(index)
    print(result.text)


e = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div[25]')
e.text