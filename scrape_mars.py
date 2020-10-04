# import pymongo

# # Setup connection to mongodb
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)

from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

​def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
# ​
def scrape():
# NASA Mars News
​
    browser = init_browser()
​
    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(nasa_url)
​w
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
​
    # Extract the latest News Title and Paragraph 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    nasa_headline = mars_news_title.a.text
    nasa_p = mars_news_title.find('div', class_="article_teaser_body").text
​
# JPL Featured Space Image
​
​
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url) 
    browser.click_link_by_partial_text('FULL IMAGE')
    jpl_html = browser.html
    soup = BeautifulSoup(jpl_html, 'html.parser')
    image_deets = soup.find('img', class_='fancybox-image')
    featured_image_url = "https://www.jpl.nasa.gov/" + image_deets["src"] ​
​
# NASA Mars Facts
​
    mars_facts_table = pd.read_html("https://space-facts.com/mars/")
    mars_facts_table = mars_facts_table[2]
​
    # Mars Facts Table
    
​
# Mars Hemispheres
​
        
    return mars_info