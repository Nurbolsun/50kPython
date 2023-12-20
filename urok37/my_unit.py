import unittest
from func import my_sum
class MySumTest(unittest.TestCase):
    def test_sum_two_num(self):
        self.assertEqual(my_sum(7,2), 9)

    def test_two_words(self):
        assert my_sum('hi', 'man') == 'himan'

    def test_sum_str(self):
        with self.assertRaises(TypeError):
            my_sum("5", 78)

unittest.main()