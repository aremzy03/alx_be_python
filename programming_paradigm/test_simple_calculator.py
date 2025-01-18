import unittest
from simple_calculator import SimpleCalculator

class Testcalculator(unittest.TestCase):
    
    
    def test_addition(self):
        self.assertEqual(SimpleCalculator().add(None, 1, 2), 3)
        self.assertEqual(SimpleCalculator().add(None, -1, 2), 1)
        self.assertEqual(SimpleCalculator().add(None, -3, -2), -5)
        
        
    def test_subtraction(self):
        self.assertEqual(SimpleCalculator().subtract(None, 5, 2), 3)
        self.assertEqual(SimpleCalculator().subtract(None, -5, 2), -7)
        self.assertEqual(SimpleCalculator().subtract(None, 0, 2), -2)
    
        
    def test_multiplication(self):
        self.assertEqual(SimpleCalculator().multiply(None, 2, 5), 10)
        self.assertEqual(SimpleCalculator().multiply(None, -2, 5), -10)
        self.assertEqual(SimpleCalculator().multiply(None, 0, 5), 0)
    
    def test_division(self):
        self.assertEqual(SimpleCalculator().divide(None, 10, 2), 5)
        self.assertEqual(SimpleCalculator().divide(None, 5, 2), 2.5)
        self.assertEqual(SimpleCalculator().divide(None, -10, 2), -5)
    