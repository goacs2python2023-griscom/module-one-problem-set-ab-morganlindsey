def numBusses(students):
    if (students % 52 == 0):
        return int(students / 52)
    else:
        return int(students / 52) + 1
print(numBusses(104))