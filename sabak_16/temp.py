print('This is temp file created')
for i in range(10):
	print(f'{i} this is i = ')


import platform
import sys

print(platform.system())
print(platform.version)
print(platform.release())


if platform.system() == "Windows":
	print("This is running windows")
	import subprocess
	subprocess.run("dir", shell=True)
elif platform.system() =='Linux':
	import subprocess
	print("This is running on linux")
	subprocess.run("ls", shell=True)
else:
	print("Sth is wrong")

print(sys.version)
print(sys.platform)
print(sys.argv)
print(sys.exit())