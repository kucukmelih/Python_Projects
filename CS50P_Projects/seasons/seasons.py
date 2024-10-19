from datetime import date
import inflect
import sys

i = inflect.engine()

def main():
    try:
        year, month, day = input("Date of birth: ").split("-")
    except ValueError:
        print("Invalid date")
        sys.exit(1)

    print(convert(year, month, day))

def convert(y, m, d):
    try:
        _date = date(int(y), int(m), int(d))
    except ValueError:
        return "Invalid date"

    _today = date.today()
    diff = _today - _date

    mins = int(diff.total_seconds() / 60)
    text = i.number_to_words(mins, andword='')
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()
