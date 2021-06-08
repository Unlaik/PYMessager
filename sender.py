import requests

response = requests.post(
    url='http://127.0.0.1:5000/send',
    json={'name': 'Jack', 'text': '123'}
)

print(response.status_code)
print(type(response.text))
print(response.text)
print(type(response.json()))
print(response.json())