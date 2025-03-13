from single_responsible_principle import math_operations


class MathOperationApplier:
    def apply(self, math_operation, first, second):
        if math_operation == "+":
            return first + second
        elif math_operation == "-":
            return first - second
        elif math_operation == "*":
            return first * second
        elif math_operation == "/":
            return first / second
        elif math_operation == "**":
            return first ** second
        else:
            raise ArithmeticError()


class Interpreter:
    def interpret(self, context):
        pass


class PythonStyleWithoutOrderMathOperationInterpreter(Interpreter):
    def __init__(self, math_operation_applier):
        self.math_operation_applier = math_operation_applier

    def interpret(self, context):
        split_data = context.strip().split()
        if len(split_data) % 2 == 0:
            raise ArithmeticError

        value = float(split_data[0])
        for i in range(1, len(split_data), 2):
            operation = split_data[i]
            next_value = float(split_data[i + 1])
            value = self.math_operation_applier.apply(
                operation, value, next_value
            )

        return value

math_operation_applier = MathOperationApplier()
interpreter = PythonStyleWithoutOrderMathOperationInterpreter(math_operation_applier)

calculation = input("Give us math operation to calculate")

value = interpreter.interpret(calculation)
print(value)