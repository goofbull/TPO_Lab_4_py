import tkinter as tk

from controller import CalculatorController
from interface import CalculatorApp
from model import CalculatorModel

if __name__ == "__main__":
    model = CalculatorModel()  # Инициализируем модель
    controller = CalculatorController(model)  # Инициализируем контроллер
    root = tk.Tk()
    app = CalculatorApp(root, controller)  # Инициализируем приложение
    root.mainloop()  # Запуск GUI