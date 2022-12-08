root = {
    'name': '/',
    'children': [],
    'files': [],
    'size': 0,
    'parent': None
}

dirSizes = {}
pointer = root

def processLine(line):
    if line[0] == "$":
        processCommand(line)
    else:
        processResponse(line)

def findChildByName(children, name):
    for child in children:
        if child['name'] == name:
            return child
    return None

def findFileByName(children, name):
    for child in children:
        if child == name:
            return child
    return None

def processCommand(line):
    global pointer
    global root
    command = line.replace("$ ", "")
    if command[:2] == "cd":
        toDir = command[3:]
        if toDir == '..':
            pointer = pointer['parent']
        elif toDir == '/':
            pointer = root
        elif findChildByName(pointer['children'], toDir) != None:
            pointer = findChildByName(pointer['children'], toDir)
        else:
            newDir = {
                'name': toDir,
                'children': [],
                'files': [],
                'size': 0,
                'parent': pointer
            }
            pointer['children'].append(newDir)
            pointer = newDir
            dirSizes[dirhashname(newDir, '')] = 0

def dirhashname(dir, name):
    name = name + "_" + dir['name']
    if dir['parent'] == None:
        return name
    return dirhashname(dir['parent'], name)

def processResponse(line):
    global pointer
    parts = line.split(" ")
    if parts[0] == 'dir':
        if findChildByName(pointer['children'], parts[1]) == None:
            newDir = {
                'name': parts[1],
                'children': [],
                'files': [],
                'size': 0,
                'parent': pointer
            }
            pointer['children'].append(newDir)
            dirSizes[dirhashname(newDir, '')] = 0
    else:
        if findFileByName(pointer['files'], parts[1]) == None:
            pointer['size'] += int(parts[0])
            pointer['files'].append(parts[1])
            dirSizes[dirhashname(pointer, '')] = pointer['size']
            updateParentSize(pointer, int(parts[0]))

def updateParentSize(curr, size):
    if curr['parent']:
        parent = curr['parent']
        parent['size'] += size
        dirSizes[dirhashname(parent, '')] = parent['size']
        updateParentSize(parent, size)

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        processLine(line.strip())
    unused = 70000000 - dirSizes['_/']
    needToFree = 30000000 - unused
    currToDelete = None
    for key, value in dirSizes.items():
        if value > needToFree and (currToDelete == None or currToDelete > value):
            currToDelete = value
    print(currToDelete)