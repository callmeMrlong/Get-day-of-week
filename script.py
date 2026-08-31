from datetime import datetime


def get_day(date_string):
    date_object = datetime.strptime(date_string, "%m/%d/%Y")
    return date_object.strftime("%A")


def generate_date_list():
    date_list = []
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for year in range(1, 10000):
        year_str = f"{year:04d}"

        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        for month in range(1, 13):
            month_str = f"{month:02d}"

            if month == 2 and is_leap_year:
                max_days = 29
            else:
                max_days = days_in_months[month]

            for day in range(1, max_days + 1):
                day_str = f"{day:02d}"
                date_list.append(f"{month_str}/{day_str}/{year_str}")

    return date_list


all_dates = generate_date_list()


def build():
    with open("dates_output.py", "w") as file:
        file.write('date = input("pick any date in MM/DD/YYYY format and find out what day of the week it was")')
        for i in all_dates:
            file.write(f"if date == '{i}': print('{get_day(i)}')\n")


build()
