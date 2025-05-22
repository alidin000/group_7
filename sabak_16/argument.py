import sys


file_name = sys.argv[0]
if len(sys.argv) > 1:
    argument_name = sys.argv[1]
    print("Bul filedyn aty", file_name)
    import os
    if os.path.exists(argument_name):
        print("Bar eken")
    else:
        print("Jok eken")
else:
    print("Bizge argument berbedin!!!!")