import requests

name = input("Input your name: ")

while True:
    text = input()
    response = requests.post(
        url='http://127.0.0.1:5000/send',
        json={'name': name, 'text': text},

)
