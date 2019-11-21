from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraper_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    #listings = mongo.db.listings.find_one()
    listings = scraper_mars.scrape()
    return render_template("index.html", data=listings)


@app.route("/scrape")
def scraper():
    listings = mongo.db.listings
    listings_data = scraper_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True, port=5001)