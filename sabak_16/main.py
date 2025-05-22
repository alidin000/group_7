# import os = > operating system
import os
print(os.getcwd())
print(os.chdir("."))
import shutil
if os.path.exists("notes"):
    print("I am removing")
    # os.rmdir("python")
    shutil.rmtree("notes")

os.makedirs("notes\\python")
with open("notes\\python\\main.txt","w") as file:
    for i in range(10):
        file.write(f"{i} Hello world \n")


# os.environ  environment 
os.system("cls")
# print(os.environ)
print(os.environ['c#'])
print(os.environ['path'])
print(type(os.environ))
# print(os.environ['python'])

# data = > password, api key

os.environ['api_key'] = '1243124df'
api_key = os.environ['api_key']
print(f" api_key = {api_key}")



