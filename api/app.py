from flask import Flask
from flask import request, redirect, session
from upstash_redis import Redis
from markupsafe import escape

app = Flask(__name__)

redis = Redis(url="https://apn1-emerging-baboon-34212.upstash.io", token="AYWkACQgYjhmZWQxNWQtZjAwYy00OGI1LThiYTYtNjUwYWRkOGY2ZWQyZDc5MGM4MjllMzIxNDkzNTg2YmJjMzUwMTk2MDM0NmU=")

@app.post('/hello')
def hello():
    username = request.form['username']
    redis.set("username", f"{escape(username)}")
    return f'<h1>Hello {escape(username)}!</h1>'

@app.get('/hello')
def hello():
    username = redis.get("username")
    return f'<h1>Hello {escape(username)}!</h1>'