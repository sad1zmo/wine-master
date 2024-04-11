from datetime import datetime
import pandas
import collections


def get_company_years():
    open_years = 1920
    now_year = datetime.now().year
    return now_year - open_years


def get_single_or_plural_years(years):
    if years % 10 == 1 and years % 100 != 11:
        return "год"
    elif 2 <= years % 10 <= 4 and (years % 100 < 10 or years % 100 >= 20):
        return "года"
    else:
        return "лет"


def get_products_from_exel(filepath, sheet_name):
    excel_data_df = pandas.read_excel(filepath, sheet_name=sheet_name,
                                      na_values=[' ', 'N/A', 'NA'],
                                      keep_default_na=False)
    products = excel_data_df.to_dict(orient='records')
    return products


def get_catalog_of_products(products):
    catalog_of_products = collections.defaultdict(list)
    for product in products:
        category = product['Категория']
        catalog_of_products[category].append(product)
    return catalog_of_products
