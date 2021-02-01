def is_leap_year(year):
    if(year == 0): # year 0 doesn't exist
        return False
    if (year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True # ex 2000
            return False # ex 1900
        return True # ex 1996
    return False # ex 2015