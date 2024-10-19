def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False

    for i in range(2, len(s)):
        if s[i].isdigit():
            if s[i] == '0': 
                return False
            return s[i:].isdigit()
        elif s[i].isalpha() and any(c.isdigit() for c in s[:i]):
            return False

    return True

if __name__ == "__main__":
    main()
