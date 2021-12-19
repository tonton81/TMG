import sys
import shutil

found = False

with open("/data/openpilot/selfdrive/common/params.cc",'r') as f: # READ CURRENT FILE
    data = f.readlines()
    search = "{\"%s\", PERSISTENT}," % (sys.argv[1])
    for line in data:
        if search in line:
            found = True
            break

if found != True: #IF KEY DOESN'T EXIST, CREATE ENTRY
    with open("/data/openpilot/selfdrive/common/params.tmp",'w') as n: # WRITE TO TEMPORARY FILE
        with open("/data/openpilot/selfdrive/common/params.cc",'r') as f: # READ CURRENT FILE
            data = f.readlines()
            search = "{\"%s\", PERSISTENT}," % ("Version")
            for line in data:
                if search in line:
                    n.writelines(line)
                    n.writelines("    {\"%s\", PERSISTENT},\n" % (sys.argv[1]))
                    found = True
                    continue
                n.writelines(line)
        n.flush()
    shutil.move("/data/openpilot/selfdrive/common/params.tmp", "/data/openpilot/selfdrive/common/params.cc")
