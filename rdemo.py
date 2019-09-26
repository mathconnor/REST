import requests

# r = requests.get('https://xkcd.com/353/')
# print(r)

r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r.status_code)
print()
print(r.headers)

# save the file in this directory
with open('comic.png', 'wb') as f:
    f.write(r.content)