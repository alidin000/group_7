#  f(x) = x ** 2 + 2 математика
# def [функциянын аты] ([argument]):
#     [code block]

# toluk struktrusy

# def name_of_function(argument:str, san: int, dictionary: dict[str, str]) -> int:
#     return 1


def hello_world():
    print("Hello world!!!")

# hello_world()

def hello_world_2(bizdin_argument):
    print(f"bizdin text:{bizdin_argument}")

# print("Hello world!!!")


# текстти алып туруп 10 жолу принт чыгар

def on_jolu_chygaruu(text):
    for i in range(10):
        print(f"i = {i}")
        hello_world_2(text)


# user_input = input("Текст киргиз:")
# on_jolu_chygaruu(user_input)


# 2 types of arguments & 2 турлуу аргументтер
# positional & позиционные аргументы
# key word argument & словарьга окшош (dictionary)
# dict [str, Any] -> key, value key туру всегда string гана бере алабыз. Any => любой нерсе
def f(*args, **kwargs):
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))

def ff(args, kwargs):
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))

# print("________________")
# f(1,2,3,4,54,6,t="keyword argument")

# ff(1,2)

# () - tuple
# {} - dictionary


def print_2(argument="Hello World!!!"):
    print(argument)


print_2()
print_2("!!!World Hello")

def do_accept(yes=True):
    print(f"Logic value = {yes}")

do_accept(False)
do_accept()


# global озгормолор 
# local озгормолор
print("++++++++++++++++++++++++++++++++++++++")
sabak_2 = "java"

def temp():
    global sabak_2
    sabak = "python"
    print(sabak[0])
    print(f"bizdin ekinchi maani = {sabak_2}")


    sabak_2 = "c++"
    print(f"bizdin temptin ichindegi sabak = {sabak_2}")

temp()
print(sabak_2[0])
print(f"bizdin temptin syrttagy sabak = {sabak_2}")



print("++++++++++++RETURN & VOID ++++++++++++")
# 2 турлуу функция, return(кайтаруу) & void(боштук) 
# return - функциядан маани кайтаруу
def summ(a,b):
    s = a + b
    return s

t = summ(3,2)
print(t)
# void - маани кайтарбаган функция
def p():
    print("hello_world")

tt = p()
print(tt)



t = {"t":4}
l = [1,2]
print(t.clear())
print(l.index(2))



# task -> сандардын суммасын табуу
print("______________ZADACHA_________")
def summa(*bizdin_sandar_positional_arguments):
    s = 0
    for san in bizdin_sandar_positional_arguments:
        print(f"san={san}")
        s = s + san
    return s

maani = summa(1)
print(maani)
print(summa(1,2))
print(summa(1,23,4,3243,24,32,4,324,324,32))
