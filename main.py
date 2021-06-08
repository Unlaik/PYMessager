import datetime
import time
#dt = datetime.datetime.now()
#print(dt.year)

#print(time.time())
#dt = datetime.datetime.fromtimesamp(time.time())

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

def send_message(name,text):
    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    database.append(message)

send_message('admin','Test message from Admin')
send_message('Jack','No, this message from Jack')


def print_messages():
    for message in database:
        dt = datetime.datetime.fromtimestamp(message['time'])
        print(f'{dt.hour}:{dt.minute}', message['name'])
        print(message['text'])
        print()


def get_messages(after):
    messages = []
    for message in database:
        if message['time'] > after:
            messages.append(message)
    return messages
