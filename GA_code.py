import math
def date_trans(date_s):
    year, month, day = map(int, date_s.strip().split('.'))
    if month == 1:
        n_date = day
    elif month == 2:
        n_date = day + 31
    elif month == 3:
        n_date = day + 31 + 28
    elif month == 4:
        n_date = day + 31 + 28 + 31
    elif month == 5:
        n_date = day + 31 + 28 + 31 + 30
    elif month == 6:
        n_date = day + 31 + 28 + 31 + 30 + 31
    elif month == 7: 
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
    return n_date