# Mission to Mars
Web scraping for Mars Data. The purpose of this code is to take the most recent story on mars from nasa's webpage, as well as add other relevant information on the Red Planet from easy to scrape site. The page contains the following information:

### Mars News
This piece of the scraping code sends an automated browser to nasa's "Red Planet Science" website. There it takes the most recent news article headline, and the introduction sentences. I do this using an html parser, and check for the html tags I know to be associated with the front page article. 

### Mars Featured Image
Next, I send the automated browser to a website dedicated to images of mars. I inspected the page to find the html tags associated with the top image, and I saved that url to be posted to my site.

### Mars Facts
After, my browser visits a website dedicated to collecting facts on mars, and collects the data to make a table on Mars' basic facts. 

### Hemisphere Identification
Fianlly, I visit another nasa site to grab images of Mars' hemispheres. This one is a little more tricky as I had to navigate to a second page and back to grab the full image. 

### Foramting
To make this more user friendly, I used bootstrap to make this html webpage mobile interactive. The page will change sizes dependning on the type of device used to view it. I also added a few fun elements, such as a custom color scheme and some title formating. 
