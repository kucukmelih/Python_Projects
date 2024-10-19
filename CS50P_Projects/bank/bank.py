string = str(input("Greeting: ")).strip().lower()

if "hello" in string:
    print("$0")
elif string.startswith("h"):
    print("$20")
else: print("$100")
