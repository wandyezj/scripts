
def readFileLines(file):
    f = open(file)
    data = f.read()
    f.close()
    lines = data.strip().split("\n")
    return lines

lines = readFileLines("02.data.txt")

#print(lines)

def fiveGroup(s):
    n = ""
    isFirst = True
    for i in range(len(s)):
        
        if i % 5 == 0 and i > 0:
            n += " "
        n += s[i]
        
    return n

def firstPolicy(composition, letter, minimum, maximum):
    letterCount = composition.count(letter)
    correctLetterCount = letterCount <= maximum and letterCount >= minimum
    
    return correctLetterCount


def inPosition(password, letter, index):
    composition = list(password)
    if index >= len(composition) or index < 0:
        return False

    item = composition[index]
    has = item == letter
    #print("\t" + str(index) + " " + letter + " " + str(has))
    return item == letter
    

def secondPolicy(password, letter, positionOne, positionTwo):
    #print("\t" + fiveGroup(password))
    composition = list(" " + password)

    a = inPosition(composition, letter, positionOne)
    b = inPosition(composition, letter, positionTwo)

    # in exactly one of the positions
    inExactlyOne = (a or b) and (not a or not b)
    #print("\t" + str(inExactlyOne))

    return inExactlyOne
    

def isValid(line, policy):
    pieces = line.split(":")
    password = pieces[1].strip()

    pieces = pieces[0].strip().split(" ")
    letter = pieces[1]
    pieces = pieces[0].split("-")
    first = int(pieces[0])
    second = int(pieces[1])

    valid = policy(password, letter, first, second)
    return valid

print("Part 1")
countValid = 0
for line in lines:
    if isValid(line, firstPolicy):
        #print("Valid " + line)
        countValid += 1

print(countValid)


print("Part 2")
countValid = 0
for line in lines:
    #print(line)
    if isValid(line, secondPolicy):
        #print("\tvalid")
        #print("\tValid " + line)
        countValid += 1

print(countValid)
