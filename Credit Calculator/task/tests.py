from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class CreditCalcTest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        print_strs = [
            'Credit principal: 1000',
            'Month 1: paid out 250',
            'Month 2: paid out 250',
            'Month 3: paid out 500',
            'The credit has been repaid!',
        ]

        for print_str in print_strs:
            if print_str not in reply:
                return CheckResult.wrong(
                    'You forgot to output string "{0}"'.format(print_str),
                )

        if not '\n'.join(print_strs) in reply:
            return CheckResult.wrong('You output strings in the wrong order')

        return CheckResult.correct()


if __name__ == '__main__':
    CreditCalcTest('creditcalc.creditcalc').run_tests()
