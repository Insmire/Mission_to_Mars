## Overview

The purpose of this project is to scrape four different websites in order to display the live aggregated Mars data within a single webpage by the press of a button. 

To this end, we inspect each webpage with Chrome Developer Tools, parse the html with BeautifulSoup and automate webpage navigation with Splinter in Jupyter Notebook, export work as a Python file, store the various structured data within the NoSQL database MongoDB, and connect MongoDB and Flask using Flask-PyMongo. Then utilizing Visual Studio, we create a Flask app in app.py, construct the webpage and embellish it with Bootstrap in index.html.

## Results

The resulting webpage as of March 22, 2022 is displayed below.

![mars_title](https://user-images.githubusercontent.com/96349090/159634340-923ce9c7-b398-447b-97a5-bc170f8ef4a6.png)

![mars_news_img_facts](https://user-images.githubusercontent.com/96349090/159634363-a200a784-a6e7-4ebd-bf92-b146a85000a9.png)

![mars_hemispheres](https://user-images.githubusercontent.com/96349090/159634388-a3a04015-5bf0-44ae-bedb-20eba041ef20.png)

## Resources

Data source:

    Mars news
        https://redplanetscience.com/

    Mars featured image
        https://spaceimages-mars.com

    Mars facts
        https://galaxyfacts-mars.com

    Mars hemispheres
        https://marshemispheres.com/

Software:

    Web scrape
        BeautifulSoup
        Chrome Developer Tools
        html5lib
        Jupyter 1.0.0 notebook 6.4.6
        lxml
        Pandas
        Python 3.9.7
        Splinter
        WebDriver-Manager

    Data storage
        MongoDB

    Web application and data display
        Bootstrap v.3 content delivery network (CDN)
        Flask
        Flask-PyMongo
        HTML
        Visual Studio Code (VSCode) 1.63.2
