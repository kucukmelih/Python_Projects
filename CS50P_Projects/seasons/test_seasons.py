from seasons import convert

def main():
    test_convert()

def test_convert():
    assert convert(2003, 4, 2) == "Eleven million, two hundred thirty-six thousand, three hundred twenty minutes"
    assert convert(2, 4, 2003) == "Invalid date"

if __name__ == "__main__":
    main()
