

from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time
import re
import requests as req
import os
from selenium import webdriver


def scrape():

    def init_browser():
        # @NOTE: Replace the path with your actual path to the chromedriver
        executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

    browser = init_browser()
    #mars news url
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    base_url='https://www.jpl.nasa.gov'
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.find_by_id('full_image').click()
    time.sleep(2)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup = bs(html, "html.parser")
    image_src = soup.find('img',class_='main_image')['src']

    featured_image_url = base_url+image_src
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    mars_weather = soup.find(class_='js-tweet-text-container')
    tweet = soup.find('p', {"class": "tweet-text"})
    weather = tweet.text
    list_tables = pd.read_html("https://space-facts.com/mars/")
    mars_facts = list_tables[0]
    mars_facts.columns = ["Name", "Measurements"]
    mars_facts_html = mars_facts.to_html()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    links = []
    idklinks = soup.find_all('a', class_='itemLink product-item')
    for x in range(len(idklinks)):
        link = 'https://astrogeology.usgs.gov' + idklinks[x]['href']
        if link not in links:
            links.append(link)


    hemisphere_image_urls = []
    for x in range(len(links)):
        browser = Browser('chrome', headless=True)
        browser.visit(links[x])
        html = browser.html
        soup = bs(html, 'html.parser')
        browser.quit()
        url = 'https://astrogeology.usgs.gov' + soup.find("img", class_="wide-image")["src"]
        title = soup.find("h2", class_="title").text
        dic = {"title": title, "img_url": url}
        hemisphere_image_urls.append(dic)
    mars_planet = {
        'head': news_title,
        'body': news_p,
        'image' : featured_image_url,
        'weather': weather,
        'table': mars_facts_html,
        'hems': hemisphere_image_urls,
    }

    browser.quit()

    return mars_planet