from pathlib import Path
from model import Combination, Stock
from jinja2 import Template
import re


def display_report_template():
    template = Template('''
    <html>
    <head>
        <title>{{ report_title }}</title>
    </head>
    <body>
        <h1>{{ report_title }}</h1>
        <h4>Total amount investment is {{total_investment}},number of stocks in the portfolio is {{number_actions}}</h4>
        <h4>Profit of the investment is {{best_profit}}</h4>
        <h4>The time used of the Algorithm is {{time}} seconds ,and memory used is {{memory}} MB</h4>
        <table>
            <tr>
                {% for column in columns %}
                <th>{{ column }}</th>
                {% endfor %}
            </tr>
            {% for item in report_data %}
            <tr>
                {% for column in columns %}
                <td>{{ item[column] }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    ''')
    return template


def report(best_portfolio: Combination, filename: str):
    combinations = best_portfolio.stocks
    report_title = 'report of' + ' ' + str(filename)
    columns = ['name', 'price', 'profit']
    report_data = []
    for combination in combinations:
        report_data.append({
            'name': combination.name,
            'price': combination.print_price,
            'profit': combination.print_profit,
        })

    return report_title, columns, report_data


def generate_report(report_title: str, columns: list[str], report_data: list[dict], best_profit, time, memory,
                    total_investment, number_actions):
    # get three attributes to generate with html template
    filename = re.sub(r"\s+", "_", report_title)
    template = display_report_template()
    report_html = template.render(report_title=report_title, columns=columns, report_data=report_data,
                                  best_profit=best_profit, time=time, memory=memory, total_investment=total_investment,
                                  number_actions=number_actions)
    filename = Path(filename + ".html")
    with open(filename, 'w') as f:
        f.write(report_html)
