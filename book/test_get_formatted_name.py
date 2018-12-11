import unittest
from book.name_function import get_formatted_name

class TestGet_formatted_name(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name=get_formatted_name('myfirst','mylast','middle')
        self.assertEqual(formatted_name,'Myfirst Middle Mylast')

if __name__ == '__main__':
    unittest.main()


