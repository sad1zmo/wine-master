from datetime import datetime
import pandas
import collections


def get_company_years():
    open_years = 1920
    now_year = datetime.now().year
    return now_year - open_years


def is_year_single_or_plural(years):
    if years % 10 == 1 and years % 100 != 11:
        return "год"
    elif 2 <= years % 10 <= 4 and (years % 100 < 10 or years % 100 >= 20):
        return "года"
    else:
        return "лет"


def get_information_from_exel(filepath, sheet_name):
    excel_data_df = pandas.read_excel(filepath, sheet_name=sheet_name,
                                      na_values=[' ', 'N/A', 'NA'],
                                      keep_default_na=False)
    drink_records = excel_data_df.to_dict(orient='records')
    return drink_records


def get_formated_drinks_data(records_about_drinks):
    formated_drinks_info = collections.defaultdict(list)
    for record_describe in records_about_drinks:
        category = record_describe['Категория']
        formated_drinks_info[category].append(record_describe)
    return formated_drinks_info
