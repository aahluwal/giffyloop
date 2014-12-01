import os
from flask import Flask, jsonify, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from lib.helpers import hash
import praw
import json
import pprint

app = Flask(__name__)
app.debug = True
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return render_template('home.html')

#Specify the type of request this route will accept
@app.route('/gifs', methods=['GET'])
def get_top_gifs():
	#gif_titles = []
	#if_urls = []
	r = praw.Reddit(user_agent='GiffyLoop by /u/dcordoba')
	submissions = r.get_subreddit('gifs').get_hot(limit=20)
	gifs = []
	for submission in submissions:
		gif_obj = {
			'title': submission.title,
			'url': submission.url
		}
		gifs.append(gif_obj)
	return jsonify({'gifs': gifs})
    
