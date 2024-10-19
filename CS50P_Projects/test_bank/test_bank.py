from bank import value

def main():
    test_bank1()
    test_bank2()
    test_bank3()

def test_bank1():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("  Hello  ") == 0

def test_bank2():
    assert value("Hi") == 20
    assert value("Hey") == 20
    assert value("How's it going?") == 20

def test_bank3():
    assert value("cs50") == 100
    assert value("50") == 100
    assert value("weee") == 100

if __name__ == "__main__":
    main()
