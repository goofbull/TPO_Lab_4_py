class CalculatorModel:
    def evaluate_expression(self, expression: str):
        try:
            # Используем встроенную функцию eval для вычисления математического выражения
            result = eval(expression)
            return result
        except Exception as e:
            raise ValueError("Ошибка вычисления!") from e
