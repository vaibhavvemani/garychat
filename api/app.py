from flask import Flask

app = Flask("adwait")

@app.route('/')
def hello():
    return "Hello World"