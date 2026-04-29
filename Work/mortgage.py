# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        payment = base_payment + extra_payment
    else:
        payment = base_payment

    principal = principal * (1+rate/12) - payment

    if principal < 0:
        total_paid = total_paid - abs(principal)
        principal = 0.0

    total_paid += payment
    left_to_pay = principal

    print(round(total_paid, 2), round(left_to_pay, 2))

print('Total paid', round(total_paid,2))
print('Months', months)