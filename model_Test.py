import unittest

from model import CalculatorModel


class TestCalculatorModel(unittest.TestCase):

    def test_evaluate_expression(self):
        model = CalculatorModel()

        # Проверим корректность вычислений
        result = model.evaluate_expression("2 + 3")
        self.assertEqual(result, 5)

        result = model.evaluate_expression("10 - 5")
        self.assertEqual(result, 5)

        result = model.evaluate_expression("2 * 3")
        self.assertEqual(result, 6)

        result = model.evaluate_expression("6 / 2")
        self.assertEqual(result, 3)

    def test_invalid_expression(self):
        model = CalculatorModel()

        # Проверим на ошибку при делении на ноль
        with self.assertRaises(ValueError):
            model.evaluate_expression("2 / 0")
