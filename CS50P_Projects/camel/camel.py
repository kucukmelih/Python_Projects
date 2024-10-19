name = input("camelCase: ").strip()

for x in name:
    if x.isupper():
        print(f"_{x.lower()}", end="")
    else: print(x, end="")
