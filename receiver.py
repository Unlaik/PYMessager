import time

import requests
from datetime import datetime


def print_messages(messages):
    for message in messages:
        dt = datetime.fromtimestamp(message['time'])
        print(dt.strftime('%H:%M:%S'), message['name'])
        print(message['text'])
        print()


after = 0
while True:
    response = requests.get(
    url='http://127.0.0.1:5000/messages',
    params={'after': 0})
    messages = response.json()['messages']
    if messages:
        print_messages(response.json()['messages'])
        after = messages[-1]['time']

    time.sleep(1)
