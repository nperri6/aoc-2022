
from functools import reduce

def convertToNum(letter):
    if (letter == letter.upper()):
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def determineDup(currLines):
    firstLetters = list(currLines[0])
    for letter in firstLetters:
        if letter in currLines[1] and letter in currLines[2]:
            return letter

with open('input.txt') as f:
    lines = f.readlines()
    dups = []
    currLines = []
    for idx, line in enumerate(lines):
        if idx > 0 and idx % 3 == 0:
            dups.append(determineDup(currLines))
            currLines = [line]
        else:
            currLines.append(line)
    dups.append(determineDup(currLines))
    mappedValues = map(convertToNum, dups )
    print(reduce(lambda a, b: a + b, mappedValues))
    