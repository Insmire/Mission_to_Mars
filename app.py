## convert Jupyter to Py to scrape
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
from pymongo import MongoClient

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    ## PyMongo finds the collection "mars" in db
    mars = mongo.db.mars.find_one()
    ## return an HTML template using file index.html and collection mars
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    ## point to mars collection in Mongo
    mars = mongo.db.mars
    ## use scrape_all() on exported Jupyter file scraping.py
    mars_data = scraping.scrape_all()
    ## form .update_one(query_parameter, {"$set": data}, options)
    ## {} updates the first document in collection
    ## $set modifies document with data mars_data
    ## upsert (aka update or insert) update if exists, insert new document if not
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    ## redirect to homepage after successful scraping
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()

