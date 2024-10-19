menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

exit_key = 'command + d'
total = 0

while True:
    try:
        order = str(input("Item: ")).strip().title()

        if order == exit_key:
            raise EOFError

        if order not in menu:
            continue

        total += menu[order]

        print(f"Total: ${total:.2f}")

    except EOFError:
        exit()

