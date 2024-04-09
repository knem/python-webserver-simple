import requests

id = 'test'
r = requests.get('http://localhost:8000/api/get/{}'.format(id))
print(r.text)
