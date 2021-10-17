import requests
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("KEY")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
sentence = "Vertigo is an evil bot and hates everyone, especially me"
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
        length = 0
        longest_word = ""
        for word in r.json()[0]["meta"]["syns"][0]:
            if len(word) >= length:
                longest_word = word
                length = len(word)
        print(longest_word)
        complete_sentence.append(longest_word)
    except:
        print("No synonym")
        complete_sentence.append(word)
    
print(complete_sentence)
