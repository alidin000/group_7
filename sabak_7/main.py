# рекурсия 


# def recursion(argument):
#     # ozunu chakyryshym kerek
#     recursion(argument)


# recursion(5)

# 10 дон 1ге чейин сана, бирок рекурсия менен корсот

# 10
# 9
# 8
# ....
# 1
# h = 10
# while h > 0:
#     print(h)
#     h = h - 1

def count_down(argument):
    if argument > 0:
        print(f"argument = {argument}")
        kiyinki_argument = argument - 1
        count_down(kiyinki_argument)
    else:
        # argument =< 0
        print("Рекурсия бутту")


def count_down_2(argument):
    if argument > 0:
        print(f"argument = {argument}")
        kiyinki_argument = argument - 1
        count_down_2(kiyinki_argument)


# count_down(10)
# print("_+_+_++_+_+_+__+")
# count_down_2(5)

# 1 kadam
# def count_down_2(argument):
#     if argument > 0: #4
#         print(f"argument = {argument}")
#         kiyinki_argument = argument - 1 # 3
#         count_down_2(kiyinki_argument) # count_down_2(3)
# # 2 kadam
# def count_down_2(argument):
#     if argument > 0: #3
#         print(f"argument = {argument}")
#         kiyinki_argument = argument - 1 # 2
#         count_down_2(kiyinki_argument)  # count_down_2(2)

# # 3
# def count_down_2(argument):
#     if argument > 0: #2
#         print(f"argument = {argument}")
#         kiyinki_argument = argument - 1 # 1
#         count_down_2(kiyinki_argument)  # count_down_2(1)

# # 4 
# def count_down_2(argument):
#     if argument > 0: #1
#         print(f"argument = {argument}")
#         kiyinki_argument = argument - 1 # 0
#         count_down_2(kiyinki_argument)  # count_down_2(0)

# # 5 
# def count_down_2(argument):
#     if argument > 0: #0 ( False )
#         print(f"argument = {argument}")
#         kiyinki_argument = argument - 1
#         count_down_2(kiyinki_argument)
#     # иф ке кирген жок, рекурсия бутту

# void return 

# 1 ден N ге чейинки сандардын суммасын чыгар  summa(10) = > 1+ 2 + 3 + ... + 10 = 55

# def summa(N):
#     if N == 0:
#         return 0
    
#     print(f"N={N}")
#     kiyinki_argument = N - 1
#     return N + summa(kiyinki_argument)

def summa(N):
    if N == 0:
        return 0
    else:
        print(f"N={N}")
        kiyinki_argument = N - 1
        return N + summa(kiyinki_argument)


# # 1 - kadam 
# def summa(N): #  10
#     if N == 0:
#         return 0
#     else:
#         print(f"N={N}")
#         kiyinki_argument = N - 1 # 9
#         return N + summa(kiyinki_argument) # 10 +  summa(9)

# # 2 - kadam 
# def summa(N): #  9
#     if N == 0:
#         return 0
#     else:
#         print(f"N={N}")
#         kiyinki_argument = N - 1 # 8
#         return N + summa(kiyinki_argument) # 10 +  9 + summa(8)

# # 3 - kadam 
# def summa(N): #  8
#     if N == 0:
#         return 0
#     else:
#         print(f"N={N}")
#         kiyinki_argument = N - 1 # 7
#         return N + summa(kiyinki_argument) # 10 +  9 + 8 + summa(7)
    

# # .......

# # 10 - kadam
# def summa(N): #  1
#     if N == 0:
#         return 0
#     else:
#         print(f"N={N}")
#         kiyinki_argument = N - 1 # 0
#         return N + summa(kiyinki_argument) # 10 +  9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + summa(0)
    
# # 11 - kadam
# def summa(N): #  0
#     if N == 0: # (True)
#         return 0 # 10 +  9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0
#     else:
#         print(f"N={N}")
#         kiyinki_argument = N - 1
#         return N + summa(kiyinki_argument)
    
N_sum = summa(10)
print(N_sum)


# 4! = 4 * 3 * 2 * 1


def factorial(N):
    print(f"N = {N}")
    # base case / базовый случай
    if N == 1:
        return 1
    else:
        # рекурсивный случай
        # recursive case
        return N * factorial(N - 1)
    

print(factorial(4)) # 24
print(factorial(5)) # 120

# Ozunu bir neche jolu chakyruu

#fibonachi sandary 
# 1chi jana 2chi sandary berilgen 0,1 
# list = [0,1,1,2,3,5,8,13,21 ..]\
# list[2] = list[0] + list[1]
# list[3] = list[1] + list[2]
# list[4] = list[2] + list[3]
# list [i] = list[i - 1] + list[i - 2]

def fibonachhi(N):
    # base case
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibonachhi(N-1) + fibonachhi(N-2) # fibonacchi(4) + fibancchi(3)

# # 1  - kadam
# def fibonachhi(N): #3
#     # base case
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1
#     else:
#         return fibonachhi(N-1) + fibonachhi(N-2) # fibonacchi(2) + fibancchi(1)

# # 2- kadam
# def fibonachhi(N): # 2
#     # base case
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1
#     else:
#         return fibonachhi(N-1) + fibonachhi(N-2) # fibonacchi(1) + fibancchi(0)
    
# # 3 - kadam
# def fibonachhi(N): # 1
#     # base case
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1 # 1 di kaitarat
#     else:
#         return fibonachhi(N-1) + fibonachhi(N-2)

# # 4 - kadam 
# def fibonachhi(N): # 0 
#     # base case
#     if N == 0:
#         return 0 # 0du kaitarat
#     elif N == 1:
#         return 1
#     else:
#         return fibonachhi(N-1) + fibonachhi(N-2)
    
# # 5 - kadam
# def fibonachhi(N): # 1
#     # base case
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1 # 1 di kaitarat
#     else:
#         return fibonachhi(N-1) + fibonachhi(N-2)
    
#                 4
#         3                 2
#     2      1          1         0
# 1    0 
# 1 + 0 + 1 + 1 + 0 = 3

print(fibonachhi(4))
print( [0,1,1,2,3,5,8,13,21][4])