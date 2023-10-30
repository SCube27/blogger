from flask import Flask
app = Flask(__name__)

# Every route describes a page of the website
@app.route("/") # The / in the brackets indicates home page
# The function gets called when the page opens and whatever is in it runs 
def love() :
    return "<h1>Sakshi Loves Sahil <<<3</h1>" # Usually in websites the html files are returned over here

@app.route("/about") # The /about is for the about page of the website
def about() :
    return "<h1>The story of Sakhil starts far early and is never ending and they both are inseparable forever! <3 As they always come to each other how apart they go</h1>"

if __name__ == '__main__':
    app.run(debug=True)

# So basically the routes form the instances to the web pages(in easy words form web pages for the URLs)