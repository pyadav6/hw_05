# test_staticAndCoverage.py
import staticAndCoverage
import unittest
from brand import my_brand

my_brand_here = False
my_brand("HW 05 - Static Code Analysis")

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = staticAndCoverage.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = staticAndCoverage.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = staticAndCoverage.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)

if not my_brand_here:
    my_brand("HW 05 - Static Code Analysis")