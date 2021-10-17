import requests
from dotenv import load_dotenv
import os
import random
load_dotenv()
key = os.getenv("KEY")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
sentence = "fashion factories in the mounains"
complete_sentence  = []
for let in sentence:
    if let in punc:
        sentence = sentence.replace(let,"")
sentence = str.split(sentence)
print(sentence)

for word in sentence:
    r = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={key}"
    r = requests.get(r)
    try:
        print(r.json()[0]["meta"]["syns"][0])
        word = r.json()[0]["meta"]["syns"][0][random.randrange(0,len(r.json()[0]["meta"]["syns"][0]))]
        print(word)
        complete_sentence.append(word)
    except:
        print("No synonym")
        complete_sentence.append(word)
    

print(" ".join(complete_sentence))
