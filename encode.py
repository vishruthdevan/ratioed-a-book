from read import read_txt
import json


def encode(text):
    text = text.replace("\n", "")
    map = {}
    with open('map.json') as mapf:
        map = json.loads(mapf.read())
    encoded_text = ''
    for j in text:
        encoded_text += map[j]
    return encoded_text


print(encode(read_txt("sample.txt")))
