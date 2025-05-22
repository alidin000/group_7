# Mock => окшоштуруу, жасалма функция же болбосо жасалма класс
# patch => убактылуу жасалма нерсеге алмаштыруу 

from unittest.mock import Mock, patch



def my_function(another_function):
    string = another_function()
    return f"the string we got is {string}"

def another_function():
    return "Some stupid string"

def action():
    return my_function(another_function)


class Human():
    def __init__(self):
        pass

    def speak(self):
        return "Hello"

mock_human = Mock()

mock_human.speak = Mock(return_value="Not Hello")

def f(person: Human):
    return person.speak()

print(f(mock_human))

def division():
    return 1 / 1

division = Mock(side_effect=TypeError)

def temp():
    try:
        return division()
    except ZeroDivisionError:
        return "fail"
    except TypeError:
        return "type"

import unittest
class TestDivision(unittest.TestCase):

    def test_division(self):
        
        self.assertEqual(temp(),"type", "testing side effect")


def misal(a):
    integer = int(a) #
    return integer

def g():
    try:
        return misal("a")
    except TypeError:
        return "type error"
    

def return_numbers():
    return 1

def get_10():
    l = []
    for _ in range(10):
        # for i in range(10)
        # for _ in range(10)
        l.append(return_numbers())
    return l

return_numbers = Mock(side_effect=[1,2,"Alidin"])
print(return_numbers())
print(return_numbers())
print(return_numbers())


return_numbers.assert_called_once()
# assert return_numbers.call_count == 1