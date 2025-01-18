import unittest
from simple_calculator import SimpleCalculator

class Testcalculator(unittest.TestCase):
    def testadd(self):
        self.assertEqual(SimpleCalculator.add(None, 1, 2), 3)
        self.assertEqual(SimpleCalculator.add(None, -1, 2), 1)
        self.assertEqual(SimpleCalculator.add(None, -3, -2), -5)
        
        
    def testsub(self):
        self.assertEqual(SimpleCalculator.subtract(None, 5, 2), 3)
        self.assertEqual(SimpleCalculator.subtract(None, -5, 2), -7)
        self.assertEqual(SimpleCalculator.subtract(None, 0, 2), -2)
    
        
    def testmul(self):
        self.assertEqual(SimpleCalculator.multiply(None, 2, 5), 10)
        self.assertEqual(SimpleCalculator.multiply(None, -2, 5), -10)
        self.assertEqual(SimpleCalculator.multiply(None, 0, 5), 0)
    
    def testdiv(self):
        self.assertEqual(SimpleCalculator.divide(None, 10, 2), 5)
        self.assertEqual(SimpleCalculator.divide(None, 5, 2), 2.5)
        self.assertEqual(SimpleCalculator.divide(None, -10, 2), -5)
    