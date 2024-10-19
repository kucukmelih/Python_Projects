calc = input("Expression: ")
n1, operator, n2 = calc.split(" ")

addition = int(n1) + int(n2)
subtraction = int(n1) - int(n2)
multiplication = int(n1) * int(n2)
division = int(n1) / int(n2)

if operator == '+':
    print(float(addition))
elif operator == '-':
    print(float(subtraction))
elif operator == '*':
    print(float(multiplication))
else:
    print(float(division))
