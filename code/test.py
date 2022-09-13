from calculator import calculate
import unittest

# python3 -m pytest

class Testing(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(calculate(4,5,'+'),9)
    def testSubtraction(self):
        self.assertEqual(calculate(5,4,'-'),1)
    def testMultiplication(self):
        self.assertEqual(calculate(4,5,'*'),20)
    def testDivision(self):
        self.assertEqual(calculate(10,5,'/'),2)




