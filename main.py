import os
from flask import Flask, jsonify, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from lib.helpers import hash
import praw
import json

app = Flask(__name__)
app.debug = True
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)


@app.route('/')
def hello():
    return render_template('home.html')

#Specify the type of request this route will accept
@app.route('/gifs', methods=['GET'])
def get_top_gifs():
	r = praw.Reddit(user_agent='GiffyLoop by /u/dcordoba')
	query = 'url:gif'
	submissions = r.search(query=query, subreddit='funny', sort='hot', period='day', limit=100)
	gifs = []
	for submission in submissions:
		gif_obj = {
			'title': submission.title,
			'url': submission.url
		}
		gifs.append(gif_obj)
	return jsonify({'gifs': gifs})
    
