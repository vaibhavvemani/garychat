from flask import Flask
from flask import request, redirect, session
from upstash_redis import Redis
from markupsafe import escape
import os

app = Flask(__name__)

vercel_url = os.getenv('CACHE_URL')
vercel_token = os.getenv('CACHE_TOKEN')
redis = Redis(url=vercel_url, token=vercel_token)

@app.post('/hello')
def hello():
    username = request.form['username']
    message = request.form['msg']
    redis.set(f"{escape(username)}", f"{escape(message)}")

@app.get('/messages/<username>')
def gethello(username):
    message = redis.get(f"{escape(username)}")
    return f'<h1>f{escape(username)} has sent {escape(message)}!</h1>'
