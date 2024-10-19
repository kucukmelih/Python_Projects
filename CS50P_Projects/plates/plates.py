def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    plate = s[2:]
    
    if 6 >= len(s) >= 2 and s.isalnum() and s[:2].isalpha():
        for i in plate:
            if i.isdigit():
                index = s.index(i)
                if s[index:].isdigit() and int(i) != 0:
                    return True
                else: return False

        return True

if __name__ == "__main__":
    main()
