# try:
#     # code block
# except Exception as e:
#     # code block

try:
    print(0 / 0)
except ZeroDivisionError as e:
    print("нольго болсо болбойт")
    print(e)
print("Hello world")


try:
    a = int('0')
except Exception as e:
    print(e)
else:
    print("It worked without any issues")
    print("Эч кандай проблемасыз иштеди")

# d = {}
# try:
#     inp = int(input("San kirgiz:"))
# except Exception as e:
#     print(e)
# else:
#     print("Ishtedi")
#     d[inp] = "YES"

# print(f"dictionary = {d}")


try:
    inn = int(input("input ber:"))
except Exception as e:
    print(e)
else:
    d = [inn]
    print(d)
finally:
    # try:
    #     d.clear()
    #     print(d)
    #     print("Buttu")
    # except Exception as ee:
    #     print(ee)
    d.clear()
    print(d)
    print("Buttu")

try:
    t = int('t')
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except TypeError as e:
    print(e)

class AndaiKeyJok(Exception):
    pass

slovar = {}
slovar['name'] = "ali"
slovar['age'] = 21
try:
    name = slovar['name']
    age = slovar['age']
    try:
        height = slovar['height']
    except Exception as e:
        raise AndaiKeyJok("Andai key jok")
    else:
        print("----")
    # raise

except AndaiKeyJok as e:
    print("Bul jer")
    print(e)
else:
    print(slovar['height'])
finally:
    print("Buttu")