# how many sundays on the first of a month from jan 1 1901 to dec 31 2000
#    1 Jan 1900 was a Monday.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

print("Program started")
count = 0
weekday = 2 # 0 - 6 for sunday - saturday, january 1 1901 was a tuesday
year = 1901 # starting year
month = 0
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
day = 1
length = {
    "jan" : 31,
    "feb" : 28,
    "mar" : 31,
    "apr" : 30,
    "may" : 31,
    "jun" : 30,
    "jul" : 31,
    "aug" : 31,
    "sep" : 30,
    "oct" : 31,
    "nov" : 30,
    "dec" : 31
}

while year <= 2000:
    # check if the prerequisite is met
    if (day == 1 and weekday == 0):
        count += 1
    
    # iterate all of the correct variables up
    isLeapYearDay = month == 1 and year%4 == 0 and day == 28 # and (year%100 !=0 or year % 400 == 0) 
    
    weekday = (weekday+1) % 7 # keeps within the 0-6 desired range
    day += 1
    

    if (day >= length[months[month]] and not isLeapYearDay):
        day = 1
        month += 1
        if month == 12:
            month = 0
            year += 1

print(count)