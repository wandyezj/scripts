import library as lib


def getInstruction(line):
    character = line[0]
    number = int(line[1:])
    return (character, number)

def getInstructions(data):
    lines = data.strip().split("\n")
    return list(map(getInstruction, lines))


INSTRUCTION_NORTH = 'N'
INSTRUCTION_SOUTH = 'S'
INSTRUCTION_EAST = 'E'
INSTRUCTION_WEST = 'W'

INSTRUCTION_RIGHT = 'R'
INSTRUCTION_LEFT = 'L'
INSTRUCTION_FORWARD = 'F'

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3

DIRECTIONS = [INSTRUCTION_EAST, INSTRUCTION_SOUTH, INSTRUCTION_WEST, INSTRUCTION_NORTH]
DIRECTION_NAMES = ["east", "south", "west", "north"]

DIRECTION_COUNT = len(DIRECTIONS)

def degreeToDirection(degree):
    index = (degree %360) // 90
    direction = DIRECTIONS[index]
    return direction


def partOne(instructions):
    north = 0
    south = 0
    east = 0
    west = 0

    degrees = 0

    for instruction, number in instructions:

        direction = instruction

        if instruction == INSTRUCTION_FORWARD:
            direction = degreeToDirection(degrees)

        if direction == INSTRUCTION_RIGHT:
            degrees += number
        elif direction == INSTRUCTION_LEFT:
            degrees -= number
        elif direction == INSTRUCTION_NORTH:
            north += number
        elif direction == INSTRUCTION_SOUTH:
            south += number
        elif direction == INSTRUCTION_EAST:
            east += number
        elif direction == INSTRUCTION_WEST:
            west += number
        else:
            print("unrecognized instruction")

    print('''
    north {}
    south {}
    east {}
    west {}
    '''.format(north, south, east, west))

    total_east = east - west
    total_north = north - south

    manhattan_distance = abs(total_east) + abs(total_north)
    return manhattan_distance


def partTwoFail(instructions):

    ship = [0, 0, 0, 0]
    waypoint = [0, 0, 0, 0]

    waypoint_direction = 0

    for instruction, number in instructions:

        if instruction == INSTRUCTION_FORWARD:
            
            # add waypoint * number to ship
            for i in range(DIRECTION_COUNT):
                d = (i + waypoint_direction) % DIRECTION_COUNT
                ship[i] += waypoint[d] * number

        elif instruction == INSTRUCTION_RIGHT:
            waypoint_direction += number // 90 + DIRECTION_COUNT
        elif instruction == INSTRUCTION_LEFT:
            waypoint_direction +=  DIRECTION_COUNT - number // 90

        elif instruction in DIRECTIONS:
            index = (DIRECTIONS.index(instruction) + waypoint_direction) % len(DIRECTIONS)
            waypoint[index] += number
        else:
            print("unrecognized instruction")

    north = ship[NORTH]
    south = ship[SOUTH]
    east = ship[EAST]
    west = ship[WEST]

    print('''
    north {}
    south {}
    east {}
    west {}
    '''.format(north, south, east, west))

    total_east = east - west
    total_north = north - south

    manhattan_distance = abs(total_east) + abs(total_north)
    return manhattan_distance

def degreesToDirectionIndex(degrees):
    return ((degrees %360 + 360) // 90) % DIRECTION_COUNT

def partTwo(instructions):

    # x = east+ west- 
    # y = north+ south-

    waypoint_east = 10
    waypoint_north = 1

    ship_east = 0
    ship_north = 0


    waypoint_direction = 0

    for instruction, number in instructions:
        #print("\t", "north", ship_north, "east", ship_east)

        print(instruction, number)
        print("\t", "before")
        print("\t", "waypoint", waypoint_north, waypoint_east, waypoint_direction)
        print("\t", "ship", ship_north, ship_east)
        #print(ship_north, ship_east, waypoint_east, waypoint_north, instruction, number)

        if instruction == INSTRUCTION_FORWARD:

            direction = degreesToDirectionIndex(waypoint_direction)
            print("\tforward", waypoint_direction, direction, DIRECTION_NAMES[direction])
            change_east = 0
            change_north = 0

           
            # add waypoint * number to ship
            if direction == EAST:
                # east -> east
                # nort -> north
                change_east += waypoint_east
                change_north += waypoint_north

            elif direction == SOUTH:
                # rotate 1
                # north -> east
                # east -> south
                change_east += waypoint_north
                change_north -= waypoint_east

            elif direction == WEST:
                # rotate 2
                # east -> west
                # north -> south
                change_east -= waypoint_east
                change_north -= waypoint_north

            elif direction == NORTH:
                # east -> north
                # north -> west
                change_east -= waypoint_north
                change_north += waypoint_east

            delta_east = change_east * number
            delta_north = change_north * number

            print("\t", delta_east, delta_north)
            ship_east += delta_east
            ship_north += delta_north


        elif instruction == INSTRUCTION_RIGHT:
            waypoint_direction += number
        elif instruction == INSTRUCTION_LEFT:
            waypoint_direction -= number

        elif instruction == INSTRUCTION_NORTH:
            waypoint_north += number
        elif instruction == INSTRUCTION_SOUTH:
            waypoint_north -= number
        elif instruction == INSTRUCTION_EAST:
            waypoint_east += number
        elif instruction == INSTRUCTION_WEST:
            waypoint_east -= number
        else:
            print("unrecognized instruction")

        print("\t", "after")
        print("\t", "waypoint", waypoint_north, waypoint_east, waypoint_direction)
        print("\t", "ship", ship_north, ship_east)
        #print("\t", ship_north, ship_east)
        

    print('''
    north {}
    east {}
    '''.format(ship_north, ship_east))

    manhattan_distance = lib.manhattenDistance(ship_north, ship_east)
    return manhattan_distance


dataSmall = '''F10
N3
F7
R90
F11'''


file = lib.defaultInputFile(__file__)
data = lib.readFile(file)


instructions = getInstructions(data)
#print(instructions)
print("Part 1")
value = partOne(instructions)
print(value)


print("Part 2")
value = partTwo(instructions)
print(value)

# 14074 ?
# 31118 low
# 66730  - NO
# 92667 high
# 103786 high
# 131167 high


 # https://github.com/kodsnack/advent_of_code_2020/blob/main/estomagordo-python3/12b.py
def solve(lines):
    wayy = 1
    wayx = 10
    y = 0
    x = 0

    for instruction in lines:
        command = instruction[0]
        val = int(instruction[1:])

        if command == 'N':
            wayy += val
        if command == 'S':
            wayy -= val
        if command == 'E':
            wayx += val
        if command == 'W':
            wayx -= val
        if command == 'L':
            if val == 90:
                wayy, wayx = wayx, wayy * -1
            if val == 180:
                wayy, wayx = wayy * -1, wayx * -1
            if val == 270:
                wayy, wayx = wayx * -1, wayy
        if command == 'R':
            if val == 90:
                wayy, wayx = wayx * -1, wayy
            if val == 180:
                wayy, wayx = wayy * -1, wayx * -1
            if val == 270:
                wayy, wayx = wayx, wayy * -1
        if command == 'F':
            y += val * wayy
            x += val * wayx
    
    return lib.manhattenDistance(x,y)

print(solve(lib.readFileLines(file)))

# above is much more elegant
# lesson is to keep it simple and the angles can be kept in values in terms of + and -
# also translating in th x and y over NSEW is much easier to visualize