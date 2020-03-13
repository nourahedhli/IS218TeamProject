import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.add(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.subtract(1, 2)
        self.assertEqual(-1, result)

    def test_multiple_result_calculator(self):
        calculator1 = Calculator()
        calculator2 = Calculator()

        calculator1.Sum(1, 2)
        calculator2.Difference(3, 4)
        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()
