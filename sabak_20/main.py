# unittest.TestCase
import unittest

def circle_area(r, pi):
    return pi * r**2

def perimeter(r, pi):
    return 2 * pi *r

def temp_function():
    return [1,2,4,5]

class TestTest(unittest.TestCase):
    def setUp(self):
        print("1. setting up our list before testing")
        self.output = [1,2,4,5]
        self.PI = 3.14
        print(self.output)
    
    def test_my_list(self):
        print("2. Testing...")
        self.assertListEqual(temp_function(),self.output)

    def test_circle_area(self):
        self.assertEqual(circle_area(3,self.PI), self.PI*3**2)

    def test_perimeter(self):
        self.assertEqual(perimeter(3,self.PI), 2 * self.PI * 3)

    def tearDown(self):
        self.output.clear()
        print("3. clearing up our list after testing")
        print(self.output)


def reading(file):
    return file.read().split('\n')

# with open("text.txt", 'r') as file:
#     output = reading(file)
#     print(output.split('\n'))


class TestReading(unittest.TestCase):
    def setUp(self):
        self.file = open("text.txt",'r')
        self.output = self.file.read().split('\n')
        self.file.seek(0)
        # self.output = ['1', '2', '3', '4', '5']
    
    def test_reading(self):
        func_output = reading(self.file)
        print(func_output)
        print(type(func_output))
        self.assertListEqual(func_output, self.output, "output okshosh emes")
    
    def tearDown(self):
        self.file.close()
        print("Closing the file")
