

import sys

import os

def write_file(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()

def data_py(number):
    return '''
number = "{}"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

lines = read_file(file_sample)


print("")
print("Part 1")


print("")
print("Part 2")


'''.format(number)

def data_learn():
    return '''# Reflect

'''

def run():
    name, day= sys.argv

    prefix = day.zfill(2)

    files = [
        'data.sample.txt',
        'data.txt',
        'puzzle.txt',
        
    ]

    for postfix in files:
        name = prefix + "." + postfix

        # don't overwrite files that already exist
        if not os.path.exists(name):
            write_file(name,"")
        else:
            print("{:<20} - already exists!".format(name))

    files = [
        ("py", data_py(prefix)),
        ('learn.md',data_learn())

    ]
    for postfix, data in files:
        name = prefix + "." + postfix

        # don't overwrite files that already exist
        if not os.path.exists(name):
            write_file(name,data)
        else:
            print("{:<20} - already exists!".format(name))





run()