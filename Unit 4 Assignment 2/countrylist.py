import csv

names = ['name', 'area', 'country code2', 'country code3']
countries = [
['Albania', 28748, 'AL', 'ALB'],
['Algeria', 2381741, 'DZ', 'DZA'],
['American Samoa', 199,'AS','ASM'],
['Andorra', 468,'AD', 'AND'],
['Angola', 1246700, 'AO','AGO' ]
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer (f)

    # write the header
    writer.writerow (names)

    # write multiple rows
    writer.writerows (countries)

