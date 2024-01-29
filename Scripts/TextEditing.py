# Texting editing script which formated the usually shabby pdf copy into something easily useable for me. This script was often changed up depending on what I was working on.

import re

def editMonster(path):
    textfile = open(path,'r+')
    text = textfile.readlines()

    i = 0
    offset = 0
    while i < len(text):
        if re.match('(^\([+-]\d\)$|^\d+ *\\n|(\d+ \([+-]\d\) *)+)', text[i]):
            offset += 1
        i += 1

    i=0
    while i < (len(text) - offset -1):
        if re.match('(^\d+ *\\n|(\d+ \([+-]\d\) *)+)', text[i]):
            if re.match('(^\([+-]\d+\)$|^\d+ *\\n|(\d+ \([+-]\d+\) *)+)', text[i+1]):
                line = text[i+1]
                text[i] = text[i].replace("\n"," ")
                text[i] = text[i] + line
                text.pop(i+1)
                i = i-1
        i = i+1

    i = 0
    while i < len(text):
        if re.search('Rarity:', text[i]):
            text[i] = text[i].replace("Rarity:", "Rarity.")
        
        if re.search('Diet:', text[i]):
            text[i] = text[i].replace("Diet:", "Diet.")

        if re.search('Environment:', text[i]):
            text[i] = text[i].replace("Environment:", "Environment.")

        if re.search('Taming Difficulty:', text[i]):
            text[i] = text[i].replace("Taming Difficulty:", "Taming Difficulty.")

        if re.search('Starting Bond Points:', text[i]):
            text[i] = text[i].replace("Starting Bond Points:", "Starting Bond Points.")

        if re.search('Suggested Personality:', text[i]):
            text[i] = text[i].replace("Suggested Personality:", "Suggested Personality.")
        i = i+1

    i=0
    offset2 = 1
    while i < (len(text)):
        if re.match('(^[A-Z][^:]+\.[^:]+|Actions|Reactions)', text[i]):
            offset2 = 1
            if not (i == len(text)-1):
                while not re.match('((^[A-Z].+\..+|Actions|Reactions)|^([A-Z]|[0-9]).+\:)', text[i+offset2]):
                    line = text[i+offset2]
                    text[i] = text[i].replace("\n","")
                    text[i] = text[i] + line
                    text[i+offset2] = " "
                    if(i+offset2 < len(text)-1):
                        offset2 += 1
                    else:
                        break
        i += 1

    i = 0
    spaceIndex = []
    while i < len(text):
        if (text[i] == " "):
            spaceIndex.append(i)
        i = i+1  
    
    offset3 = 0
    for space in spaceIndex:
        text.pop(space - offset3)
        offset3 += 1
        
    with open(path, 'w+') as newtextfile:
        newtextfile.writelines(text)

