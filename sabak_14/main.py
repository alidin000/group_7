# accound password = > файлдарга сактап келишкен
# logs = > print("бул кадамда бир нерсе болду {data}")
# file modes => 'r',    'w' ,    'a'
#               read | write | append 

# write = файлды башынан жазуу
# append = файлга кошуп жазуу / улап жазуу
# read \ 'r'
file = open("example.txt", "r")
ichindegi_nerseler = file.read()
print(ichindegi_nerseler)
file.close()
# .
# write  \ 'w'
# file_2 = open("example_2.txt","w")
# num_of_characters = file_2.write("Ozgoruldu")
# print(f"{num_of_characters} characters")
# file_2.close()

file_3 = open("C:\\Users\\user\\Desktop\\Motion web\\group_7\\sabak_14\\example_3.txt","w")
num_of_characters = file_3.write("Hello world 3")
print(f"{num_of_characters} characters")
file_3.close()

# special characters => "*, \, \n ,"
# append = 'a' 
file_appenod = open("example_2.txt","a")
num_of_characters = file_appenod.write("\nAppend boldu\n")
print(f"{num_of_characters} characters")
file_appenod.close()
# with(menen) - context manager

with open("example.txt", 'r') as filee:
    content = filee.read()
    print(content)
with open("example.txt", 'a') as filee:
    print(filee.write("\nToday we are learning how to work with files!\n"))

# account with password
