def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

def createLines(data):
    return data.strip().split("\n")

def readFileLines(file):
    data = readFile(file)
    return createLines(data)

def createNumberList(data):
    lines = createLines(data)
    return list(map(int, lines))

def readFileNumberList(file):
    data = readFile(file)
    return createNumberList(data)

def createGrid(data):
    lines = createLines(data)
    grid = list(map(list, lines))
    return grid

def readFileGrid(file):
    data = readFile(file)
    return createGrid(data)


def defaultInputFile(file):
    '''
    [row][column]
    '''
    number = file.split(".")[-2]
    return number + ".input.txt"

def manhattenDistance(x, y):
    return abs(x) + abs(y)