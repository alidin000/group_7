# Homework

dicionary = {}
dicionary['aty'] = "Ali"
dicionary['jash'] = 24
dicionary['ulutu'] = "kyrgyz"
dicionary['srok'] = "2029/10/12"

print("===========================")
print("= Aty:         ",dicionary['aty'],"      =")
print("= jash       ",dicionary['jash'],"         =")
print("===========================")
print("===========================")
print("===========================")
print("===========================")


# 6 April

# IF, ELSE - эгер же болбосо

if 4 > 3:
    print("Ooba 4 chon")
else:
    print("4 chon emes")

if True:
    print("True")

if False:
    print("False")
else:
    print("False emes")

print("experiment")
san = 5

if san == 5:
    print("Mykty okuuchu")
elif san == 5:
    print("Jakshy okuuchu")
elif san == 5:
    print("Ortocho okuuchu")
else:
    print ("Jaman okuuchu")

print("_____")
if san == 5:
    print("Mykty okuuchu")
if san == 5:
    print("Jakshy okuuchu")
if san == 5:
    print("Ortocho okuuchu")
if san < 5:
    print ("Jaman okuuchu")
# loop <=> цикл

# Hello world -> 10 jolu print kylyp chygar 
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")

# for loop <-> for цикл
# range(1,10) -> 1,2,3,4,5,6,7,8,9,10
# for i in range(1,11):
#     print(i)
#     print(i, "- Hello world")

# 1 - kadam
# i = 1
#print(1)
#print("Hello world")
# 2- kadam 
# i = 2
#print(2)
#print("Hello world")
# -------
# ------
# 10 - kadam
# i = 10
# print(10)
# print("Hello world")

# print("_________")
# print("List menen for loop")
# menin_listim = [1,2,3,4,5,6,7,8,9,10]
# menin_tuplum = (1,2,3,4,5,6,7,8,9,10)
# menin_setim = {1,2,3,4,5,6,7,8,9,10}

# for ozgormo in menin_listim:
#     print("LIST")
#     print(ozgormo)
#     print(ozgormo, "- Hello World")

# print("_________")
# print("TUPLE menen for loop")
# for i in menin_tuplum:
#     print("TUPLE")
#     print(i)
#     print(i, "- Hello World")


# print("_________")
# print("SET menen for loop")
# for ozgormo in menin_setim:
#     print("SET")
#     print(ozgormo)
#     print(ozgormo, "- Hello World")

# FOR loop strukturasy => [for] [ozgormonun aty] [in] [range method je data structures]



# while LOOP (ЦИКЛ)

# while (condiition \ условие ):
#     # code block \ блок кода

# while True:
#     print("TUUUURAA?")

# эгер бесконечный цикл кирип калсак ctrl + c дегенди терминалга жазыш керек
i = 0
while i < 10:
    print(i)
    i = i + 1
# 1 - kadam 
# i = 0
# print(0)
# i = 0 + 1
# 2 - kadam
# i = 1
# print(1)
# i = 1 + 1
# 3 - kadam
# i = 2
# print(2)
# i = 2 + 1
# .......
# 10 - kadam
# i = 9
# print(9)
# i = 9 + 1
# 11 - kadam
# i = 10 -> 10 < 10 => bul false maani beret

j = 10

while j >= 0:
    print("j=",j)
    j = j - 1

menin_listim_2 = [1,2,3,4,5,5]
print("teksheruu")
print(len(menin_listim_2))
# print(menin_listim_2[6])
# [1,2,3,4,5,5]
# [0,1,2,3,4,5]
index = 0
# len() -> method. Bul data structures чондугун (ичинде канча бар)
while index < len(menin_listim_2):
    print(menin_listim_2[index])
    index = index + 1

# 1- kadam
# index = 0
# print(menin_listim_2[0]) => 1
# index = 0 + 1
# 2 - kadam
# index = 1
# print(menin_listim_2[1]) => 2
# index = 1 + 1
# ......
# 6 - kadam
# index = 5
# print(menin_listim_2[5]) => 5
# 7 - kadam
# index = 5 + 1
#  6 < 6 -> False (while loop ka kirbeit)

# break, continue -> 
print("BREAK")
for i in range(1,10):
    if i == 5:
        print("men chygyp kettim")
        break
    else:
        print(i)
        print("besh bolo elek")

print( "CONTINUE ")
for i in range(1,10):
    if i == 5:
        print("men 5 ti ignor kylyp atam")
        continue

    print(i)
    print("balbal")


index2 = 0

while index2 < 10:
    if index2 % 2 == 0:
        print("Bul jup san")
        index2 = index2 + 1
        continue
    print(index2)
    index2 = index2 + 1


menin_atym = input("atyndy jaz:")
# terminaldan kirgen nerseler string
# integer algybyz kelse -> int()
print("menin atym:", menin_atym)

san = int(input("san ber:"))
print("san:", san)
print(type(san))