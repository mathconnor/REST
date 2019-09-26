import requests
from pprint import pprint

# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)

# print(r.url)

payload = {'username': "mathconnor", 'count': 25}
r = requests.post('https://httpbin.org/post', data=payload)

pprint(r.json())

print()

r_dict = r.json()

pprint(f"headers: {r_dict['headers']}")

