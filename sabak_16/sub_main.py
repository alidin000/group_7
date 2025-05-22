import subprocess

# subprocess.run("mkdir temppp", shell= True)
output = subprocess.check_output("python temp.py")
print(output.decode('utf-8'))
print(type(output))

# 'w' >
# 'a' >>