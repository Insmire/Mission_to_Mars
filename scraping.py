# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

## pd for read_html() and to_html()
import pandas as pd

## show time that code was run
import datetime as dt

def scrape_all():
    # initiate headless driver for deployment
    ## set up url for scraping
    ## headless=True means we don't see browser while scraping
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemi_img(browser)
    }

    # stop webdriver and return data
    browser.quit()
    return data



# Add try/except for error handling

def mars_news(browser):

    # scrape mars news
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # converst the browser html to a soup object and then quit the browser
    ## search for tag <div> class attribute "list_text" 
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # add try/except for error handling
    ## try-except statement for scraping;
    ## return nothing if attribute error, continue to run resut of code if all other errors
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        ## get_text() will only return the element, no tag
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

### JPL Space Images Featured Images

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    ## f string is cleaner and executed at run-time, so better for live data
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

### Facts Table

def mars_facts():
    # add try/except for error handling
    try:
        # use "read_html" to scrape the facts table into a dataframe
        ## take html of table and convert to df
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    ## BaseException is a catch-all for built-in exceptions;
    ## used here due to using pandas' read_html() instead of BeautifulSoul or Splinter
    except BaseException:
        return None
    
    # assign columns and set index of dataframe
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    df

    ## convert df to html format, add bootstrap
    return df.to_html(classes="table table-responsive table-bordered table-striped table-hover")

def hemi_img(browser):
    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    for i in range(4):
        hemispheres={}
        tag=browser.find_by_tag("h3")[i]
        title=tag.text
        tag.click()
        url=browser.links.find_by_text("Sample")[0]["href"]
        hemispheres={"title": title, "img_url": url}
        hemisphere_image_urls.append(hemispheres)
        browser.back()

    # 4. Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls

## tells Flask that code is ready to run
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

