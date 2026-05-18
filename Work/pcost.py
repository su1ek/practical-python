# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        total_cost = 0.0
        rows = csv.reader(f)
        headers = next(rows)
        for n, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                num_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += num_shares * price
            except ValueError:
                print(f"Row {n}: Couldn't convert: {row}")
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'
    
cost = portfolio_cost(filename)
print('Total cost:', cost)

