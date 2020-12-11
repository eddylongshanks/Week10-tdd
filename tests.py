import unittest
from app import Calculator

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
    
    def test_calculator_should_instantiate(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_should_return_sum_when_given_two_integers(self):
        result = self.calculator.add(4,5)
        expected = 9

        self.assertEqual(result, expected)
    
    def test_add_should_return_ValueError_when_given_two_strings(self):
        self.assertRaises(ValueError, self.calculator.add, "ten", "twenty")
    
    def test_multiply_should_multiply_numbers_when_given_two_integers(self):
        result = self.calculator.multiply(3,5)
        expected = 15

        self.assertEqual(result, expected)
    
    def test_multiply_should_return_ValueError_when_given_two_strings(self):
        self.assertRaises(ValueError, self.calculator.multiply, "five", "ten")
    
    def test_subtract_should_subtract_numbers_when_given_two_integers(self):
        result = self.calculator.subtract(5,2)
        expected = 3

        self.assertEqual(result, expected)
    
    def test_subtract_should_return_ValueError_when_given_two_strings(self):
        self.assertRaises(ValueError, self.calculator.subtract, "fourty", "one")

if __name__ == "__main__":
    unittest.main()
