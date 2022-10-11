def century(year):

    if (year % 100 == 0):
        return year // 100
    elif (year <= 100):
        return 1
    else:
        return year // 100 + 1



print(century(1705))
print(century(356))
print(century(89))
print(century(2000))