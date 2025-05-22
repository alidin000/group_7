# Mock mocking =>окшоштуруу

def get_data(filename):
    with open(filename, 'r') as file:
        return file.read()

def action():
    data = get_data("text.txt")

    for i in data:
        print(i)
    
    return data

# test method "action"

from unittest.mock import Mock
from unittest import TestCase
from unittest.mock import patch


class TestAction(TestCase):
    @patch("main_mock.get_data", return_value=['1'])
    def test_action(self,mocked):
        self.assertListEqual(action(),['1'])

class Temp:
    def temp_func(self):
        return 1
    
def method_temp(temp_object: Temp):
    return temp_object.temp_func()

mock_temp_func = Mock(return_value=['1'])

mock_temp = Mock()

mock_temp.temp_func = mock_temp_func

class TestMethod(TestCase):
    def test_method(self):
        self.assertEqual(method_temp(mock_temp),['1'])

    def test_method_temp(self):
        method_temp = Mock(return_value=1)
        self.assertEqual(method_temp(),1)