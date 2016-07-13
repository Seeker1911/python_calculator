import unittest
import calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    pass
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    calc = calculator.Calculator()
    self.assertEqual(calc.add(2, 7), 9)

  def test_subtract(self):
    calc = calculator.Calculator()
    self.assertEqual(calc.subtract(7, 2), 5)

  def test_multiply(self):
    calc = calculator.Calculator()
    self.assertEqual(calc.multiply(7, 2), 14)

  def test_divide(self):
    calc = calculator.Calculator()
    self.assertEqual(calc.divide(7, 2), 3.5)

  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
