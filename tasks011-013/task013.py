from unittest import TestCase, main
from task011 import exponentiation
from task012 import calculate
from task012 import cur1_calculate

class Tests(TestCase):
    def test_equal(self):
        self.assertEqual(exponentiation(1, 2, 1), 3336.2175999999995)

    def test_calculation(self):
        self.assertEqual(calculate(1, '+', 1, '+', 1, '+', 1, '+', 1), 5)

    def test_cur1(self):
        self.assertEqual('hgfjdks', int)


if __name__ == '__main__':
    main()
