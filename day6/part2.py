with open('input.txt') as f:
    last = []
    lines = f.readlines()
    for line in lines:
        chars = list(line)
        for idx, char in enumerate(chars):
            if len(last) < 14:   
                last.append(char)
            else:
                st = set(last)
                if len(st) == 14:
                    print(idx)
                    break
                else:
                    last.append(char)
                    last = last[1:]