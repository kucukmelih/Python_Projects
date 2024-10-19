calories = {
    "apple" : "130",
    "sweet cherries" : "100",
    "avocado" : "50",
    "kiwifruit" : "90",
    "pear" : "100"
}

fruit = str(input("Item: ")).strip().lower()

if fruit in calories:
    print(f"Calories: {calories[fruit]}")
else: print()

