from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0

    ###

    try:
        convert("3/2")
    except ValueError:
        pass
    else:
        assert False

    try:
        convert("1/0")
    except ZeroDivisionError:
        pass
    else:
        assert False

    try:
        convert("one/two")
    except ValueError:
        pass
    else:
        assert False

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

    assert gauge(99) == "F"
    assert gauge(100) == "F"

    assert gauge(50) == "50%"
    assert gauge(25) == "25%"

if __name__ == "__main__":
    test_convert()
    test_gauge()
