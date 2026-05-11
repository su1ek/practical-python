# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        total_cost = 0.0
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                continue
    return total_cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)

