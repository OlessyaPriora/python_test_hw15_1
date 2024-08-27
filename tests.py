import unittest
import json
import os
from write_read_file import *


class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_file.txt'
        self.test_data = {
            "pk": 4,
            "title": "Test Title",
            "author": "Test Author",
            "published_date": "2024-06-23",
            "publisher": 6,
            "price": 9.99,
            "discounted_price": 3.56,
            "is_bestseller": True,
            "is_banned": False,
            "genres": [1, 3, 5]
        }
        self.empty_data = {}


    def test_write_and_read_file(self):
        write_to_file(self.test_file, self.test_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, self.test_data)


    def test_write_and_read_empty_file(self):
        write_to_file(self.test_file, self.empty_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, self.empty_data)

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('nonexistent_file.txt')

    def test_write_bad_data_into_file(self):
        with self.assertRaises(TypeError):
            write_to_file(self.test_file, object())


    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == '__main__':
    unittest.main()







