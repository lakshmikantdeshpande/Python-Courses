import re


def process_date(this_date):
    if not re.search(r'^\d\d\d\d-\d\d-\d\d$', this_date):
        raise ValueError('Please submit date in YYYY-MM-DD format')

    print('The submitted date is {}'.format(this_date))


process_date('1980-01-03')
print()
process_date('1/1/2013')
