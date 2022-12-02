with open('input.txt') as f:
    lines = f.readlines()
    max = 0
    curr = 0
    for line in lines:
        if line in ['\n', '\r\n']:
            if curr > max:
                max = curr
            curr = 0
        else:
            curr += int(line)
    if curr > max:
        max = curr
    print(max)