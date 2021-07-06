print("Template Command")

import sys


arguments = sys.argv[1:]

# default arguments
file = "temp/items.data.txt"
out = "temp/commands.cmd"


print("arguments: {}".format(arguments))
if len(arguments) >= 1:
    file = arguments[0]

if len(arguments) >= 2:
    out = arguments[1]

if len(arguments) > 2:
    raise "invalid number of arguments"
    
    
print("file: [{}]".format(file))

def read(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

def writeLines(file, lines):
    f = open(file, "w")
    data ="\n".join(lines)
    f.write(data)
    f.close()

lines = read(file).strip().split("\n")
print("\n\n\n")

commands = []
for line in lines:
    item = line.strip()
    if not "-" in item:
        continue
    command = "git push --delete origin {}".format(item)
    #"git tag -d {}".format(item)
    commands.append(command)
    print(command)

# optional
#commands.sort()

writeLines(out, commands)
