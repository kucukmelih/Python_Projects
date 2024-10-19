string = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()

if string == "42":
    print("Yes")
elif string == "forty_two":
    print("Yes")
elif string == "forty-two":
    print("Yes")
elif string == "forty two":
    print("Yes")
else: print("No")
