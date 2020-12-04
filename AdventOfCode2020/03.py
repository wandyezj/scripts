def readFileLines(file):
    f = open(file)
    data = f.read()
    f.close()
    lines = data.strip().split("\n")
    return lines

lines = readFileLines("03.input.txt")

size = len(lines[0])

slope = "".join(lines)


def numberOfTreesEncountered(slope, size, right, down):

    modified = list(slope)


    trees = 0

    TREE = '#'
    ENCOUNTER_TREE = 'X'
    ENCOUNTER_EMPTY = 'O'

    position_down = 0
    position_right = 0
    position = 0

    while position < len(slope):
        c = slope[position]

        modified[position] = ENCOUNTER_EMPTY
        if c == TREE:
            trees += 1
            modified[position] = ENCOUNTER_TREE

        # go down a certain number
        # go across a certain number and wrap
        position_down += down * size
        position_right = (position_right + right)% size
        
        position = position_down + position_right

        

    # Debug
    #modified = "".join(modified)
    #for i in range(len(lines)):
    #    print(modified[i*size: (i+1) * size])

    return trees;


print("Part 1")
right = 3
down = 1
trees = numberOfTreesEncountered(slope, size, right, down)

print("trees")
print(trees)


print("Part 2")

'''
Right 1, down 1.
Right 3, down 1.
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
'''

angles = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees = 1;
for right, down in angles:
    #right = angle[0]
    #down = angle[1]
    print('{} {}'.format(right, down))

    trees *= numberOfTreesEncountered(slope, size, right, down)

print("trees")
print(trees)


