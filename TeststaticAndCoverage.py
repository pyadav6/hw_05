""" To test the unit test cases for a program, 
    for printing the student and assignment details, 
    test the functions of the staticandcoverage.py
"""
import unittest
from brand import my_brand
import staticandcoverage

MYBRANDHERE = False
my_brand("HW 05 - Static Code Analysis")

class TestFunctionsOfstaticandcoverage(unittest.TestCase):
    """
    Test the functions from the staticandcoverage.py
    """

    def test_addintegers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = staticandcoverage.add(4, 7)
        self.assertEqual(result, 11)

    def test_addfloats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = staticandcoverage.add(15.7, 14.3)
        self.assertEqual(result, 30.0)

    def test_addstrings(self):
        """
        Test the addition of two strings returns the two string as one concatenated string
        """
        result = staticandcoverage.add('Spider', 'Man')
        self.assertEqual(result, 'SpiderMan')

    def test_subtractintegers(self):
        """
        Test the subtraction of two integers returns the correct result
        """
        result = staticandcoverage.subtract(55, 11)
        self.assertEqual(result, 44)

    def test_multiplyintegers(self):
        """
        Test the multiplication of two integers returns the correct result
        """
        result = staticandcoverage.multiply(13, 3)
        self.assertEqual(result, 39)

    def test_divideintegers(self):
        """
        Test the division of two integers returns the correct result
        """
        result = staticandcoverage.divide(8, 2)
        self.assertEqual(result, 4)

    def test_dividebyzero(self):
        """
        Test the division of a integer by zero returns the correct result
        """
        with self.assertRaises(ZeroDivisionError):
            staticandcoverage.divide(8, 0)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)

if not MYBRANDHERE:
    my_brand("HW 05 - Static Code Analysis")
#End-of-file (EOF)
