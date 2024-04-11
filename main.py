from http.server import HTTPServer, SimpleHTTPRequestHandler
from support_functions import get_company_years, \
                              get_single_or_plural_years, \
                              get_products_from_exel, \
                              get_catalog_of_products
from jinja2 import Environment, FileSystemLoader, select_autoescape
from environs import Env


def main():
    env = Env()
    exel_filepath = env.str('EXEL_FILEPATH', default='wine.xlsx')
    exel_sheet_name = env.str('EXEL_SHEET_NAME', default='Лист1')

    jinja_env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = jinja_env.get_template('template.html')
    catalog = get_catalog_of_products(
            get_products_from_exel(exel_filepath, exel_sheet_name))

    rendered_page = template.render(
        years=get_company_years(),
        number_of_years=get_single_or_plural_years(get_company_years()),
        catalog=catalog,
        )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
