def isleapyear(year):
    year_div_4 = year % 4
    year_div_100 = year % 100
    year_div_400 = year % 400
    if(year_div_4 == 0):
        if(year_div_100 == 0):
            if(year_div_400 ==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False