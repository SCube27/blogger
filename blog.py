from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

# This is dummy data, it'll actually come from a database
posts = [
    {
        'author':'Sahil Shah',
        'title':'Real Love',
        'content':'real love happens only once like Sahil has with Sakshi',
        'date_posted':'31st October 2023'
    },
    {
        'author':'Sakshi Paygude',
        'title':'My Partner',
        'content':'I am really fortunate to have found a real love and life partner in Sahil! I Love Him Alottt!',
        'date_posted':'14th February 2024'
    }
]

# Every route describes a page of the website
@app.route("/") # The / in the brackets indicates home page
# The function gets called when the page opens and whatever is in it runs 
def love() :
    return render_template('home.html', posts=posts)

@app.route("/about") # The /about is for the about page of the website
def about() :
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

# So basically the routes form the instances to the web pages(in easy words form web pages for the URLs)