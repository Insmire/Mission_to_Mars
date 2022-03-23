## Overview
The purpose of this project is to scrape four different websites in order to display the live aggregated Mars data within a single webpage by the press of a button. To this end, we inspect each webpage using Chrome Developer Tools, parse the html with Splinter and BeautifulSoup in Jupyter Notebook, download the Notebook file as a Python file, store the various structured data within NoSQL database MongoDB, and connect MongoDB and Flask using Flask-PyMongo. Then utilizing Visual Studio, we create a Flask app in app.py, construct the webpage and embellish it with Bootstrap in index.html.

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
        Visual Studio Code (VSCode) 1.63.2

## Results

The resulting webpage as of March 22, 2022 is displayed below.

