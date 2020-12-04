
def readFileLines(file):
    f = open(file);
    data = f.read().strip()
    f.close()
    return data.split("\n")


lines = readFileLines("02.data.txt")


partOneCount = 0
partTwoCount = 0
#go through each line
for line in lines:
    
    # a b letter password
    # a-b letter: password

    pieces = line.split(": ")
    password = pieces[1].strip()

    pieces = pieces[0].split(" ")
    letter = pieces[1].strip()

    pieces = pieces[0].split("-")
    a = int(pieces[0])
    b = int(pieces[1])

    #print("{} {} {} {}".format(a, b, letter, password))
    
    
    # part 1
    # count how many of the letter is in the password
    letterCount = password.count(letter)
    # test against a and b

    if letterCount >= a and letterCount <= b:
        partOneCount += 1
    

    # part 2
    # test for letters presence at a and b using one based index
    password = " " + password

    one = password[a] == letter
    two = password[b] == letter

    if one ^ two:
        partTwoCount += 1

    # count the number that pass


print("Part 1")
print(partOneCount)
print("Part 2")
print(partTwoCount)
