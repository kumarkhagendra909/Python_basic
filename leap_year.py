"""
A leap year comes for 1 after every 4 years
a leap year year is divisible by 4,100,400 , if any of these condition proved wrong then
it is not a leap year

"""
year = int(input("Enter the year :- "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            # Block of 400
            print("{0}  is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

