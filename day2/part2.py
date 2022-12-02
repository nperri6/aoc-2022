
values = {
    "A": 1,
    "B": 2,
    "C": 3
}

def calcMove(plays):
    if plays[1] == "X":
        match plays[0]:
            case "A":
                return 3
            case "B":
                return 1
            case "C":
                return 2
    elif plays[1] == "Y":
        match plays[0]:
            case "A":
                return 4
            case "B":
                return 5
            case "C":
                return 6
    elif plays[1] == "Z":
        match plays[0]:
            case "A":
                return 8
            case "B":
                return 9
            case "C":
                return 7

def score_line(line):
    plays = line.split()
    return calcMove(plays)

with open('input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        total += score_line(line)
    print(str(total))