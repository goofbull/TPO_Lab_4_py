import unittest
from unittest.mock import patch
import tkinter as tk

from controller import CalculatorController
from interface import CalculatorApp
from model import CalculatorModel


class TestCalculatorApp(unittest.TestCase):

    @patch('tkinter.messagebox.showerror')
    @patch.object(CalculatorModel, 'evaluate_expression', side_effect=ValueError("Ошибка вычисления!"))
    def test_display_error_called_on_invalid_expression(self, mock_evaluate, mock_showerror):
        # Подготовка модели, контроллера и приложения
        model = CalculatorModel()
        controller = CalculatorController(model)
        root = tk.Tk()
        app = CalculatorApp(root, controller)

        # Симулируем ошибку в модели
        model.evaluate_expression.side_effect = ValueError("Ошибка вычисления!")

        # Нажмем кнопку "=" с ошибочным выражением
        app.display.insert(tk.END, "1 / 0")  # Вводим ошибочное выражение
        app.on_button_click("=")  # Кликаем "=" для вычисления

        # Проверим, что метод отображения ошибки был вызван с нужными параметрами
        mock_showerror.assert_called_with("Ошибка", "Ошибка вычисления!")

    def test_calculator_app_correct_output(self):
        model = CalculatorModel()
        controller = CalculatorController(model)
        root = tk.Tk()
        app = CalculatorApp(root, controller)

        # Симулируем ввод и вычисление выражения
        app.display.insert(tk.END, "3 + 2")
        app.on_button_click("=")

        # Проверим, что на дисплее появился правильный результат
        self.assertEqual(app.display.get(), "5")
