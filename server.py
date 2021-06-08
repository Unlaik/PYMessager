from flask import Flask, request
import json
import time
import datetime
from flask import abort

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
            "time": time.time()
        }


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json # TODO validate

    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if not 0 < len(name) <= 128:
        return abort(400)
    if not 0 < len(text) < 1000:
        return abort(400)


    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    database.append(message)

    return {'ok': True}

@app.route('/messages')
def get_messages():
    try: #перехват поломаной страницы и вывод плохого реквеста
        after = float(request.args['after'])
    except:
        return abort(400)

    messages = []
    for message in database:
        if message['time'] > after:
            messages.append(message)

    return {'messages': messages[:50]} #[:50] фильтрация только первые 50 сообщений

app.run()