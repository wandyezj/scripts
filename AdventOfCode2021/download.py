import urllib.request

def download_data(year, day, session):
    url = r'''https://adventofcode.com/{}/day/{}/input'''.format(year, day)
    print(url)

    opener = urllib.request.build_opener()
    opener.addheaders = [('cookie', 'session={}'.format(session))]
    response = opener.open(url)

    #print(response)

    data = response.read().decode('utf-8')

    #print(data)
    return data


def write_file(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()


import sys

def run():
    name, year, day, session = sys.argv

    if (year == None or day == None or session== None):
        print("usage: year day session")
        return

    print('''
    year: {}
    day: {}
    session: {}
    '''.format(year, day, session))

    data = download_data(year, str(int(day)), session)

    file = "{}.data.txt".format(str(int(day)).zfill(2))

    print()
    print(file)

    write_file(file, data)

run()
