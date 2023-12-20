b = {
    "test": True,
    "key": "another",
    4: "hello"
}

for k in b:
    print(k, b[k])  #k only key    b[k] value

for k, v in b.items(): #key, value with items
    print(k, v)

