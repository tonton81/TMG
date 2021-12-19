from subprocess import Popen
from subprocess import call
call(['python', '/data/TMG/controls_h.patch'])
call(['python', '/data/TMG/settings_cc.patch'])


from pathlib import Path
my_file = Path("/data/TMG/keylist")
if my_file.is_file():
    pass
else:
    with open("/data/TMG/keylist", 'w') as fp:
        pass
