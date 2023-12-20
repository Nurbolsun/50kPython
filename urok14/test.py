import json
with open('text.txt', 'r') as f:
    data = json.load(f)
print(data)