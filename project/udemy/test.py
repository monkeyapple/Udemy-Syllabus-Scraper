import os
import sys

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

# from UdemyAPI import udemy
# try:
#     Client=PyUdemy()
# except:
#     pass
# else:
#     print('work well')
