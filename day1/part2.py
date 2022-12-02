from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()
    max_three = [0,0,0]
    curr = 0
    for line in lines:
        if line in ['\n', '\r\n']:
            min_val = min(max_three)
            if curr > min_val:
                max_three.remove(min_val)
                max_three.append(curr)
            curr = 0
        else:
            curr += int(line)
    if curr > min(max_three):
        max_three = curr
    print(reduce(lambda a, b: a + b, max_three))