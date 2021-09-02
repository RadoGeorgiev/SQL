import requests
import json

data = requests.get('http://jsonplaceholder.typicode.com/users')
df = data.json()
"""this is paragraph comment print('Hello, World!')"""
for i in range(10):
	print(df[i]['email'])
    
