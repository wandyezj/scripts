def readLines(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip().split("\n")
