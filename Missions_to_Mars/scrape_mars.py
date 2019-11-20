from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

# I wanted a headless Browser (TRUE), made things faster. GJM
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)
    listings = {}
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    listings["news_title"] = soup.find("div", class_="content_title").get_text()
    listings["news_p"] = soup.find("div", class_="article_teaser_body").get_text()

    #Next Scrape


    # Store data in a dictionary
    mars_data = {
        "news_title": listings["news_title"],
        "news_p": listings["news_p"],
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
