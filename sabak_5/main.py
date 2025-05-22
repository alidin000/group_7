# print(9/0)

# print("Hello world")

# Katalar
# try / except strukturasy
try:
    # print(9/0)
    # print(int("'"))
    l = [3]
    print(len(l))
    # [1,2,3]
    # [0,1,2]
    print(l[2])
except ValueError as e:
    print("Error: ", "integer конвертация боло албайт, сан бер")
except ZeroDivisionError as e2:
    print("Error:", "nolgo boluugo bolboit")
except IndexError as t:
    print("Error:", "index списоктун чондугунан ашып кетти")
finally:
    print("Programma buttu")

# not, in, for, if
# try / except 

# try:
#     san = int(input("eki orunduu san ber:"))
#     l = [san]
#     if san > 99 or san < 10:
#         print("Eki orunduu emes")
#     else:
#         print('eki orunduu san')
#         print(f"Akyrky цифрасы {san % 10}")
#     print(l[312243])
# # except ValueError as e:
# #     print("TUURA EMES INPUT BERIP ATASYN VALUERROR")
# except Exception as e:
#     print("TUURA EMES INPUT BERIP ATASYN")
# finally:
#     print("Programma buttu")

print("______________________________________________")
try:
    dictionary = {}
    dictionary["name"] = "John"
    dictionary["age"] = 30
    print(dictionary["name"])
    print(dictionary["age"])
    print(dictionary["computer"])
except KeyError as key_error:
    print("Andai key jok")
except Exception as e:
    print("Andai soz jok")
finally:
    print(f"до:{dictionary}")
    dictionary.clear()
    print(f"posle: {dictionary}")


# try:
#     input = input("bir nerse jaz:")
# except KeyboardInterrupt as key_board_interrupt: 
#     print("\nCTRL + C basyldy")
# finally:
#     print("\tbuttu")

def func(text):
    if len(text) >= 5:
        raise Exception("Oto uzun")
    else:
        print(text)

t = "sgadfds"
print(t[0])
print(t[-1])
text = input("soz jaz (uzundugu 5 ten az bolgon):")

try:
    func(text)
except Exception as e:
    print("Men ыргыткан exception")
finally:
    print("Buttu")


boluuchu = int(input("boluuchunu ber:"))
if boluuchu == 0:
    raise ZeroDivisionError("0 саны болуучу боло албайт!")
else:
    print(10/boluuchu)