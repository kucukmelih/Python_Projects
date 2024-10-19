def main():
    string = str(input("Greeting: "))
    print(value(string))

def value(string):
    string = string.strip().lower()
    if "hello" in string:
        return 0
    elif string.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
