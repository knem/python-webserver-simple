import requests

id = 'test'
data = {'key': 'value'}
r = requests.post('http://localhost:8000/api/post/{}'.format(id), json=data)
