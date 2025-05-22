def addition(a,b):
    return a+b

def tataal_function(list): 
    for i in range(len(list)):
        list[i] = list[i]**4
    return list

# 2 + 1 = 3
# 0 + 0 = 0

# UNIT TEST => бирдик

# assertEqual(addition(2,3), 5)

# case 1:
# assetEqual(tataal_function([12,4]),[144,16])

# Integration test => модулдардын же башка башка компоненттердин бири-бири иштоосун текшеруу
# End-To-End => бир программанын башынан аягына чейинки процессти текшерет 

# black box testing 
# white box testing 
def print_hello():

    print("hello")
    # return 0

import unittest

class TestMethods(unittest.TestCase):
    def test_addition(self):
        # EDGE cases => 
        self.assertEqual(addition(2,3),5) # equal = барабар
        self.assertEqual(addition(0,0),0)

    def test_addition_2(self):
        self.assertEqual(addition(1,2),3)
        self.assertEqual(addition(-1,-2),-3)
    
    # def test_addition_failure(self):
    #     # EDGE cases => 
    #     self.assertEqual(addition(2,3),3) # equal = барабар
    #     self.assertEqual(addition(0,0),-1)

    def test_check_none(self):
        self.assertIsNone(print_hello(),"We are checking None")


def fun_function(a):

    import random

    if random.randint(1,10) >= 5:
        return a / 2
    else:
        return a * 2

class TestFunFunction(unittest.TestCase):
    def test_fun_function(self):
        self.assertGreater(fun_function(10),10,"We are checking if outcome of func is greater then the argument")



def fun_2(list):
    
    mx = list[0] / list[1]

    for i in list:
        mx = max(mx,i)

    return max(list) == mx


class TestFun_2(unittest.TestCase): 
    def test_fun_2(self):
        self.assertTrue(fun_2([1,2,3,4]))

    def test_fun_2_2(self):
        self.assertTrue(fun_2([1,2,3,4]))

    def test_for_empty_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            fun_2([0,0])

    def test_for_empty_list(self):
        with self.assertRaises(IndexError):
            fun_2([])

        # self.assertTrue(fun_2([]),"Empty list")
    
# reverse = "Ali" => "ilA"
class NotStringError(Exception):
    pass

def func(string):
    if type(string) != str:
        raise NotStringError("String emes")
    
    st = ""
    for i in range(len(string)):
        print(f"st = {st}")
        print(f"i = {i} string[-(i+1)]= {string[-(i+1)]}")

        st += string[-(i+1)]
    # "ali ad ad ".split(" ")
    string = list(string)
    for i in range(len(string)//2):
        string[i], string[len(string)-i-1] = string[len(string)-i-1] , string[i]
        # ali 
        # a, i = i , a
        # ila

    return "".join(string)

    # return string[::-1]
    

# print(func("Ali"))
# print("Ali"[::-2])

class TestFunc(unittest.TestCase):
    def test_func(self):
        # case 1 base case "text" => "txet"
        self.assertEqual(func("text"),"txet")

        # case 2 tak sanduu => "tan" => "nat"
        self.assertEqual(func("tan"), "nat")

        # case 3 jup sanduu => "test" => "tset"
        self.assertEqual(func("test"),"tset")

        # case 4 empty string => "" => ""
        self.assertEqual(func(""),"")

        # case 5 not string => 5 => NotString
        with self.assertRaises(NotStringError):
            func(0)