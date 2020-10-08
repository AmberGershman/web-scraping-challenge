from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import mars_scrape
import mars_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://127.0.0.1:27017/mars_db'
mongo = PyMongo(app)
# mongo = MongoClient('mongodb://localhost:27017/mars_db')

@app.route("/")
def index():
    mars_data_db = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars_data=mars_data_db)

@app.route("/scrape")
def scrape():
    # mars_data_ = mongo.db.mars_db
    mars_data = mars_scrape.scrape()
    mongo.db.mars_collection.update({}, mars_data, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
