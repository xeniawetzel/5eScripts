# Splits multiple monsters (or something with similar formatting) into different files and runs the `TextEditing.py` script on each.

import TextEditing

textfile = open(r'.\Textfile.txt','r+')
text = textfile.readlines()

files = []
monsternumber = 0
monsterfile = None
for string in text:
    if (string == "#\n"):
        path = r'.\Monster' + str(monsternumber) + '.txt'
        open(path,'w+')
        files.append(path)
        monsternumber += 1
    elif (string == "#"):
        monsterfile = open(r'.\Monster' + str((monsternumber2)) +'.txt','a')
        monsterfile.write("\n")
        continue
    else:
        monsternumber2 = monsternumber-1
        monsterfile = open(r'.\Monster' + str((monsternumber2)) +'.txt','a')
        monsterfile.write(string)

for path in files:
    TextEditing.editMonster(path)
