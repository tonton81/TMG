import sys

with open("/data/TMG/keylist", "r") as file:
    keys = str(file.readline())
    print(keys)

    search = "\"%s\"" % (sys.argv[1])
    if search not in keys:
        append = "\"%s\"" % (sys.argv[1])
        keys = keys.strip() + " " + append.strip()
        with open("/data/TMG/keylist", "w") as keylist:
            keylist.write(keys)
