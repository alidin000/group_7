x = 10 # integer
name = "Alidin" # str
salmak = 10.6 # float
is_student = False # bool

if x >= 9:
    print("Eki oruduu sandar")
elif x == 10:
    print("x == 10")
else:
    print("else")


for i in range(1,10):
    print(i)
for i in range(1,10):
    if i == 5:
        continue
    print(f"i={i}")

for i in range(1,10):
    if i == 5:
        break
    print(f"i={i}")

index_2 = 1

while index_2 < 10:
    print(f"index = {index_2}")
    index_2 = index_2 * 2


try:
    inputt = int(input(" san kirgiz "))
    print(inputt)
except Exception as e:
    print("Sende kata chygyp kaldy")

def print_hello(*args, **kwags):
    print(args)
    return kwags
maani = print_hello(12,4, name=23)
print(f"maani = {maani}")

def recursion(n):
    if n == 0:
        print("0")
    else:
        print(n)
        recursion(n-1)

recursion(10)


import random

print(random.randint(1,10))