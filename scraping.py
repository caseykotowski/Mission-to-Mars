# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
# Pandas
import pandas as pd

# Set up to run Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit mars news nasa site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading page
browser.is_element_present_by_css('div.list_text', wait_time=1)

#set up the parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Finding most recent news headline
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# And now the most recent article summary
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit the new site
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use base url to create full image url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Mars facts table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df
df.to_html()

browser.quit()





