from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import pymongo


def scrape():

    browser = Browser("chrome", executable_path="C:/Users/Amber/Data_Analytics/DA Homework/web-scraping-challenge/chromedriver.exe", headless=False)
    # Scraping latest news and teaser paragraph about Mars from NASA

    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(nasa_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    # mars_news_title = soup.find_by_tag('div', class_='image_and_description_container')
    news_title = browser.find_by_css('.grid_gallery.list_view .content_title a').text
    nasa_headline = news_title
    print(nasa_headline)
    nasa_p = browser.find_by_css('.grid_gallery.list_view .article_teaser_body').text
    print(nasa_p)

    # Scraping JPL Mars image

    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    browser.find_by_id('full_image').click()
    browser.click_link_by_partial_text('more info')
    jpl_html = browser.html
    soup = BeautifulSoup(jpl_html, 'html.parser')
    image_deets = browser.find_by_css('img.main_image')['src']
    print(image_deets)
    featured_image_url = image_deets
# Scraping information about Mars as a table


    mars_facts_table = pd.read_html('https://space-facts.com/mars/')
    mars_facts_table = mars_facts_table[2].to_html()
    print(mars_facts_table)

# Scraping images and names of Mars' hemispheres

    cerberus = {}
    schiaparelli = {}
    marineris = {}
    syrtis = {}

    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    browser.click_link_by_partial_text('Cerberus')
    hemis_html = browser.html
    soup = BeautifulSoup(hemis_html, 'html.parser')
    title_class = soup.find('div', class_='content')
    cerberus.update({'title': title_class.h2.text})
    cerberus_image = soup.find_all('li')
    for i in cerberus_image:
        if 'full' in i.a['href']:
            cerberus.update({'img_url': i.a['href']})

    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    browser.click_link_by_partial_text('Schiaparelli')
    hemis_html = browser.html
    soup = BeautifulSoup(hemis_html, 'html.parser')
    title_class = soup.find('div', class_='content')
    schiaparelli.update({'title': title_class.h2.text})
    schiaparelli_image = soup.find_all('li')
    for i in schiaparelli_image:
        if 'full' in i.a['href']:
            schiaparelli.update({'img_url': i.a['href']})

    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    browser.click_link_by_partial_text('Marineris')
    hemis_html = browser.html
    soup = BeautifulSoup(hemis_html, 'html.parser')
    title_class = soup.find('div', class_='content')
    marineris.update({'title': title_class.h2.text})
    marineris_image = soup.find_all('li')
    for i in marineris_image:
        if 'full' in i.a['href']:
            marineris.update({'img_url': i.a['href']})

    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    browser.click_link_by_partial_text('Syrtis')
    hemis_html = browser.html
    soup = BeautifulSoup(hemis_html, 'html.parser')
    title_class = soup.find('div', class_='content')
    syrtis.update({'title': title_class.h2.text})
    syrtis_image = soup.find_all('li')
    for i in syrtis_image:
        if 'full' in i.a['href']:
            syrtis.update({'img_url': i.a['href']})

    mars_data = [cerberus, schiaparelli, marineris, syrtis]

    mars_scrape = {"hemispheres": mars_data,
                   "table_data": mars_facts_table,
                   "jpl_image": featured_image_url,
                   "nasa_headline": nasa_headline,
                   "nasa_p": nasa_p
                   }

    # conn = 'mongodb://localhost:27017'
    # client = pymongo.MongoClient(conn)

    # db = client.mars_information
    # db.mars_db.insert(mars_scrape)

    return mars_scrape

# if __name__ == "__main__":
    # print(scrape())
