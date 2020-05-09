import math

credit = int(input('Enter the credit principal:\n'))
type_calculations = input(
        'What do you want to calculate?\n' + 'type "m" - for count of months,\n' + 'type "p" - for monthly payment:\n')
if type_calculations == 'm':
    monthly_payment = int(input('Enter monthly payment:\n'))
    months = math.ceil(credit / monthly_payment)

    print(f'\nIt takes {months} {"months" if months > 1 else "month"} to repay the credit')
elif type_calculations == 'p':
    count_months = int(input('Enter count of months:\n'))
    monthly = math.ceil(credit / count_months)
    last_payment = credit - (count_months - 1) * monthly
    if last_payment == monthly:
        print(f'\nYour monthly payment = {monthly}')
    else:
        print(f'\nYour monthly payment = {monthly} with last month payment = {last_payment}.')
