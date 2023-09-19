# -*- coding: cp1251 -*-
import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Ошибка: деление на 0"
    return a / b

def exponentiation(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Ошибка: невозможно извлечь квадратный корень из отрицательного числа"
    return math.sqrt(a)

def factorial(a):
    if a < 0 or not isinstance(a, int):
        return "Ошибка: невозможно вычислить факториал отрицательного или нецелого числа"
    if a == 0:
        return 1
    return a * factorial(a-1)

def sine(a):
    return math.sin(a)

def cosine(a):
    return math.cos(a)

def tangent(a):
    return math.tan(a)

# Функция для проверки ввода числа
def check_number_input(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

# Функция для проверки ввода операции
def check_operation_input(input_str):
    allowed_operations = ["+", "-", "*", "/", "^", "sqrt", "factorial", "sin", "cos", "tan"]
    if input_str.lower() in allowed_operations:
        return True
    return False


# Пример использования калькулятора
while True:
    operation = input("Введите операцию (+, -, *, /, ^, sqrt, factorial, sin, cos, tan): ")
    if not check_operation_input(operation):
        print("Ошибка: некорректная операция!")
        continue

    if operation in ["sqrt", "factorial", "sin", "cos", "tan"]:
        number = input("Введите число: ")
        if not check_number_input(number):
            print("Ошибка: некорректное число!")
            continue
        number = float(number)

        if operation == "sqrt":
            result = square_root(number)
        elif operation == "factorial":
            result = factorial(int(number))
        elif operation == "sin":
            result = sine(number)
        elif operation == "cos":
            result = cosine(number)
        elif operation == "tan":
            result = tangent(number)
    else:
        number1 = input("Введите первое число: ")
        number2 = input("Введите второе число: ")
        if not (check_number_input(number1) and check_number_input(number2)):
            print("Ошибка: некорректное число!")
            continue
        number1 = float(number1)
        number2 = float(number2)

        if operation == "+":
            result = addition(number1, number2)
        elif operation == "-":
            result = subtraction(number1, number2)
        elif operation == "*":
            result = multiplication(number1, number2)
        elif operation == "/":
            result = division(number1, number2)
        elif operation == "^":
            result = exponentiation(number1, number2)

    print("Результат:", result)
    choice = input("Хотите продолжить? (да/нет): ")
    if choice.lower() != "да":
        break
