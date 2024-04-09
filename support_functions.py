from datetime import datetime


def get_company_years():
    open_years = 1920
    now_year = datetime.now().year
    return now_year - open_years


def single_or_plural(years):
    if years % 10 == 1 and years % 100 != 11:
        return "год"
    elif 2 <= years % 10 <= 4 and (years % 100 < 10 or years % 100 >= 20):
        return "года"
    else:
        return "лет"
