import unittest

from lib.divisors import getNumberOfDivisors


class TestFunctions(unittest.TestCase):

    def testDivisors(self):
        self.assertEquals(getNumberOfDivisors(10), 4)

    def testDivisorsTricky(self):
        self.assertEquals(getNumberOfDivisors(25), 3)

    def testDivistors1(self):
        self.assertEquals(getNumberOfDivisors(1),1)

    def testDivisorsPrime(self):
        self.assertEquals(getNumberOfDivisors(7),2)


if __name__ == '__main__':
    unittest.main()