#Fixed table entries by inserting repetitive syntax and saving it inside a new file.

# package to work with textfiles
import re

# reading the tabledata file and saving it in *text*
textfile = open(r'.\TableData.txt','r+')
# is stored as an array of strings, one string being one line until a break
text = textfile.readlines()

# opening a new file that is created called FixedTableData, where the fixed Table is going to be
path = r'.\FixedTableData.txt'
open(path,'w')
# saving the file as *file*
file = open(r'.\FixedTableData.txt', 'w+')
# going through all strings in the array

def  createTableEntry(line):
    if re.search(',', line):
        line = line.replace(',', '|SCoC},', 1)

    if re.search(',', line):
        line = line.replace(',', '","')

    if re.search('\n', line):
        if not re.search('[#]$', line):
            lineContent = line
            line = line.replace(lineContent, '[ "{@creature ' + lineContent)
            line = line.replace('\n', '" ],' + '\n')
        
    return line

textLength = len(text)
i = 0
while i < textLength:
    # make it a tableentry
    text[i] = text[i].replace(text[i], createTableEntry(text[i]))
    i=i+1

file.writelines(text)

