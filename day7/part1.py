root = {
    'name': '/',
    'children': [],
    'files': [],
    'size': 0,
    'parent': None
}

smallDirs = [root]

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
            smallDirs.append(newDir)      

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
            smallDirs.append(newDir)
    else:
        if findFileByName(pointer['files'], parts[1]) == None:
            pointer['size'] += int(parts[0])
            pointer['files'].append(parts[1])
            if pointer['size'] > 100000 and pointer in smallDirs:
                    smallDirs.remove(pointer)
            updateParentSize(pointer, int(parts[0]))

def updateParentSize(curr, size):
    if curr['parent']:
        parent = curr['parent']
        parent['size'] += size
        if (parent['size']) > 100000 and parent in smallDirs:
            smallDirs.remove(parent)
        updateParentSize(parent, size)

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        processLine(line.strip())
    total = 0
    for dir in smallDirs:
        total+= dir['size']
    print(total)