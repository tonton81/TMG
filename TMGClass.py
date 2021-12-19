from subprocess import Popen
from subprocess import call
from common.params import Params
params = Params()

class TMGClass:
#  def __init__(self):

  def get(self, key, value, isDynamic = False): # Dynamic capability example: steerRatio
    try: # if key exists, send the value
      if params.get_bool(key + "_dynamic"):
          return value
      else:
          return eval(params.get(key))

    except: # if key doesn't exist, create it and send back original value. Also create a default file for it.
      try:
        params.put(key, str(value))
        params.put(key + "_default", str(value))
        if isDynamic:
            params.put_bool(key + "_dynamic", True)

      except:
        pass

      call(['python', '/data/TMG/params_add.py', key]) # add key to params
      call(['python', '/data/TMG/params_add.py', key + "_default"]) # add key to params
      call(['python', '/data/TMG/params_add.py', key + "_dynamic"]) # add key to params
      call(['python', '/data/TMG/keylist_add.py', key]) # add key to GUI
      return value
