<h2><strong>Learning About Mars!</strong></h2>

My assignment was to create a website that supplied information about Mars based on several different site updates but it was a bit tricky, as I was out for most of the Bootstrap lessons. If you'd like more information about my hudband's accident and susbsequent hospitalization, please click here. 

However, with determination and grit and A LOT of help from Sarah and Lisa, I was able to finish. 

I started by setting up the initial web scrape using my very best friend, Python via Pandas via Juypter Notebook, Splinter, and BeautifulSoup. This was a lovely way to parse through the html code of the browsers, and pull the appropriate divs. I won't lie - accessing the JPL image was painstaking but a friend clocked me to the "grid" div to pull from. 

<strong>The (Jupyter) Notebook</strong><br>
<i>Starring Python Gosling and Rachel McPandas</i> <br>
I was able to pull information from all four websites, scraping updated news information from NASA, images from the Jet Propulsion Lab, facts data from Space Facts, and Mars' Hemisphere images from the US Geological Services. I tried to set up a for-loop to cycle through the Hemispheres' to scrape the relevant data, but my chromedriver would crash on each attempt so was forced to visit individual pages and update hemisphere-specific dictionaries with the image url and the image title. My final test to connect to MongoDB and successfully compile the Mars data into a collection. 

<strong>Flask & Unbearable Lightness of Mongo</strong><br>
Once the code was successful in Jupyter Notebook, I began creating the app.py and mars_scrape.py files. I did have difficulty in determining how to connect to the MongoDB collection, but with help, was able to construct the Flask app to connect to the scrape file. On the advice of both Sarah Popelka and Sandhu Kumari, I manually retyped each file to remove deeply embeded errors and frustratingly vague red squiggles, which would appear under random imports or unassociated with any text/punctuation at all. Luckily, retyping seemed to fix the issues. The app.py code ran seemlessly in connecting to the scrape file, performing the scrape, and storing in the MongoDB server. 

<strong>HTML: </strong> <br>
<i>How to Make Lasagna.</i><br>
The index.html file was a bit more tricky - again because I hadn't yet caught up on missed class content. I was able to use examples from former cohorts to understand the structure and flow of the html file, but reviewed the HTML/CSS & Bootstrap videos to firmly grasp the concepts. The elements from the MongoDB collection were easy enough to incorporate, but formatting those elements were slightly more difficult. For example, I had exported the Mars facts table from the Space Facts website directly as an html table, but failed to format it before exporting. There were no column headers and the index was unnecessary. It was incredibly helpful to be able to go back to the Jupyter Notebook and run tests to ensure that the elements I would be scraping were in the appropriate format. I wasn't able to link the CSS stylesheet to the html file despite the file being linked in the header (and opening from there to the correct stylesheet). Sarah helped in sorting out the for loop - for which I had the correct elements but failed to call the right key/value syntax. In the end, I was able to successfully render the entire scrape and by pasting the styling code into the Inspector, I was extremely pleased with how much I learned, my patience (and everyone elses') and the final product. I REALLY enjoyed styling the page - this was an infurtiating but incredibly satisfying project. 

<h2 text-align: center> YOU DON'T HAVE TO BE PROUD OF ME, I'M PROUD ENOUGH FOR THE BOTH OF US </h2>
<img src="https://github.com/AmberGershman/web-scraping-challenge/blob/master/Mars%20Website%20(head).PNG" alt = "Do you SEE how pretty this is?">
