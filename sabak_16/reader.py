import os
import sys

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if os.path.exists(arg):
        with open(arg,'r') as file:
            print(arg)
            content = file.read()
            print(content)