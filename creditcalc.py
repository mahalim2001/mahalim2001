# > python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Your loan principal = 800018!
# Overpayment = 246622




import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'], required = True, help = "type")
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--interest', type=float, required = True)
parser.add_argument('--periods', type=int)

args = parser.parse_args()
loan_p = args.principal
monthly_a = args.payment
loan_i = args.interest
monthly_n = args.periods
if loan_i > 1:
    loan_i = loan_i / 100 / 12
else:
    loan_i = loan_i / 12
    # print('monthly interest is : %s' % loan_i)
over_payment = 0
if args.type == "diff":
    print('Differential calculation')
    if not monthly_a:
        for n in range(monthly_n):
            d = math.ceil(loan_p / monthly_n + (loan_i * (loan_p - (loan_p * (n + 1 - 1) / monthly_n))))
            over_payment += d
            print("Month", n+1 ,"Payment is ", d)
        print("Over Pyment = ", over_payment - loan_p)

    else:
        print("This calculate the differential payment, please chose 'anuuity'")
    exit()

if args.type == "annuity":
    print("annuity calculation")
    print('principal', loan_p)
    print('payment', monthly_a)
    print('interest', loan_i)
    print('periods', monthly_n)
# number of monthly payments
    if not monthly_n:
        # loan_p = float(input('Enter the loan principal :'))
        # monthly_a = float(input('Enter the monthly payment: '))
        # loan_i = float(input('Enter the loan interest: '))
        loan_con = -(math.log(1 - (loan_i * loan_p / monthly_a)))
        monthly_n = math.ceil(loan_con / math.log(1 + loan_i))
        print('Number of months :', monthly_n)
        y_n = monthly_n // 12
        m_n = math.ceil((monthly_n - y_n * 12))
        # print('Number of years :', y_n)
        # print('Number of months :', m_n)
        if monthly_n % 12 == 0:
            print(f'It will take {y_n} years to repay this loan!')
        elif monthly_n > 12:

            if y_n > 1:
                y = 'years'
            if y_n == 1:
                y = 'year'
            if m_n > 1:
                m = 'months'
            if m_n == 1:
                m = 'month'
            print(f'It will take {y_n} {y} and {m_n} {m} to repay this loan!')
        else:
            if m_n > 1:
                if m_n < 12:
                    m = 'months'
                else:
                    m = ""
            elif m_n == 1:
                m = 'month'

            print(f'It will take {m_n} {m} to repay this loan!')
            print('Over payment', ((y_n * 12 + m_n) * monthly_a)-loan_p)

    # annuity monthly payment amount
    if not monthly_a:
        # loan_p = float(input('Enter the loan principal :'))
        # monthly_n = int(input('Enter the number of monthly payment: '))
        # loan_i = float(input('Enter the loan interest: '))
        loan_con = (1-(1 / (1 + loan_i) ** monthly_n))
        monthly_a = math.ceil(loan_p * loan_i / loan_con)
        print('Your monthly payment : ', monthly_a)
        print('Over payment :', monthly_a * monthly_n-loan_p)

    # loan principal
    if not loan_p:
        # monthly_a = float(input('Enter the monthly payment: '))
        # monthly_n = int(input('Enter the number of monthly payment: '))
        # loan_i = float(input('Enter the loan interest: '))
        if loan_i == 0.0:
            Loan_p = monthly_a * monthly_n
        else:
            loan_con = (1-(1 / (1 + loan_i) ** monthly_n))
            loan_p = monthly_a / loan_i * loan_con
        print('Your loan principal : %s' % math.floor(loan_p), '!')
        print('Over Payment :', math.floor(monthly_a * monthly_n - loan_p))

