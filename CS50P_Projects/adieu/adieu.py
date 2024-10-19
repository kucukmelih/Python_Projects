import inflect

p = inflect.engine()

name_list = []

while True:
    try:
        user_input = str(input("Name: "))
        if user_input == "":
            break
        name_list.append(user_input)
    except EOFError:
        print()
        break

output = p.join(name_list)
print("Adieu, adieu, to", output)
