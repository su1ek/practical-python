# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        total_cost = 0.0
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                continue
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

