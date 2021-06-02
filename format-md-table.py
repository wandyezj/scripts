# Format a markdown table

print("Format Table")


import sys


arguments = sys.argv[1:]

print(arguments)
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


data = read(file)

#print(data)

data = data.strip()
lines = data.split("\n")

# figure out longest lengths
longest_column = []

line_columns = []

for line in lines:
    columns = line.split("|")
    line_columns.append(columns)
    for i in range(len(columns)):
        column = columns[i].strip()

        while len(longest_column) <= i:
                   longest_column.append(0)

        column_length = len(column)

        if column_length >  longest_column[i]:
            longest_column[i] = column_length

print(longest_column)


# format each line
rows = []
for line in line_columns:
    row = []
    for i in range(len(line)):
        column = line[i].strip()
        size = longest_column[i]

        s = column + " " * (size -len(column))
        row.append(s)

    rows.append(row)


# join it all together
s = ""
for row in rows:
    s += "| ".join(row) + "\n"


print(s)




