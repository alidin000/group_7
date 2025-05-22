# # int float str 
# # a = 10

# # ctrl + / 

# a = 10
# python_7_group = 12.4
# python_7_group_ters = -12.4 # -> float
# ozgormo = 11 # -> int 
# string = "бул текст"
# string_2 = 'бул да текст'
# bool2 = True # -> туура 
# bool2 = False # -> ката 

# # print() -> терминалга чыгарып беруучу нерсе
# print("Bizdin ozgormolor")
# print(a)
# print(python_7_group)
# print(python_7_group_ters)
# print(string)
# print(bool2)

# print("bizdin orgormonun turu:")
# print(type(bool2))
# print(type(string_2))
# print(type(python_7_group))


# # Python operations => Питондогу операциялар 

# # + (Кошуу), 
# # - (Кемитуу), 
# # * (Көбөйтүү), 
# # / (Бөлүү), 
# # // (Бүтүн бөлүү), 
# # % (Калдык), 
# # ** (Даражага көтөрүү). 
# ozgormo1 = 1
# ozgormo2 = 2
# summa = ozgormo1 + ozgormo2
# print("ozgormo1",ozgormo1)
# print("ozgormo2",ozgormo2)
# print("summa=", summa)

# print("kemituu => ", ozgormo2 - ozgormo1)
# print("koboituu => ", ozgormo2 * ozgormo1)
# print("boluu => ", ozgormo2 / ozgormo1)
# print("boluu 2=> ", ozgormo2 // ozgormo1)
# print("boluugo misal=>", 12 / 5)
# print("boluugo misal2=>", 12 // 5)
# print("boluugo misal2=>", 14 // 5)
# print("boluugo misal2=>", 14 / 5)


# san = 10
# boluuchu = 3
# kaldyk = 10 % 3
# print(kaldyk)
# print(11 % 3)
# print(12 % 3)
# # 10 = 3 * 3 + 1
# # 12 = 3 * 4 + 0

# daraja = 2 ** 3 # = 8 
# print("daraja =",daraja)

# t = "python"
# g = "group"
# print(t+" "+g)
# print(t+g)

# # Python Салыштыруулар 


# n = 1
# n2 = 2
# text1 = "python"
# text2 = "python2"

# print("Salyshtyruular")
# print(n == n2)
# print(n > n2)
# print(n < n2)

# print( n != n2 )

# print(text1 == text2)
# print(text1 != text2)
# print(text1 > text2)
# print('ac' > 'ab')
# # a b c d e ..... z



# # logicalyk operatorlor 

# # and (жана) koboitup koisok 
# # not (эмес) 
# # or (же) koshup koisok 

# x = True # 1 dep esepteili
# y = False # 0 dep esepteili
# print("_________________")
# # 0 menen 1 => koboitup koisok 
# print(x and y) # 0 * 1 => 0 => False
# print(x or y) # 0 + 1 => 1 => True

# print(not x) # -> False
# print(not y) # -> True


# # Struktura dannyh

# # List -> список 
# # Sets -> коптук
# # Tuple -> кортеж
# # Dictionary -> словарь создук

# # ozgoruuchu 
# # ozgorboochu 

# tuple_1 = (1,2,4)
# print("_______")
# print(tuple_1)
# print(type(tuple_1))


# print(tuple_1[0])

# list_1 = [1,2,4]
# print(list_1[0])

# # [1,2,3,4]
# #  0 1 2 

import os
f = open("temp.txt",'w')
for root, dir, files in os.walk('.'):
    f.write('\nroot\n')
    f.write(str(root))
    f.write('\ndirs\n')
    f.write(str(dir))
    f.write('\nfiles\n')
    f.write(str(files))