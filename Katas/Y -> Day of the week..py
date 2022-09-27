from datetime import date
import calendar


def day_of_week(dates):
    dates = dates.split("/")

    my_date = date(int(dates[2]), int(dates[1]), int(dates[0]))
    return calendar.day_name[my_date.weekday()]

print(day_of_week("08/12/2015"))