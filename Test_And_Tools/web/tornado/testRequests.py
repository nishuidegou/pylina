import requests
result = 'hello'
r = requests.get('http://localhost:8888/api?id=1&value='+result)