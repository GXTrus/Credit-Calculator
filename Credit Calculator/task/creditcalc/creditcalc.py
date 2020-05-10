import math


class CreditCalculator:

    def __init__(self):
        self.mode = input("What do you want to calculate?\n" +
                          'type "n" - for count of months,\n' +
                          'type "a" - for annuity monthly payment,\n' +
                          'type "p" - for credit principal:\n')
        if self.mode != 'p':
            self.credit = float(input('Enter the credit principal:\n'))
        if self.mode != 'a':
            self.monthly = float(input('Enter monthly payment:\n'))
        if self.mode != 'n':
            self.count = int(input('Enter count of periods:\n'))
        self.interest = float(input('Enter credit interest:\n'))
        print(self.calculations())

    def calculations(self):
        rate = self.interest / 12 / 100
        if self.mode == 'n':
            n = math.ceil(math.log((self.monthly / (self.monthly - rate * self.credit)), 1 + rate))
            years = n // 12
            months = n - years * 12
            answer = f'You need {years if years else ""}{" year" + "s" if (years > 1) else "" if years else ""}' \
                     f'{" and " if (years and months) else ""}' \
                     f'{months if months else ""}{" month" + ("s" if (months > 1) else "") if months else ""}' \
                     f' to repay this credit!'
            return answer
        elif self.mode == 'a':
            x = (1 + rate) ** self.count
            annuity = math.ceil(self.credit * ((rate * x) / (x - 1)))
            return f"Your annuity payment = {annuity}!"
        elif self.mode == 'p':
            x = (1 + rate) ** self.count
            principal = self.monthly / ((rate * x) / (x - 1))
            return f"Your credit principal = {int(principal)}!"


CreditCalculator()
