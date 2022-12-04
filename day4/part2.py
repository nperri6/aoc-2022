# refactored version of similar logic in part 1
with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        parts = line.split(",")
        [s1, e1] = parts[0].strip().split("-")
        [s2, e2] = parts[1].strip().split("-")
        if (int(s1) <= int(e2) and int(s2) <= int(e1)):
            count += 1
    print(count)

