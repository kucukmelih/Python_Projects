import re
import sys

def convert(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)
    if time:
        start_hour = int(time.group(1))
        start_minute = time.group(2) if time.group(2) else '00'
        end_hour = int(time.group(4))
        end_minute = time.group(5) if time.group(5) else '00'

        if int(start_minute) >= 60 or int(end_minute) >= 60:
            raise ValueError("ValueError")

        if time.group(3) == "PM" and start_hour != 12:
            start_hour += 12
        elif time.group(3) == "AM" and start_hour == 12:
            start_hour = 0

        if time.group(6) == "PM" and end_hour != 12:
            end_hour += 12
        elif time.group(6) == "AM" and end_hour == 12:
            end_hour = 0

        time1 = f"{start_hour:02}:{start_minute}"
        time2 = f"{end_hour:02}:{end_minute}"

        return f"{time1} to {time2}"
    else:
        raise ValueError("ValueError")

def main():
    try:
        user_input = input("Hours: ")
        print(convert(user_input))
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
