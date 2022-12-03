map = {
    "a":
}

with open('input.txt') as f:
    lines = f.readlines()
    dups = []
    for line in lines:
        mid = len(line)/2 -1 
        firstLetters = line[:mid].split("")
        second = line [mid:]
        for letter in firstLetters:
            if letter in second:
                dups.append(letter)
    
