class CalculatorController:
    def __init__(self, model):
        self.model = model  # Модель

    def calculate(self, expression: str):
        return self.model.evaluate_expression(expression)
