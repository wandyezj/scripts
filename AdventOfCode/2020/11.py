import library as lib


SEAT_OCCUPIED = "#"
SEAT_EMPTY = "L"

# reduce grid to easy seat lookup
# its actually more efficient to simply surround by a border of 1
def seatMap(grid):
    seats = {}
    maxRow = len(grid)
    maxColumn = len(grid[0])
    r = 0
    for row in grid:
        c = 0
        seats[r] = {}
        for item in row:
            if item == SEAT_EMPTY:
                seats[r][c] = False
            elif item == SEAT_OCCUPIED:
                seats[r][c] = True
            c +=1
        r +=1
    return seats, maxRow, maxColumn

directions = [
    (0, 1, "right"),

    (-1, -1, "up left"),
    (-1, 0, "up"),
    (-1, 1, "up right"),
    (0, -1, "left"),

    (1, -1, "down left"),
    (1, 0, "down"),
    (1, 1, "down right"),
]

# next change for the seat
def seatChange(row, column, maxRow, maxColumn, seats):

    occupied = 0
    for rOffset,cOffset, direction in directions:
        r = row + rOffset
        c = column + cOffset
        if r in seats and c in seats[r] and seats[r][c]:
            occupied += 1

    state = seats[row][column]
    if state:
        if occupied >= 4:
            return False
    else:
        if occupied == 0:
            return True
    
    return state

def inBounds(n, minimum, maximum):
    return n >= minimum and n < maximum

def seatsSeenToBeOccupiedFromSeat(row, column, maxRow, maxColumn, seats):
    occupied = 0

    rMin = 0
    rMax = maxRow
    cMin = 0
    cMax = maxColumn
    for rOffset,cOffset,d in directions:
        r = row
        c = column

        while True: 
            r += rOffset
            c += cOffset
            if not inBounds(r, rMin, rMax):
                break
            if not inBounds(c, cMin, cMax):
                break
            if r in seats and c in seats[r]:
                break

        if inBounds(r, rMin, rMax) and inBounds(c, cMin, cMax):
            o = seats[r][c]
            if o:
                occupied += 1
    return occupied

def seatChangeSearch(row, column, maxRow, maxColumn, seats):

    occupied = seatsSeenToBeOccupiedFromSeat(row, column, maxRow, maxColumn, seats)
    state = seats[row][column]
    if state:
        if occupied >= 5:
            return False
    else:
        if occupied == 0:
            return True
    
    return state


def seatsOccupied(seats):
    count = 0
    for r, row in seats.items():
        for c, occupied in row.items():
            if occupied:
                count += 1
    return count

def nextChange(seats, maxRow, maxColumn, seatChange):
    new = {}
    changed = False
    for r, row in seats.items():
        new[r] = {}
        for c, occupied in row.items():
            before = occupied
            after = seatChange(r, c, maxRow, maxColumn, seats)
            if before != after:
                changed = True
            new[r][c] = after
    
    return (changed, new)

def runChangesUntilStill(seats, maxRow, maxColumn, seatChange):
    # until no seats change state
    changed, seats = nextChange(seats, maxRow, maxColumn, seatChange)
    while changed:
        #print("change")
        changed, seats = nextChange(seats, maxRow, maxColumn, seatChange)

    return seats



def createSeats(s):
    grid = lib.createGrid(s)
    seats = seatMap(grid)
    return seats

def test():
    s = '''
.##.##.
#.#.#.#
##...##
...L..#
##...##
#.#.#.#
.##.##.
'''.strip()

    seats = createSeats(s)
    count = seatsSeenToBeOccupiedFromSeat(3,3,seats)
    print("Test")
    print(count)



#test()

read = lib.defaultInputFile(__file__)
grid = lib.readFileGrid(read)
originalSeats, maxRow, maxColumn = seatMap(grid)

seats = runChangesUntilStill(originalSeats, maxRow, maxColumn, seatChange)
count = seatsOccupied(seats)
print("Part 1")
print(count)

seats = runChangesUntilStill(originalSeats, maxRow, maxColumn, seatChangeSearch)
count = seatsOccupied(seats)
print("Part 2")
print(count)

# This solution is absolutely disgusting
# Would have been easier to implement with TypeScript