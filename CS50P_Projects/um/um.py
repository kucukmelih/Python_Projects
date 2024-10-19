import re

def main():
    print(count(input("Text: ")))

def count(s):
    word = "um"
    pattern = r'\b' + word + r'\b'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
