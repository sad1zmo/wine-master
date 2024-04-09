from http.server import HTTPServer, SimpleHTTPRequestHandler
from support_functions import get_company_years, \
                              single_or_plural, \
                              get_information_from_exel, \
                              get_formated_data
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    years=get_company_years(),
    single_or_plural=single_or_plural(get_company_years()),
    wines_info=get_formated_data(
        get_information_from_exel('wine.xlsx', 'Лист1')),
    categories=get_formated_data(
        get_information_from_exel('wine.xlsx', 'Лист1')).keys()
    )


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
