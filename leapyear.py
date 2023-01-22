def leapYear(year):
    if (year % 100 == 0 and year % 400 != 0):
        return False
    if (year % 400 == 0 or year % 4 == 0):
        return True
 
print(leapYear(1600))
print(leapYear(1500))
