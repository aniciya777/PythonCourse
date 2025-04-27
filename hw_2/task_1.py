import os

from latex_generator_itmo_aniciya import generate_table, generate_image

table = [
    ['Version', 'Latest micro version', 'Release Date', 'End of full support', 'End of security fixes'],
    ['3.2',     '3.2.6',    '2011-02-20',   '2013-05-13',   '2016-02-20'],
    ['3.3',     '3.3.7',    '2012-09-29',   '2014-03-08',   '2017-09-29'],
    ['3.4',     '3.4.10',   '2014-03-16',   '2017-08-09',   '2019-03-18'],
    ['3.5',     '3.5.10',   '2015-09-1',    '2017-08-08',   '2020-09-30'],
    ['3.6',     '3.6.15',   '2016-12-2',    '2018-12-24',   '2021-12-23'],
    ['3.7',     '3.7.17',   '2018-06-27',   '2020-06-27',   '2023-06-06'],
    ['3.8',     '3.8.20',   '2019-10-14',   '2021-05-03',   '2024-10-07'],
    ['3.9',     '3.9.22',   '2020-10-05',   '2022-05-17',   '2025-10'],
    ['3.10',    '3.10.17',  '2021-10-04',   '2023-04-05',   '2026-10'],
    ['3.11',    '3.11.12',  '2022-10-24',   '2024-04-02',   '2027-10'],
    ['3.12',    '3.12.10',  '2023-10-02',   '2025-04-08',   '2028-10'],
    ['3.13',    '3.13.3',   '2024-10-0',    '2026-05',      '2029-10'],
    ['3.14',    '3.14.0a7', '2025-10-07',   '2027-05',      '2030-10'],
]

with open('artifacts/table.tex', 'w', encoding="utf-8") as file:
    print(generate_table(table), file=file)
os.system(r'pdflatex -output-directory=artifacts -aux-directory=artifacts artifacts\table.tex')

with open('artifacts/image.tex', 'w', encoding="utf-8") as file:
    print(generate_image('samples/my cats.jpg'), file=file)
os.system(r'pdflatex -output-directory=artifacts -aux-directory=artifacts artifacts\image.tex')
