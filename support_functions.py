from datetime import datetime
import pandas
import collections


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


def get_information_from_exel(file, sheet_name):
    excel_data_df = pandas.read_excel(file, sheet_name=sheet_name,
                                      na_values=[' ', 'N/A', 'NA'],
                                      keep_default_na=False)
    list_of_dicts = excel_data_df.to_dict(orient='records')
    return list_of_dicts


def get_formated_data(list_of_dicts):
    wine_dict = collections.defaultdict(list)
    for wine_info in list_of_dicts:
        category = wine_info['Категория']
        wine_dict[category].append(wine_info)
    return wine_dict
