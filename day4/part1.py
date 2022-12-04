with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        parts = line.split(",")
        s1 = 0
        e1 = 0
        s2 = 0
        e2 = 0
        for idx, part in enumerate(parts):
            split = part.split("-")
            if idx == 0:
                s1 = int(split[0])
                e1 = int(split[1])
            else:
                s2 = int(split[0])
                e2 = int(split[1])
        if (s1 <= s2 and e1 >= e2):
            count += 1 
        elif (s2 <= s1 and e2 >= e1):
            count += 1
    print(count)

