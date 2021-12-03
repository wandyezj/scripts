

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
        'py',
        'reflect.md'
    ]

    for postfix in files:
        name = prefix + "." + postfix

        # don't overwrite files that already exist
        if not os.path.exists(name):
            write_file(name,"")
        else:
            print("{:<20} - already exists!".format(name))

run()