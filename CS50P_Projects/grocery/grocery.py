from collections import Counter

item_list = []

while True:
    try:
        item = input("").strip().upper()
        if item == "":
            break
        else:
            item_list.append(item)
    except EOFError:
        break

counts = Counter(sorted(item_list))

for item, count in counts.items():
    print(f"{count} {item}")
