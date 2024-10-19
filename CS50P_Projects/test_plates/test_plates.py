from plates import is_valid

def main():
    test_plates()

def test_plates():
    assert is_valid("HELLO") == True
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("CS50!") == False  
    assert is_valid("AB12C3") == False

if __name__ == "__main__":
    main()
