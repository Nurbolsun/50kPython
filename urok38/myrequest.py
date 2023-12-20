import requests

response = requests.get("https://www.python.org/")

f = open('python.html', 'w', encoding='utf-8')
f.write(response.text)
f.close()
