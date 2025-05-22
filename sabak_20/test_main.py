import unittest

def print_():
    print("Hello")
    return True

class TestPrint(unittest.TestCase):
    def test_print(self):
        self.assertTrue(print_())

# discover => test*.py