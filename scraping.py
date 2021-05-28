# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
# Pandas
import pandas as pd
import datetime as dt

def scrape_all():
# Set up to run Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    news_title, news_paragraph = mars_news(browser)
#Scraping results
    data = {
    "news_title": news_title,
    "news_paragraph": news_paragraph,
    "featured_image": featured_image(browser),
    "facts": mars_facts(),
    "last_modified": dt.datetime.now(),
    "hemispheres": hemispheres(browser)}
    
    #Stop webdriver, return data
    browser.quit()
    return data

def mars_news(browser):
    # Visit mars news nasa site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #set up the parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    try:
        slide_elem = news_soup.select_one('div.list_text')
        #slide_elem.find('div', class_='content_title')

        # Finding most recent news headline
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # And now the most recent article summary
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None
    return news_title, news_p



def featured_image(browser):
    # Visit the new site
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
    # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None

    # Use base url to create full image url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

def mars_facts():
    try:
    # Mars facts table
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
        
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    
    return df.to_html(classes="table table-striped")

def mars_hemispheres(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []
    # a class = "itemLink product-item".get('href') takes you there
    # img class="wide-image" get 'src'
    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    #Looping only over 4 because I know there are 4 himispheres
    for i in range(4):
        #empty dictionary to add the title, img_url key:value pairs
        hemispheres = {}
        #grab the link to the main picture
        browser.find_by_css('a.product-item h3')[i].click()
        #grab the picture link
        element = browser.find_link_by_text('Sample').first
        img_url = element['href']
        title = browser.find_by_css("h2.title").text
        hemispheres["img_url"] = img_url
        hemispheres["title"] = title
        # add the dictionary to the list
        hemisphere_image_urls.append(hemispheres)
        browser.back()
    return hemisphere_image_urls


if __name__ == "__main___":
    # If running as script, print scraped data
    print(scrape_all())







