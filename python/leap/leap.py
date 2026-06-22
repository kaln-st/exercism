def leap_year(year):
    
    if type(year) != int:
        raise ValueError("Only positive year will be accept!")
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False