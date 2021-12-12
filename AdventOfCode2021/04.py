
number = "04"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"


def read_file_lines(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip().split("\n")

lines = read_file_lines(file)

to_numbers = lambda x: int(x)

numbers = lines.pop(0).strip().split(",")

# only check rows or columns

boards = []

board = []
for line in lines:
    line = line.strip()
    if line:
        board.append(line.split())
    
    if len(board) == 5:
        boards.append(board)
        board = []

def bingo(board, called):

    # rows
    for row in board:
        count = 0
        for n in row:
            if n in called:
                count +=1

        if count == 5:
            return True


    # columns
    for i in range(5):
        count = 0
        for row in board:
            if row[i] in called:
                count +=1
        if count == 5:
            return True

def unmarked_numbers(board, called):
    unmarked = []
    for row in board:
        for col in row:
            if not col in called:
                unmarked.append(col)
    return unmarked

print("")
print("Part 1")

def winning_board_and_number(boards, numbers):

    called = []
    for n in numbers:
        called.append(n)
        for board in boards:
            if bingo(board, called):
                return (board, called)

board, called = winning_board_and_number(boards, numbers)
win = called[-1]
unmarked = unmarked_numbers(board, called)

print(sum(map(to_numbers, unmarked)) * int(win))



print("")
print("Part 2")

def last_winning_board_and_number(boards, numbers):

    winning_boards = []
    called = []
    for n in numbers:
        called.append(n)
        for i in range(len(boards)):
            if i in winning_boards:
                continue

            board = boards[i]

            if bingo(board, called):
                winning_boards.append(i)

        if len(boards) == len(winning_boards):
            return (boards[winning_boards[-1]], called)


board, called = last_winning_board_and_number(boards, numbers)
win = called[-1]
unmarked = unmarked_numbers(board, called)

print(sum(map(to_numbers, unmarked)) * int(win))