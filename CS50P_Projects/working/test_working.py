import pytest
from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

    with pytest.raises(ValueError):
        convert("9:70 AM to 12:70 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("9AM - 5PM")

    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")

    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00")

if __name__ == "__main__":
    pytest.main()
