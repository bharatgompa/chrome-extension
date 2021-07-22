# This script contains a function which takes a URL as input
# and returns the content of the webpage

# 'newspaper' library is used here to extract only the main
# content in a webpage
from flask import Flask,render_template
import urllib
from newspaper import Article
from flask_cors import CORS, cross_origin


app = Flask(__name__)  #creating the Flask class object  
CORS(app)
@app.route('/<name>')
def failurl(name):
	return "Please enter a valid url"
	
@app.route('/', defaults={'path': ''})
@app.route('/<path:url>')
def getContentFromURL(url):
	article = Article(url)
	article.download()
	article.parse()
	article.nlp()
	article.summary
	strKeyword = ""
	for item in article.keywords:
		strKeyword += item + " "
	return strKeyword 



if __name__ == '__main__':
    app.run(host='0.0.0.0')

