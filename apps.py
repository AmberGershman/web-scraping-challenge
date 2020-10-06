import pymongo
from flask import Flask, render_template

import mars_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongo://localhost:27017/mars_db'

mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars_scrape.find_out()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    mars_scrape = mongo.db.mars_db
    mars_data = mars_scrape.scrape()
    mongo.db.mars_scrape.update({}, mars_data, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
