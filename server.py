from flask import Flask, request
import json
import time
import datetime


app = Flask(__name__)

database = [
    {
        'name': 'Jack',
        'text': 'Привет всем!',
        'time': time.time()
    },
    {
        'name': 'Mary',
        'text': 'Привет, Jack!',
        'time': time.time()
    },
]


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Get status</a>"


@app.route("/status")
def status():
    return {
            "status": True,
            "name": "PYMesseger",
            "time": datetime.now()
        }


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json # TODO validate
    name = data['name']
    text = data['text']

    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    database.append(message)

    print(database) #TODO remove

    return {'ok': True}

app.run()