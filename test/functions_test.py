import unittest

from lib.functions_zosia import divisors


class TestFunctions(unittest.TestCase):

    def testDivisors(self):
        self.assertEquals(divisors(10),4)

    def testDivisorsTricky(self):
        self.assertEquals(divisors(25),3)

if __name__ == '__main__':
    unittest.main()