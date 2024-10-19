months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# January 1, 1970 --> YEAR-MONTH-DAY
# 1/1/1970 --> 1970-01-01

while True:
     try:
        calendar = str(input("Date: ")).strip()

        if calendar[0].isalpha() and "," in calendar:
            parts = calendar.replace(",","").split(" ")
            if len(parts) != 3:
                raise ValueError
            month, day, year = parts[0], parts[1], parts[2]
            month_index = months.index(month) + 1
            if month not in months:
                raise ValueError
            if not (1 <= int(day) <= 31):
                raise ValueError
            print(f"{year}-{month_index:02d}-{int(day):02d}")
            break

        elif calendar[0].isdigit() and "/" in calendar:
            parts = calendar.split("/")
            if len(parts) != 3:
                raise ValueError
            month, day, year = int(parts[0]), int(parts[1]), int(parts[2])
            if not (1 <= month <= 12):
                raise ValueError
            if not (1 <= day <= 31):
                raise ValueError
            print(f"{year}-{month:02d}-{day:02d}")
            break

        else:
            continue

     except(ValueError):
         ...
