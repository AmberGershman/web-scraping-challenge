





from flask import Flask, render_template
import scrape_mars
import pymongo
app = Flask(__name__)
​# Create a connection to MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_db'
mongo = PyMongo(app)
​
# Create a route that renders index.html template
​
@app.route("/")
def index():
    mars_data = mongo.db.mars_scrape.find_one()
    return render_template("index.html", mars_data=mars_data)
​
@app.route("/scrape")
def scrape():
​
    mars_scrape = mongo.db.mars_db
    mars_data = mars_scrape.scrape()
    mongo.db.mars_scrape.update({}, mars_data, upsert=True)
    return redirect('/', code=302)
​
if __name__ == "__main__":
