# directory => папка
# import os => operating system
import os

print(os)
# path -> дорога / location =>локация 
print(os.path)
print(os.path.exists("C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_15"))
print(os.path.exists("C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_16"))
print(os.path.exists("C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_15\\directory"))
print(os.path.exists("C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_15\\main.py"))

# . -> current directory = учурдагы папка
# .. -> root directory => бир жогору = parent directory
# print(os.path.exists("temp.txt"))
# if False:
#     print("hello world")

if not os.path.exists("temp.txt"):# not False = True
    ff = open("temp.txt","w")
    ff.close()

f = open("temp.txt",'r')
f.close()

# mkdir => make directory => папка жасоо
if not os.path.exists("directory_3"):
    os.mkdir("directory_3")
print("Текшеруу:")
print(os.path.exists("directory_3"))

print("Check")
print(os.getcwd()) # get current directory
# os.getcwd()
# special characters => \n \t   
file_name = os.getcwd() + "\\temp_2.txt"

print(f"file_name = {file_name}")

tt = os.getcwd() + "\yellow.txt"

ff = open(tt,"w")

# C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_15\\main.py

ttt = open("temppp.py","w")
ttt.write("print('Hello world')")

# cd = > change directory

os.chdir("..")
print(f" check {os.getcwd()}")
# os.chdir()
os.chdir("C:\\Users\\user\\Desktop\\Motion web")
print(f" check {os.getcwd()}")
if not os.path.exists("group_8"):
    os.mkdir("group_8")
print(f" Does it exist ?: {os.path.exists("C:\\Users\\user\\Desktop\\Motion web\\group_8")}")
os.chdir("C:\\Users\\user\\Desktop\\Motion web\\group_8")
print(f" is it group_8 directory?: {os.getcwd()}")
# if os.getcwd() == "C:\\Users\\user\\Desktop\\Motion web\\group_8":
#     python = open("main.py",'w')
#     python.write("import random\n")
#     python.write("print(random.randint(1,2))\n")

os.chdir("C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_15")

list_of_content = os.listdir()
print(f" current files and folders: {list_of_content}")

# import random
# random.randint()

# 
print("____________________________________________")
os.chdir("C:\\Users\\user\\Desktop\\Motion web\\group_7")
tabyldy = False
for d in os.listdir():
    # if d in ["sabak_1","sabak_2", "sabak_3"]:
    if d in {"sabak_15","sabak_2", "sabak_3"}:
        print("Табылды")
        tabyldy = True
if not tabyldy:
    print("табылбады")

print(os.listdir())

# 
print("_+_+_+_+_+_+_+_")
for dd in os.listdir():
    if os.path.isdir(dd):
        print("Bul papka", dd)
    if os.path.isfile(dd):
        print("Bul file", dd)

# os.mkdir('group_8')
os.rmdir("C:\\Users\\user\\Desktop\\Motion web\\group_8") # remove directory
print("очтубу?")
print(os.path.exists("C:\\Users\\user\\Desktop\\Motion web\\group_8"))
# import shutil
# shutil.rmtree("C:\\Users\\user\\Desktop\\Motion web\\group_9") # remove directory
# print(os.path.exists("C:\\Users\\user\\Desktop\\Motion web\\group_9"))

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
for root, dir, file in os.walk("C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_15"):
    print(f"root {root}")
    print(f"directory {dir}")
    print(f"file {file}")