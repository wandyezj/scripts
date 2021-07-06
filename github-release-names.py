print("GitHub release tags")
# gh release --repo <x> list --limit 1000

import sys


arguments = sys.argv[1:]

print("arguments: {}".format(arguments))
if len(arguments) == 1:
    file = arguments[0]
else:
    file ="temp/releases.data.txt"
    
print("file: [{}]".format(file))

def read(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

print()

lines = read(file).strip().split("\n")

tags = []
for line in lines:
    halves = line.split("(")
    if len(halves) != 2:
        print("skip: " + line)
        continue
    
    halves = halves[-1].split(")")
    if len(halves) != 2:
        print("skip: " + line)
        continue

    tag = halves[0]
    print(tag) 
    tags.append(tag)


print()

print("formatted remove commands:\n\n")

for tag in tags:
    print("%gh% release --repo %repo% delete {} --yes".format(tag))


