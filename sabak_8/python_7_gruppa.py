import math
# from math import pow
from math import sqrt
# def sqrt(argument):
#     return argument ** 0.5

# print(math.)

# 1-10 tak sandardyn квадраты
index = 1

while index < 11:
    if index % 2 == 1:
        print(f"kvadraty : {pow(index,2)}")

    if index % 2 == 0:
        print(f"tamyry: {sqrt(index)}")
    index = index + 1



import random


# print(random.randint(1,10))
# sandy tabuu
# binary search 
# 6 10
# 5 
# 7 
# 6

# target = random.randint(1,10)

# while True:
#     bizdin_san = int(input("san kirgiz:"))
#     if target == bizdin_san:
#         print("taptyn!")
#         break
#     print("tappadyn dagy araket kyl!")


import os

print(os.listdir())
print(os.getcwd())
# print(os.)