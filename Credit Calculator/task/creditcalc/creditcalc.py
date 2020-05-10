import math
import sys


class CreditCalculator:

    def __init__(self):
        args = sys.argv
        # test_args = 'credit_calc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8'
        # args = test_args.split()
        args_dict = {}
        if len(args) == 1:
            self.asking_parameters()
            print(self.calculations())
        else:
            for a in range(1, len(args)):
                slicing = args[a].split('=')
                if slicing[0] in ('--payment', '--interest', '--principal'):
                    args_dict[slicing[0]] = float(slicing[1])
                elif slicing[0] == '--periods':
                    args_dict[slicing[0]] = int(slicing[1])
                else:
                    args_dict[slicing[0]] = slicing[1]
            self.check_arguments(args_dict)

    def asking_parameters(self):
        self.mode = input("What do you want to calculate?\n" +
                          'type "n" - for count of months,\n' +
                          'type "a" - for annuity monthly payment,\n' +
                          'type "p" - for credit principal,\n' +
                          'type "d" - for differentiated payment:\n')
        if self.mode != 'p':
            self.principal = int(input('Enter the credit principal:\n'))
        if self.mode != 'a' and self.mode != 'd':
            self.payment = int(input('Enter monthly payment:\n'))
        if self.mode != 'n':
            self.periods = int(input('Enter count of periods:\n'))
        self.interest = float(input('Enter principal interest:\n'))

    def check_arguments(self, args):
        mode = args.get('--type')
        if set(args.keys()) == {'--type', '--principal', '--periods', '--interest'} and \
                args.get('--principal') > 0 and args.get('--periods') > 0 and args.get('--interest') > 0:
            self.principal = args.get('--principal')
            self.periods = args.get('--periods')
            self.interest = args.get('--interest')
            if args.get('--type') == 'diff':
                self.mode = 'd'
            else:
                self.mode = 'a'
            print(self.calculations())
        elif set(args.keys()) == {'--type', '--payment', '--periods', '--interest'} and \
                args.get('--payment') > 0 and args.get('--periods') > 0 and args.get('--interest') > 0:
            self.payment = args.get('--payment')
            self.periods = args.get('--periods')
            self.interest = args.get('--interest')
            self.mode = 'p'
            print(self.calculations())
        elif set(args.keys()) == {'--type', '--principal', '--payment', '--interest'} and \
                args.get('--principal') > 0 and args.get('--payment') > 0 and args.get('--interest') > 0:
            self.principal = args.get('--principal')
            self.payment = args.get('--payment')
            self.interest = args.get('--interest')
            self.mode = 'n'
            print(self.calculations())
        else:
            print('Incorrect parameters')

    def calculations(self):
        rate = self.interest / 12 / 100
        # n - for count of months
        # uses principal, payment, interest
        if self.mode == 'n':
            n = math.ceil(math.log((self.payment / (self.payment - rate * self.principal)), 1 + rate))
            years = n // 12
            months = n - years * 12
            overpayntment = int(n * self.payment - self.principal)
            answer = f'You need {years if years else ""}{" year" + "s" if (years > 1) else "" if years else ""}' \
                     f'{" and " if (years and months) else ""}' \
                     f'{months if months else ""}{" month" + ("s" if (months > 1) else "") if months else ""}' \
                     f' to repay this credit!\nOverpayment = {overpayntment}'
            return answer
        # a - for annuity monthly payment
        # uses principal, periods, interest
        elif self.mode == 'a':
            x = (1 + rate) ** self.periods
            annuity = math.ceil(self.principal * ((rate * x) / (x - 1)))
            overpayntment = int(annuity * self.periods - self.principal)
            return f"Your annuity payment = {annuity}!\nOverpayment = {overpayntment}"
        # p - for credit principal
        # uses payment, periods, interest
        elif self.mode == 'p':
            x = (1 + rate) ** self.periods
            principal = self.payment / ((rate * x) / (x - 1))
            overpayntment = math.ceil(self.payment * self.periods - principal)
            return f"Your credit principal = {int(principal)}!\nOverpayment = {overpayntment}"
        # calculate differentiated payments
        # uses principal, periods, interest
        elif self.mode == 'd':
            overpayntment = - self.principal
            for i in range(1, self.periods + 1):
                payment = math.ceil(
                        self.principal / self.periods + rate * (
                                self.principal - self.principal * (i - 1) / self.periods))
                print(f"Month {i}: paid out {payment}")
                overpayntment += payment
            return f'\nOverpayment = {int(overpayntment)}'


CreditCalculator()
