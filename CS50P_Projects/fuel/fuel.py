while True:
    try:
        x, y = input("Fraction: ").strip().split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        break

    except(ZeroDivisionError, ValueError):
        ...

result = int(x) / int(y) * 100

if result >= 99:
    print("F")
elif result <= 1:
    print("E")
else:
    print(f"{result:.0f}%")
