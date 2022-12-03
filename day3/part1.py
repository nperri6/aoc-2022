
from functools import reduce
from math import floor

def convertToNum(letter):
    if (letter == letter.upper()):
        return ord(letter) - 38
    else:
        return ord(letter) - 96


with open('input.txt') as f:
    lines = f.readlines()
    dups = []
    for line in lines:
        mid = floor(len(line)/2)
        firstLetters = list(line[:mid])
        second = line [mid:]
        for letter in firstLetters:
            if letter in second:
                dups.append(letter)
                break
    mappedValues = map(convertToNum, dups )
    print(reduce(lambda a, b: a + b, mappedValues))
    