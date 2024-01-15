import json
import time

data = {
"Name":"New York",
"article": [
{"min":"1",
"sec":"8"}
]
}

x = 100
while x > 0:
    data['article'][0]['sec'] = x
    data_str = json.dumps(data)


    my_file = open ('test.json', 'w') #2
    my_file.write(data_str)
    x-=1
    my_file.close()
    time.sleep(1)



