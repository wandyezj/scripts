

import sys

import os

def write_file(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()

def run():
    name, day= sys.argv

    prefix = day.zfill(2)

    files=[
        'data.sample.txt',
        'data.txt',
        'puzzle.txt',
        'reflect.md'
    ]

    for postfix in files:
        name = prefix + "." + postfix

        # don't overwrite files that already exist
        if not os.path.exists(name):
            write_file(name,"")
        else:
            print("{:<20} - already exists!".format(name))

    postfix = "py"
    name = prefix + "." + postfix

    if not os.path.exists(name):
        write_file(name, '''
number = "{}"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file_lines(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip().split("\\n")

lines = read_file_lines(file_sample)



print("Part 1")



print("Part 2")


'''.format(prefix))

run()