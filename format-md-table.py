# Format a markdown table

print("Format Table")


import sys


arguments = sys.argv[1:]

print("arguments: {}".format(arguments))
if len(arguments) == 1:
    file = arguments[0]
else:
    file ="temp/data.txt"
    
print("file: [{}]".format(file))

def read(file):
    f = open(file)
    data = f.read()
    f.close()
    return data


#print(data)

def tableRowCol(data):
    lines = data.strip().split("\n")
    rows = []
    for line in lines:
        row = []
        cols = line.split("|")
        for col in cols:
            row.append(col.strip())
        rows.append(row)
    return rows


def orderTableCol(row_col, order):
    new_row_col = []

    for row in row_col:
        new_row = []
        for i in order:
            col = row[i]
            new_row.append(col)
        new_row_col.append(new_row)

    return new_row_col
    

def formatTable(row_col):
    # figure out longest lengths
    longest_column = []


    for row in row_col:
        columns = row
        for i in range(len(columns)):
            column = columns[i].strip()

            while len(longest_column) <= i:
                       longest_column.append(0)

            column_length = len(column)

            if column_length >  longest_column[i]:
                longest_column[i] = column_length

    #print(longest_column)


    # format each line
    rows = []
    for cols in row_col:
        row = []
        for i in range(len(cols)):
            column = cols[i]
            size = longest_column[i]

            s = column + " " * (size - len(column))
            row.append(s)

        rows.append(row)


    # join it all together
    s = ""
    for row in rows:
        #print(row)
        s += "| ".join(row) + "\n"


    return s



data = read(file)

#print("data")
#print(data)
row_col = tableRowCol(data)

#print("row_col")
#print(row_col)

print(formatTable(row_col))

# reorder
order = [0,1,2,3,4,5,6]
order = [0,1,3,4,5,2,6,7,8]
# will fail if not everything has the same number of columns
row_col = orderTableCol(row_col, order)

#print()
print("Format Table")
print("\n\n\n")
s = formatTable(row_col)
print(s)





