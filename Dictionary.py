
#The data searched from a json file named DictionaryData.json
import json
from difflib import get_close_matches

data = json.load(open("DictionaryData.json"))

def translate(word):

    if word.lower() in data:
        print(word.lower() + " : ")
        for line in data[word.lower()] :
            print(line.rjust(len(line)+len(word)))
    
    elif word.title() in data:
        print(word.title() + " : ")
        for line in data[word.title()] :
            print(line.rjust(len(line)+len(word)))
    
    elif word.upper() in data:
        print(word.upper() + " : ")
        for line in data[word.upper()] :
            print(line.rjust(len(line)+len(word)))
    
    elif len(get_close_matches(word , data.keys(), cutoff = 0.8)) > 0 :
        f = get_close_matches(word , data.keys())[0]
        print(f + " : ")
        for line in data[f] :
            print(line.rjust(len(line)+len(f)))
    
    else:
        print("Did not found any match!!!")

#----------------------------------------------------------------------------------------------
while True :
    word = input("\nEnter the word you want to search : ")
    translate(word)
    if input("\nSearch again y/n : ") != 'y' :
        break
