def divisionFunction(year):
    if (year % 4) == 0:
        if (year % 400) == 0:
            return True
        elif (year % 100) == 0:
            return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    leap_year = divisionFunction(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year is True and month == 2:
        month_days[1] += 1
    month_index = month - 1
    number_of_days = month_days[month_index]

    return number_of_days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"There is {days}days in month no- {month} of year- {year}")
