import os
# os.system("ren mainn.py main.py")
with open("temp.py", 'w') as file:
    file.write("print('This is temp file created')\n")
    file.write("for i in range(10):\n")
    file.write("\tprint(f'{i} this is i = ')\n")

print("Running the created python file")
os.system("python temp.py")