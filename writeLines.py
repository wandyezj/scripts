def writeLines(file, lines):
    f = open(file, "w")
    data ="\n".join(lines)
    f.write(data)
    f.close()