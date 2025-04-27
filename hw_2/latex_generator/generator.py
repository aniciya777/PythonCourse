import os
from datetime import date
from string import Template
from typing import List

TEMPLATE = Template(r"""\documentclass{article}
\usepackage{graphicx}
\title{python}
\author{ $user }
\date{ $date }
\begin{document}
$table
\end{document}""")


def generate_table(table: List[List[str]]) -> str:
    """
    Generates a latex table from the given list of rows.

    :param table: 2d list of cells
    :return: latex document with table
    """
    count_columns = max(map(len, table))  # максимальное количество столбцов
    table_str = [
        list(map(str, row)) + [''] * (count_columns - len(row))  # заполняем пустыми строками остальные столбцы
        for row in table
    ]

    content = r'''\begin{table}
    \centering
    \begin{tabular}{''' + '|c' * count_columns + '|}\n'''
    for row in table_str:
        content += '        \\hline \n'
        content += '        ' + ' & '.join(row) + ' \\\\\n'
    content += r'''         \hline
    \end{tabular}
\end{table}'''

    user = os.getenv('USER') or os.getenv('USERNAME') or os.getenv('LOGNAME') or ''
    return TEMPLATE.substitute(
        date=date.today().strftime('%d %B %Y'),
        user=user,
        table=content
    )
