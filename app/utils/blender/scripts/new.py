from sys import argv
from bpy import ops

ops.wm.save_as_mainfile(filepath=argv[3])