#Import dependenceies
from flask import Flask, render_template, redirect, url_for
import scraping


#Initialization
app = Flask(__name__)

#Define home page
@app.route("/")
def home():
    return render_template("index.html", image_url = [])


#Scraping route
@app.route("/scrape")
def scrape():
    image_url = scraping.scrape_images()
    image_url.update_oone({})

    return redirect('/', code = 302)






#Run app
if __name__ == "__main__":
    app.run()