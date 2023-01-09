import hashlib
import requests

from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from flask import Flask, make_response
from datetime import date, datetime, timezone

# app = Flask(__name__)

# app.route('/')




    

def generate_rss():
    


    dt = datetime.now()
    dt = dt.replace(tzinfo=timezone.utc)

    fg = FeedGenerator()
    fg.title('UK Economy RSS')
    fg.description('RSS feed capturing updates to the ONS UK Economy blog')
    fg.link(href='https://93b9-51-141-125-233.eu.ngrok.io')
    # fg.image(url_for('misc', filename='icon.png'))


    response = make_response(fg.rss_str())
    response.headers.set('Content-Type', 'application/rss+xml')
    return response

scrape_blog()