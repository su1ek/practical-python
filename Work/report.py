# report.py
#
# Exercise 2.4

import csv
import sys



def read_portfolio(filename):
    with open(filename, 'rt') as f:
        portfolio = []
        total_cost = 0.0
        rows = csv.reader(f)
        headers = next(rows)
        for n, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                name = record['name']
                num_shares = int(record['shares'])
                price = float(record['price'])
                holding = (name, num_shares, price)
                portfolio.append(holding)
            except ValueError:
                print(f"Row {n}: Couldn't convert: {row}")
    return portfolio

def read_prices(filename):
    with open(filename, 'r') as f:
        prices = {}
        rows = csv.reader(f)
        for row in rows:
            if not row:
                continue
            if row[0] == '<null>':
                continue
            name = row[0]
            try:
                price = float(row[1])
                prices[name] = price
            except ValueError:
                continue
        return prices

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

total = 0.0
current_value = 0.0

for name, shares, price in portfolio:
    if name in prices:
        current_price = prices[name]
        current_value += shares * current_price
    total += shares * price

gain_loss = current_value - total

print('Total cost:', total)
print('Today value:', current_value)
print(f'Gain/Loss: {gain_loss:0.2f}')
