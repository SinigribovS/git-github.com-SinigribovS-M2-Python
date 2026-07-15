def calculator_mic(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y == 0:
            return "Nu e posibila impartirea la 0"
        return x / y
    else:
        return "Operatie nerecunoscuta"

print(calculator_mic(10, 5, "+"))
print(calculator_mic(10, 5, "*"))
print(calculator_mic(10, 2, "/"))
print(calculator_mic(10, 2, "-"))