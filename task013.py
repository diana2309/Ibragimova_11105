from unittest import TestCase, main
from task011 import exponentiation
from task012 import calculate

class Tests(TestCase):
    def test_type(self):
        self.assertEqual(exponentiation('3.45', 45, 67), int)

    def test_calculation(self):
        self.assertEqual(calculate(1, '+', 1, '+', 1, '+', 1, '+', 1), 5)


if __name__ == '__main__':
    main()