import unittest

from controller import CalculatorController
from model import CalculatorModel


class TestCalculatorController(unittest.TestCase):

    def test_calculate(self):
        model = CalculatorModel()
        controller = CalculatorController(model)

        # Проверим, что метод calculate вызывает модель и передает результат
        result = controller.calculate("3 + 2")
        self.assertEqual(result, 5)

        result = controller.calculate("10 * 2")
        self.assertEqual(result, 20)

    def test_calculate_invalid_expression(self):
        model = CalculatorModel()
        controller = CalculatorController(model)

        # Проверим, что контроллер вызывает ошибку при некорректном выражении
        with self.assertRaises(ValueError):
            controller.calculate("2 / 0")
