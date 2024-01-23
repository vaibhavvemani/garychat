from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.get('/hello/<username>')
def hello(username):
    return f'<h1>Hello {escape(username)}!</h1>'
