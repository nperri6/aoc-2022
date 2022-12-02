
values = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def calcWin(plays):
    if plays[0] == "A":
        match plays[1]:
            case "X":
                return 3
            case "Y":
                return 6
            case "Z":
                return 0
    elif plays[0] == "B":
        match plays[1]:
            case "X":
                return 0
            case "Y":
                return 3
            case "Z":
                return 6
    elif plays[0] == "C":
        match plays[1]:
            case "X":
                return 6
            case "Y":
                return 0
            case "Z":
                return 3


def score_line(line):
    plays = line.split()
    return values[plays[1]] + calcWin(plays)

with open('input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        total += score_line(line)
    print(str(total))