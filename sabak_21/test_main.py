from unittest import TestCase
from unittest.mock import Mock, patch
import unittest

from main_ import action

class TestAction(TestCase):
    @patch("main.another_function")
    def test_action(self,mocked_another_function):
        # another_function mocking
        mocked_another_function.return_value = "Test string" 
        self.assertEqual(action(),f"the string we got is Test string")
    
    @patch("main.my_function", return_value="the string we got is Test string")
    def test_action_2(self,mocked_function):
        self.assertEqual(action(),f"the string we got is Test string", "patching - 2")


import random

def func_2(random):
    if random.randint(1,5) == 2:
        return "temp"
    else:
        return None

class TestFunc_2(TestCase):
    @patch("test_main.random")
    def test_func_2(self,mocked_random):
        mocked_random.randint.return_value = 2
        self.assertEqual(func_2(mocked_random),"temp", "testing mocked random = 2 ")
    
    @patch("test_main.random")
    def test_func_2_1(self, mocked_random):
        mocked_random.randint.return_value = 1
        self.assertEqual(func_2(mocked_random),None, "testing mocked random = 1")

    
    def test_with_mock(self):
        random = Mock()
        random.randint = Mock(return_value=2)
        self.assertEqual(func_2(random),"temp", "testing with Mock()")

from main_ import division, temp, g, get_10

class TestDivision(TestCase):
    @patch("main.division")
    def test_division(self, division):

        division.side_effect = ZeroDivisionError
        
        self.assertEqual(temp(),"fail", "testing side effect")
    
    @patch("main.misal")
    def test_misal(self,misal_mock):
        misal_mock.side_effect = TypeError
        self.assertEqual(g(),"type error")

    @patch("main.return_numbers")
    def test_return_numbers(self,mocked_func):
        mocked_func.side_effect =[0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(get_10(),[0,1,2,3,4,5,6,7,8,9,10])