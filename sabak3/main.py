# terminaldy achuu -> ctrl + J
# ctrl + S -> сактоо учун

# A = p * r^2

# p = 3.14
# r = 5
# Homework, 3chu misal
# p = 3.14
# radius = 5
# print("Area:",p * radius**2)


# документация -> 
# https://pylessons.readthedocs.io/ru/latest/basics/types.html#id8 
# Bugunki temabyz

# 1 list - список
print("LIST")
menin_listim = []
b = 2
v = 3
c = 4
menin_listim_2 = [2, 3, 4, 5,6,b,v,c]
print(type(menin_listim))
print(menin_listim)
print(menin_listim_2)

# method - метод
menin_listim.append(4)
menin_listim.append(100)
print("koshkondon kiyin ->", menin_listim)
print(menin_listim.index(100)) # [4,100]
menin_listim.remove(4)
# menin_listim.pop()
print(menin_listim)
#index = индекс - >  бул data structures елементтин ордун белгилейт
# [10,100,100]
# [0,1,2]
kaitarylgan_maani = menin_listim.index(100)
print(menin_listim)
print(kaitarylgan_maani)

menin_listim3 = [3]
menin_listim3[0] = 10000000000
print(menin_listim3)
# -------------------------------------------- #

# 2 tuple - кортеж
print("TUPLE")
# en negizgi aiyrmasy == > bul ozgoboochu data structure
menin_tuplum = (1,2)
adam = ("Mike", 23, 90.5,"programmer")
print(adam)
print("Aty:",adam[0], " jash:", adam[1], " kalgandary..")
# menin_tuplum[0] = 1000000000
print(menin_tuplum[0])
print(type(menin_tuplum))

# 4 set - коптук (ozgorot)
print("SET")
menin_setim = {1,2,3,4,5,4}
print(type(menin_setim))
print(menin_setim)
menin_setim.add(1000)
menin_setim.add(1000)
menin_setim.remove(1000)
print(menin_setim)
menin_setim_2 = {1,"2dafd"}
print(menin_setim_2)

# 3 dict - словарь
# key - бул эшикти ачуучу инструмент

print("DICTIONARY")
menin_dictionarym = {"key":"achkych", "dictionary":"data structures"}
print(type(menin_dictionarym))
print(menin_dictionarym)
print("key =",menin_dictionarym["key"])
menin_dictionarym["group_7"] = "python"
menin_dictionarym[5] = "besh"
print(menin_dictionarym[5])

# telefon nomerler 
# Adyl - > key
# Adyldyn nomeri - > value 
telefon_nomerler = {}
telefon_nomerler["Adyl"] = "123456789"
print(telefon_nomerler["Adyl"])
print(telefon_nomerler.items())



# PEP8 style 
a=[]
# meninatym x
# meninAtym x
# MeninAtym x
menin_atym = 'Alidin' #✅
# classka misal
class BulClass:
    pass
# tab koldonuu
for i in range(12):
    print(i)
if True:
    print("Ok")
# flake8 di kochuruu -> pip install flake8
