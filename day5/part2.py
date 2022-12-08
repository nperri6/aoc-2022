rows = []
processingStacks = True
transformed = []

with open('input.txt') as f:
    lines = f.readlines()
    for rowNum, line in enumerate(lines):
        if len(line) > 1 and line[1] == "1":
            processingStacks = False
            # this seems like an easy numpy transformation
            for i, r in enumerate(rows):

                for j, v in enumerate(r):
                    if len(transformed) <= j:
                        transformed.append([])
                    if (v != " "):
                        transformed[j].insert(0,v)

        if processingStacks:
            chars = list(line)
            for idx, char in enumerate(chars):
                if (idx -1) % 4 == 0:
                    if (rowNum > len(rows) - 1):
                        rows.append([])
                    rows[rowNum].append(char)
        elif line[0] == "m":
            line = line.replace("move ", "")
            line = line.replace(" from ", ",")
            line = line.replace(" to ", ",")
            directions = line.split(",")
            val = transformed[int(directions[1])-1][-1*int(directions[0]):]
            transformed[int(directions[1])-1] = transformed[int(directions[1])-1][:-1*int(directions[0])]
            transformed[int(directions[2])-1] += val
    st = ''
    for t in transformed:
        st += t[-1]
    print(st)
